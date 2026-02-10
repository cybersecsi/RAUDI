import helper

def get_config(organization, common_args):
    api_results = {
        'PIP_VERSION': helper.get_latest_pip_version('py-altdns'),
    }

    config = {
        'name': organization+'/altdns',
        'version': helper.clean_version(api_results['PIP_VERSION']),
        'buildargs': {
            'PYTHON_ALPINE_VERSION': common_args['PYTHON_LEGACY_ALPINE_VERSION'],
            'PIP_VERSION': api_results['PIP_VERSION'],
        },
        'tests': ['--help']
    }
    return config