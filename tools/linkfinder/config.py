import helper

def get_config(organization, common_args):
    api_results = {
        'GITHUB_INFO': helper.get_latest_github_commit('GerbenJavado/LinkFinder'),
    }

    config = {
        'name': organization+'/linkfinder',
        'version': api_results['GITHUB_INFO'],
        'buildargs': {
            'PYTHON_ALPINE_VERSION': common_args['PYTHON_ALPINE_VERSION'],
            'DOWNLOAD_URL': "https://github.com/GerbenJavado/LinkFinder.git",
        },
        'tests': ['--help']
    }
    return config