import helper


def get_config(organization, common_args):
    api_results = {
        'DATASPLOIT_GITHUB_INFO': helper.get_latest_github_commit('dvopsway/datasploit'),
    }

    config = {
        'name': organization + '/datasploit',
        'version': helper.clean_version(api_results['DATASPLOIT_GITHUB_INFO']),
        'buildargs': {
            'PYTHON2_ALPINE_VERSION': common_args['PYTHON2_ALPINE_VERSION'],
            'DATASPLOIT_DOWNLOAD_URL':  "https://github.com/dvopsway/datasploit"
        },
        'tests': ['-h']
    }
    return config