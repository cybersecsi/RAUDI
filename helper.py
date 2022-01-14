import requests
import re
import shutil
from errors import Errors
from python_on_whales import docker
from os import listdir
from os.path import isfile, join
import json

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

def log(m):
    print("[+] {}".format(m))

def logErr(m):
    print("[-] {}".format(m))

def get_highest_version_number(version_numbers):
    version_numbers.sort(key=lambda s: list(map(int, s.strip('v').split('.'))))
    return version_numbers[-1]

def get_latest_docker_hub_version(docker_image, org="library/", avoid_date=False):
    url = "{base}{org}{image}{tags}".format(base=DOCKER_API['base'], org=org, image=docker_image, tags=DOCKER_API['tags'])
    r = requests.get(url)
    results = r.json()['results']
    regex = '^[v]?\d+(\.\d+)*$' if avoid_date == False else '^[v]?\d{1,4}(\.\d+)*$' # Only digits and dots (avoid Date-based tags)
    tags_with_version_number = [result["name"] for result in results if re.match(regex, result["name"])]
    if len(tags_with_version_number) > 0:
        return get_highest_version_number(tags_with_version_number)
    else:
        return 'latest'

def get_latest_pip_version(package):
    url = "{base}{package}{json}".format(base=PYPI_API['base'], package=package, json=PYPI_API['json'])
    r = requests.get(url)
    version = r.json()['info']['version']
    return version

def get_latest_npm_registry_version(package):
    url = "{base}{package}{release}".format(base=NPM_REGISTRY_API['base'], package=package, release=NPM_REGISTRY_API['latest_release'])
    r = requests.get(url)
    version = r.json()['version']
    return version

def get_latest_github_release(repo, target_string):
    url = "{base}{repo}{release}".format(base=GITHUB_API['base'], repo=repo, release=GITHUB_API['latest_release'])
    r = requests.get(url)
    try:
        assets = r.json()['assets']
        for asset in assets:
            if target_string in asset['name']:
                return {
                    'url': asset['browser_download_url'],
                    'version': r.json()['tag_name']
                }
    except:
        logErr('Error while retriving info from GitHub. Maybe Rate Limiting took place...')

def get_latest_github_release_no_browser_download(repo):
    try:
        url = "{base}{repo}{release}".format(base=GITHUB_API['base'], repo=repo, release=GITHUB_API['latest_release'])
        r = requests.get(url)
        data = r.json()
    except Exception as e: 
        raise Errors.github_json()

    if r.status_code != 200:
        # TODO Check that an error always return message val
        raise Errors.connection_error(repo, r.status_code, data['message'])
    return {
        'url': data['tarball_url'],
        'version': data['tag_name']
    }

def get_latest_github_tag_no_browser_download(repo):
    try:
        url = "{base}{repo}{tags}".format(base=GITHUB_API['base'], repo=repo, tags=GITHUB_API['tags'])
        r = requests.get(url)
        results = r.json()
    except Exception as e: 
        raise Errors.github_request()

    regex = '^[v]?\d{1,4}(\.\d+)*$' # Only digits and dots (avoid Date-based tags)
    if r.status_code != 200:
        # TODO Check that an error always return message val
        raise Errors.connection_error(repo, r.status_code, results['message'])

    data = [result for result in results if re.match(regex, result['name'])]
    versions = [d["name"] for d in data]
    if len(versions) > 0:
        latest_version = get_highest_version_number(versions)
        index = next((i for i, item in enumerate(data) if item["name"] == latest_version), -1)
        return {
            'url': data[index]['tarball_url'],
            'version': latest_version
        }

def get_latest_github_commit(repo):
    url = "{base}{repo}{commits}".format(base=GITHUB_API['base'], repo=repo, commits=GITHUB_API['commits'])
    r = requests.get(url)
    results = r.json()

    if r.status_code != 200:
        # TODO Check that an error always return message val
        msg = json.loads(r.text)['message']
        raise ConnectionError(msg)
    
    data = results[0]['commit']['author']['date'][:10] # YYYY-MM-DD
    latest_commit_date = ''.join(data.split('-'))
    return latest_commit_date

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
        docker.run('{docker_image}:{version}'.format(docker_image=docker_image, version=version), command=command, detach=False)

def check_if_readme_is_set(docker_image):
    url = "{base}{image}".format(base=DOCKER_API['base'], image=docker_image)
    r = requests.get(url)
    data = r.json()
    return data['full_description'] != None

def get_list_tools():
    """A function to get the tools based on the directory names in /tools"""
    return [f for f in listdir('tools') if not isfile(join('tools', f)) and f != '__pycache__']

def get_config_names():
    return ['tools.{}.config'.format(t) for t in get_list_tools()]

def get_list_templates():
    return [f for f in listdir('templates') if not isfile(join('templates', f)) and f != 'DOCKERHUB.md']

def create_tool_folder(tool_name, template):
    shutil.copytree('templates/'+template, 'tools/'+tool_name)
    shutil.copy('templates/DOCKERHUB.md', 'tools/'+tool_name+'/README.md')
