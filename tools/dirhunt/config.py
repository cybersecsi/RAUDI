import helper

def get_config(organization, common_args):
    api_results = {
        'DIRHUNT_PIP_VERSION': helper.get_latest_pip_version('dirhunt'),
    }
    
    config = {
        'name': organization+'/dirhunt',
        'version': api_results['DIRHUNT_PIP_VERSION'],
        'buildargs': {
            'DIRHUNT_VERSION': api_results['DIRHUNT_PIP_VERSION']
        }
    }
    return config