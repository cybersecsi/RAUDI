import requests
import re
import shutil
import sys
from .errors import Errors
from python_on_whales import docker
from os import listdir, getenv
from os.path import isfile, join

# Global vars
DOCKER_API = {
    'base': "https://hub.docker.com/v2/repositories/",
    'tags': "/tags?page=1&page_size=50"
}
PYPI_API = {
    'base': "https://pypi.org/pypi/",
    'json': "/json"
}
NPM_REGISTRY_API = {
    'base': "https://registry.npmjs.org/",
    'latest_release': "/latest"
}
GITHUB_API = {
    'base': "https://api.github.com/repos/",
    'commits': "/commits",
    'latest_release': "/releases/latest",
    'tags': "/tags"
}
GITLAB_API = {
    'base': "https://gitlab.com/api/v4/projects/",
    'commits': "/repository/commits", 
    'latest_release': "/releases",
    'tags' : "/repository/tags",
    'archive': "/repository/archive"
}

def _response_error_message(response):
    try:
        data = response.json()
    except (TypeError, ValueError):
        data = None

    if isinstance(data, dict) and data.get('message'):
        return data['message']

    return getattr(response, 'reason', None) or 'request failed'

def _get_response(url, resource, **kwargs):
    try:
        response = requests.get(url, **kwargs)
    except requests.RequestException as error:
        raise ConnectionError('Unable to request "{}": {}'.format(resource, error)) from error

    if not 200 <= response.status_code < 300:
        raise Errors.connection_error(
            resource,
            response.status_code,
            _response_error_message(response),
        )

    return response

def _get_json(response, resource):
    try:
        return response.json()
    except (TypeError, ValueError) as error:
        raise ValueError('Invalid JSON response for "{}"'.format(resource)) from error

def log(m):
    print("[+] {}".format(m))
    flushIfGithubAction()

def logErr(m):
    print("[-] {}".format(m))
    flushIfGithubAction()

def flushIfGithubAction():
    enable_stdout_flush_env = get_env('RAUDI_GITHUB_ACTION', False)
    enable_stdout_flush = False if (enable_stdout_flush_env == False) or (enable_stdout_flush_env == "False") else True
    if (enable_stdout_flush):
        sys.stdout.flush()

def get_env(NAME, default_value=None):
    """Returns and environment variable
    Args:
        NAME (String): The environment variable to be returned
    Raises:
        NotImplementedError: Throws if the env is not found
    Returns:
        String: The environment variable value
    """
    r = getenv(NAME)
    if not r:
        if default_value is None:
            # TODO: Alert the user that the variable is unset.
            raise NotImplementedError('{} Environment Variable not found'.format(NAME))
        return default_value
    return r

def get_highest_version_number(version_numbers):
    version_numbers.sort(key=lambda s: list(map(int, s.strip('v').split('.'))))
    return version_numbers[-1]

def get_latest_docker_hub_version(docker_image, org="library/", avoid_date=False):
    url = "{base}{org}{image}{tags}".format(base=DOCKER_API['base'], org=org, image=docker_image, tags=DOCKER_API['tags'])
    r = _get_response(url, docker_image)
    results = _get_json(r, docker_image)['results']
    regex = r'^[v]?\d+(\.\d+)*$' if avoid_date == False else r'^[v]?\d{1,4}(\.\d+)*$' # Only digits and dots (avoid Date-based tags)
    tags_with_version_number = [result["name"] for result in results if re.match(regex, result["name"])]
    if len(tags_with_version_number) > 0:
        return get_highest_version_number(tags_with_version_number)
    else:
        return 'latest'

def get_latest_pip_version(package):
    url = "{base}{package}{json}".format(base=PYPI_API['base'], package=package, json=PYPI_API['json'])
    r = _get_response(url, package)
    version = _get_json(r, package)['info']['version']
    return version

def get_latest_npm_registry_version(package):
    url = "{base}{package}{release}".format(base=NPM_REGISTRY_API['base'], package=package, release=NPM_REGISTRY_API['latest_release'])
    r = _get_response(url, package)
    version = _get_json(r, package)['version']
    return version

def get_github_headers():
    github_token = getenv('RAUDI_GITHUB_TOKEN')
    if not github_token:
        return {}
    else:
        return {
            'Authorization': "token {github_token}".format(github_token=github_token)
        }

def get_latest_github_release(repo, target_string):
    url = "{base}{repo}{release}".format(base=GITHUB_API['base'], repo=repo, release=GITHUB_API['latest_release'])
    r = _get_response(url, repo, headers=get_github_headers())
    try:
        data = _get_json(r, repo)
        assets = data['assets']
        for asset in assets:
            if target_string in asset['name']:
                return {
                    'url': asset['browser_download_url'],
                    'version': data['tag_name']
                }
    except KeyError as e:
        raise Exception('Key {key} not found'.format(key=e))
    except Exception as e:
        raise Exception(e)

    raise LookupError('No release asset matching "{}" found for "{}"'.format(target_string, repo))

