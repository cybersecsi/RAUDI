import helper

def get_config(organization, common_args):
    api_results = {
        'GITHUB_INFO': helper.get_latest_github_commit('rbsec/sslscan'),
    }
    
    config = {
        'name': organization+'/sslscan',
        'version': helper.clean_version(api_results['GITHUB_INFO']),
        'buildargs': {
            'LATEST_ALPINE_VERSION': common_args['LATEST_ALPINE_VERSION'],
            'DOWNLOAD_URL': "https://github.com/rbsec/sslscan"
        },
        'tests': ['--help']
    }
    return config