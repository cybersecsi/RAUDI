import helper

def get_config(organization, common_args):
    api_results = {
        'WAYBACKPY_PIP_VERSION': helper.get_latest_pip_version('waybackpy'),
    }
    
    config = {
        'name': organization+'/waybackpy',
        'version': api_results['WAYBACKPY_PIP_VERSION'],
        'buildargs': {
            'PYTHON_ALPINE_VERSION': common_args['PYTHON_ALPINE_VERSION'],
            'WAYBACKPY_PIP_VERSION': api_results['WAYBACKPY_PIP_VERSION']
        }
    }
    return config