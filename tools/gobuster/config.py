from helper import get_latest_docker_hub_version, get_latest_github_release

def get_config():
    return {
        'name': 'secsi/gobuster',
        'version': get_latest_github_release('OJ/gobuster', target_string='linux-amd64')['version'][1:], # Remove the leading 'v',
        'buildargs': {
            'LAST_UBUNTU_VERSION': get_latest_docker_hub_version('ubuntu'),
            'GOBUSTER_DOWNLOAD_URL': get_latest_github_release('OJ/gobuster', target_string='linux-amd64')['url']
        }
    }