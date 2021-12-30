import requests
import re
import docker
import os
import shutil

# Global vars
DOCKER_API = {
    'base': "https://hub.docker.com/v2/repositories/",
    'tags': "/tags?page=1&page_size=50"
}
PYPI_API = {
    'base': "https://pypi.org/pypi/",
    'json': "/json"
}
GITHUB_API = {
    'base': "https://api.github.com/repos/",
    'latest_release': "/releases/latest"
}

def get_highest_version_number(version_numbers):
    version_numbers.sort(key=lambda s: list(map(int, s.split('.'))))
    return version_numbers[-1]

def get_latest_docker_hub_version(docker_image, org="library/"):
    r = requests.get(DOCKER_API['base']+org+docker_image+DOCKER_API['tags'])
    results = r.json()['results']
    regex = '^\d+(\.\d+)*$' # Only digits and dots
    tags_with_version_number = [result["name"] for result in results if re.match(regex, result["name"])]
    if len(tags_with_version_number) > 0:
        return get_highest_version_number(tags_with_version_number)
    else:
        return 'latest'

def get_latest_pip_version(package):
    r = requests.get(PYPI_API['base']+package+PYPI_API['json'])
    version = r.json()['info']['version']
    return version

def get_latest_github_release(repo, target_string):
    r = requests.get(GITHUB_API['base']+repo+GITHUB_API['latest_release'])
    assets = r.json()['assets']
    for asset in assets:
        if target_string in asset['name']:
            return {
                'url': asset['browser_download_url'],
                'version': r.json()['tag_name']
            }

def get_latest_github_release_no_browser_download(repo):
    r = requests.get(GITHUB_API['base']+repo+GITHUB_API['latest_release'])
    data = r.json()
    return {
        'url': data['tarball_url'],
        'version': data['tag_name']
    }

def check_if_docker_image_exists(docker_image):
    client = docker.from_env()
    try:
        res = client.images.get(docker_image)
        return res
    except docker.errors.ImageNotFound:
        return None