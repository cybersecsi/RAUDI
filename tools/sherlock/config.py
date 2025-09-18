import helper

def get_config(organization, common_args):
    api_results = {
        'PIP_VERSION': helper.get_latest_pip_version('sherlock-project'),
    }

    config = {
        'name': organization+'/sherlock',
        'version': helper.clean_version(api_results['PIP_VERSION']),
        'buildargs': {
            'PYTHON3_SLIM_VERSION': common_args['PYTHON3_SLIM_VERSION'],
            'PIP_VERSION': api_results['PIP_VERSION'],
        },
        'tests': ['--help']
    }
    return config