def get_latest_github_release_no_browser_download(repo):
    url = "{base}{repo}{release}".format(base=GITHUB_API['base'], repo=repo, release=GITHUB_API['latest_release'])
    r = _get_response(url, repo, headers=get_github_headers())
    data = _get_json(r, repo)
    return {
        'url': data['tarball_url'],
        'version': data['tag_name']
    }

def get_latest_github_tag_no_browser_download(repo):
    url = "{base}{repo}{tags}".format(base=GITHUB_API['base'], repo=repo, tags=GITHUB_API['tags'])
    r = _get_response(url, repo, headers=get_github_headers())
    results = _get_json(r, repo)

    regex = r'^[v]?\d{1,4}(\.\d+)*$' # Only digits and dots (avoid Date-based tags)
    data = [result for result in results if re.match(regex, result['name'])]
    versions = [d["name"] for d in data]
    if len(versions) > 0:
        latest_version = get_highest_version_number(versions)
        index = next((i for i, item in enumerate(data) if item["name"] == latest_version), -1)
        return {
            'url': data[index]['tarball_url'],
            'version': latest_version
        }

    raise LookupError('No version tags found for "{}"'.format(repo))


def get_latest_github_commit(repo):
    url = "{base}{repo}{commits}".format(base=GITHUB_API['base'], repo=repo, commits=GITHUB_API['commits'])
    r = _get_response(url, repo, headers=get_github_headers())
    results = _get_json(r, repo)
    
    data = results[0]['commit']['author']['date'][:10] # YYYY-MM-DD
    latest_commit_date = ''.join(data.split('-'))
    return latest_commit_date



def get_gitlab_id_project(owner, project):
    """Get id gitlab form projet

    Args:
        owner (string): The owner
        project (string): The project name

    Raises:
        ConnectionError: if a connection error occurs
        Errors.gitlab_request: if the gitlab req fails

    Returns:
        [type]: [description]
    """
    expected_path = "{}/public/{}".format(owner, project)
    try:
        url = "{base}?search={project}".format(base=GITLAB_API['base'], project=project)
        r = _get_response(url, expected_path)
        results = _get_json(r, expected_path)
        for d in results: 
            if d['path_with_namespace'] == expected_path:
                return d['id']

        raise Errors.gitlab_not_found()
    except ConnectionError:
        raise
    except Exception as e: 
        raise Errors.gitlab_request()
    
# https://gitlab.com/api/v4/projects/7348427/repository/tags
def get_latest_gitlab_tag(owner, project):
    try:
        # Get id_project
        id_project = get_gitlab_id_project(owner, project)
        url = "{base}{id_project}{tags}".format(base=GITLAB_API['base'], id_project=id_project, tags=GITLAB_API['tags'])
        r = _get_response(url, "{}/{}".format(owner, project))
        results = _get_json(r, "{}/{}".format(owner, project))
        # latest tag
        tag = results[0]['name']
        commid = results[0]['commit']['id']
        # https://gitlab.com/projects/:id/repository/archive?sha=<commid>

        return {
            'url' : "{}{}{}?sha={}".format(GITLAB_API['base'], id_project, GITLAB_API['archive'], commid),
            'version': tag
        }
    except ConnectionError:
        raise
    except Exception as e: 
        raise Errors.gitlab_request()


def get_latest_gitlab_commit(owner, project):
    try:
        # Get id_project
        id_project = get_gitlab_id_project(owner, project)
        url = "{base}{id_project}{commits}".format(base=GITLAB_API['base'], id_project=id_project, commits=GITLAB_API['commits'])
        r = _get_response(url, "{}/{}".format(owner, project))
        results = _get_json(r, "{}/{}".format(owner, project))
        # latest tag
        date = results[0]['committed_date'][:10] #YYYY-MM-DD
        latest_commit_date = ''.join(date.split('-'))
        return latest_commit_date
        # https://gitlab.com/projects/:id/repository/archive?sha=<commid>
    except ConnectionError:
        raise
    except Exception as e: 
        raise Errors.gitlab_request()


def get_remote_resource(url, json=False):
    r = _get_response(url, url)
    if json:
        return _get_json(r, url)
    else:
        return r.text

def grep(the_output, to_search):
    """Looks for to_search string and returns a list of found elements
    Args:
        the_output (string): the output of a get request
        to_search (string): The string to be searched
    Returns:
        list: The list of strings obtained by grep
    """
    lines = the_output.split("\n")
    found = []
    for line in lines:
        if to_search in line:
            found.append(line.strip())
    return found


