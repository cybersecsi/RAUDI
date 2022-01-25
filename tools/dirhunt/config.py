import helper

def get_config(organization, common_args):
    api_results = {
        'DIRHUNT_PIP_VERSION': helper.get_latest_pip_version('dirhunt'),
    }
    
    config = {
        'name': organization+'/dirhunt',
        'version': helper.clean_version(api_results['DIRHUNT_PIP_VERSION']),
        'buildargs': {
            'PYTHON_ALPINE_VERSION': common_args['PYTHON_ALPINE_VERSION'],
            'DIRHUNT_VERSION': api_results['DIRHUNT_PIP_VERSION']
        },
        'tests': ['--help']
    }
    return config