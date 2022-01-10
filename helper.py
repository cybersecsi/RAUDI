import requests
import re
import docker
from os import listdir
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

def get_latest_docker_hub_version(docker_image, org="library/"):
    r = requests.get(DOCKER_API['base']+org+docker_image+DOCKER_API['tags'])
    results = r.json()['results']
    regex = '^\d{1,4}(\.\d+)*$' # Only digits and dots (avoid Date-based tags)
    tags_with_version_number = [result["name"] for result in results if re.match(regex, result["name"])]
    if len(tags_with_version_number) > 0:
        return get_highest_version_number(tags_with_version_number)
    else:
        return 'latest'

def get_latest_pip_version(package):
    r = requests.get(PYPI_API['base']+package+PYPI_API['json'])
    version = r.json()['info']['version']
    return version

def get_latest_npm_registry_version(package):
    r = requests.get(NPM_REGISTRY_API['base']+package+NPM_REGISTRY_API['latest_release'])
    version = r.json()['version']
    return version

def get_latest_github_release(repo, target_string):
    r = requests.get(GITHUB_API['base']+repo+GITHUB_API['latest_release'])
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
    r = requests.get(GITHUB_API['base']+repo+GITHUB_API['latest_release'])

    data = r.json()
    if r.status_code != 200:
        # TODO Check that an error always return message val
        raise ConnectionError(data['message'])
    return {
        'url': data['tarball_url'],
        'version': data['tag_name']
    }

def get_latest_github_tag_no_browser_download(repo):
    r = requests.get(GITHUB_API['base']+repo+GITHUB_API['tags'])
    regex = '^[v]?\d{1,4}(\.\d+)*$' # Only digits and dots (avoid Date-based tags)
    results = r.json()

    if r.status_code != 200:
        # TODO Check that an error always return message val
        raise ConnectionError(results['message'])

    data = [result for result in results if re.match(regex, result['name'])]
    versions = [d["name"] for d in data]
    if len(versions) > 0:
        latest_version = get_highest_version_number(versions)
        index = next((i for i, item in enumerate(data) if item["name"] == latest_version), -1)
        return {
            'url': data[index]['tarball_url'],
            'version': latest_version
        }

def check_if_docker_image_exists_local(docker_image):
    client = docker.from_env()
    try:
        res = client.images.get(docker_image)
        return True
    except docker.errors.ImageNotFound:
        return False

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
    client = docker.from_env()
    log('Executing tests for container {docker_image}:{version}'.format(docker_image=docker_image, version=version))
    for test in tests:
        client.containers.run('{docker_image}:{version}'.format(docker_image=docker_image, version=version), test, detach=False)


def get_list_tools():
    return [f for f in listdir('tools') if not isfile(join('tools', f)) and f != '__pycache__']

def get_config_names():
    return ['tools.{}.config'.format(t) for t in get_list_tools()]