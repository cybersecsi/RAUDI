import helper

def get_config(organization, common_args):
    api_results = {
        'GITHUB_INFO': helper.get_latest_github_commit('s0md3v/Striker'),
    }

    config = {
        'name': organization+'/striker',
        'version': api_results['GITHUB_INFO'],
        'buildargs': {
            'PYTHON_ALPINE_VERSION': common_args['PYTHON_ALPINE_VERSION'],
            'DOWNLOAD_URL': "https://github.com/s0md3v/Striker.git",
        },
        'tests': []
    }
    return config