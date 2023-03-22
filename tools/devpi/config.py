import helper


def get_config(organization, common_args):
    api_results = {
        'GITHUB_INFO': helper.get_latest_github_commit('devpi/devpi'),
    }

    config = {
        'name': organization+'/devpi',
        'version': helper.clean_version(api_results['GITHUB_INFO']),
        'buildargs': {
            'PYTHON_ALPINE_VERSION': common_args['PYTHON_ALPINE_VERSION'],
            'DOWNLOAD_URL': "https://github.com/devpi/devpi.git",
        },
        'tests': []
    }
    return config
