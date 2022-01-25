import helper

def get_config(organization, common_args):
    api_results = {
        'VERSION': helper.get_latest_github_commit('epsylon/xsser'),
    }

    config = {
        'name': organization+'/xsser',
        'version': helper.clean_version(api_results['VERSION']),
        'buildargs': {
            'PYTHON_ALPINE_VERSION': common_args['PYTHON_ALPINE_VERSION'],
            'DOWNLOAD_URL': 'https://github.com/epsylon/xsser'
        },
        'tests': ['--help']
    }
    return config