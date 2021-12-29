from helper import get_latest_pip_version

def get_config():
    return {
        'name': 'secsi/dirhunt',
        'version': get_latest_pip_version('dirhunt'),
        'buildargs': {
            'DIRHUNT_VERSION': get_latest_pip_version('dirhunt')
        }
    }   
