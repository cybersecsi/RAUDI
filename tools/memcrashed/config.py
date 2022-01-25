import helper

def get_config(organization, common_args):
    api_results = {
        'GITHUB_INFO': helper.get_latest_github_commit('649/Memcrashed-DDoS-Exploit'),
    }

    config = {
        'name': organization+'/memcrashed',
        'version': helper.clean_version(api_results['GITHUB_INFO']),
        'buildargs': {
            'PYTHON_ALPINE_VERSION': common_args['PYTHON_ALPINE_VERSION'],
            'DOWNLOAD_URL': "https://github.com/649/Memcrashed-DDoS-Exploit.git",
        },
        'tests': []
    }
    return config