from helper import get_latest_docker_hub_version

def get_config():
    return {
        'name': 'secsi/dirb',
        'version': 'latest',
        'buildargs': {
            'LAST_UBUNTU_VERSION': get_latest_docker_hub_version('ubuntu')
        }
    }