def check_if_docker_image_exists_local(docker_image):
    return docker.image.exists(docker_image)

def check_if_docker_image_exists_remote(docker_image_with_version):
    docker_image = docker_image_with_version.split(':')
    repo = docker_image[0]
    version = docker_image[1]
    latest_ver = get_latest_docker_hub_version(repo, org="")
    return True if latest_ver == version else False

def check_if_docker_image_exists(docker_image, remote_src):
    # The check can be made against the local Docker or the Docker Hub (mainly for GitHub Actions) based on the value of 'remote_src'
    if not remote_src:
        log('Checking on local Docker if {image} already exists...'.format(image=docker_image))
        return check_if_docker_image_exists_local(docker_image)
    else:
        log('Checking on Docker Hub if {image} already exists...'.format(image=docker_image))
        return check_if_docker_image_exists_remote(docker_image)

def check_if_container_runs(docker_image, version, tests):
    log('Executing tests for container {docker_image}:{version}'.format(docker_image=docker_image, version=version))
    for test in tests:
        # docker.run() will try to pull the image if it doesn't exist
        # `command` should be a list of string(s) - e.g. ['ls'] or ['ls', '-l']
        command = test.split(' ')
        docker.run('{docker_image}:{version}'.format(docker_image=docker_image, version=version), command=command, remove=True , detach=False)

def check_if_readme_is_set(docker_image):
    url = "{base}{image}".format(base=DOCKER_API['base'], image=docker_image)
    r = _get_response(url, docker_image)
    data = _get_json(r, docker_image)
    return data['full_description'] != None

def print_docker_build_command(name, version, buildargs):
    buildargs_docker_cmd = ['--build-arg {key}={value}'.format(key=key, value=value) for key, value in buildargs.items()]
    buildargs_cmd = ' '.join(buildargs_docker_cmd)
    log("The command executed is the following:")
    log("docker build . {buildargs_cmd} -t {name}:{version}".format(buildargs_cmd=buildargs_cmd, name=name, version=version ))

def check_and_fill_args(tool_name, buildargs, common_args, tools_dir='tools'):
    """Fill common Docker build arguments and reject missing required ones."""
    if not isinstance(buildargs, dict):
        raise TypeError('buildargs for "{}" must be a dictionary'.format(tool_name))
    if not isinstance(common_args, dict):
        raise TypeError('common_args must be a dictionary')

    dockerfile_path = join(tools_dir, tool_name, 'Dockerfile')
    dockerfile_args = {}
    arg_pattern = re.compile(r'^\s*ARG\s+([A-Za-z_][A-Za-z0-9_]*)(\s*=)?')

    with open(dockerfile_path, encoding='utf-8') as dockerfile:
        for line in dockerfile:
            match = arg_pattern.match(line)
            if match:
                name = match.group(1)
                has_default = match.group(2) is not None
                dockerfile_args[name] = dockerfile_args.get(name, False) or has_default

    filled_args = dict(buildargs)
    missing_args = []

    for name, has_default in dockerfile_args.items():
        if name in filled_args:
            continue
        if name in common_args:
            filled_args[name] = common_args[name]
        elif not has_default:
            missing_args.append(name)

    if missing_args:
        raise ValueError(
            'Tool "{}" is missing required Docker build argument(s): {}'.format(
                tool_name,
                ', '.join(missing_args),
            )
        )

    return filled_args

def get_list_tools():
    """A function to get the tools based on the directory names in /tools"""
    tools=[f for f in listdir('tools') if not isfile(join('tools', f)) and f != '__pycache__']
    tools.sort()
    return tools

def check_tools():
    """Validate that every tool directory contains its required files."""
    required_files = ('config.py', 'Dockerfile')
    missing_files = {}

    for tool in get_list_tools():
        missing = [
            filename
            for filename in required_files
            if not isfile(join('tools', tool, filename))
        ]
        if missing:
            missing_files[tool] = missing

    if missing_files:
        raise Errors.invalid_tools(missing_files)

def get_config_names():
    check_tools()
    return ['tools.{}.config'.format(t) for t in get_list_tools()]

def get_list_templates():
    return [f for f in listdir('templates') if not isfile(join('templates', f)) and f != 'DOCKERHUB.md']

def create_tool_folder(tool_name, template):
    shutil.copytree('templates/'+template, 'tools/'+tool_name)
    shutil.copy('templates/DOCKERHUB.md', 'tools/'+tool_name+'/README.md')


def clean_version(v):
    v = re.sub('[-_]', '.', v) # 1.2.0-beta.2
    v = re.sub('[a-zA-Z]', '', v)
    v = v.replace('..', '.')
    v = v.strip()
    v = v.strip('.')
    return v
