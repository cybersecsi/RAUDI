import helper

def get_config(organization, common_args):
    api_results = {
        'DNSCAN_GITHUB_INFO': helper.get_latest_github_commit('rbsec/dnscan'),
    }
    
    config = {
        'name': organization+'/dnscan',
        'version': helper.clean_version(api_results['DNSCAN_GITHUB_INFO']),
        'buildargs': {
            'PYTHON_ALPINE_VERSION': common_args['PYTHON_ALPINE_VERSION'],
            'DNSCAN_DOWNLOAD_URL': "https://github.com/rbsec/dnscan"
        },
        'tests': ['-h']
    }
    return config