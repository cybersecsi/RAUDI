import helper

def get_config(organization, common_args):
    api_results = {
        'NMAP_GITHUB_INFO': helper.get_latest_github_commit('nmap/nmap'),
    }
    
    config = {
        'name': organization+'/nmap',
        'version': helper.clean_version(api_results['NMAP_GITHUB_INFO']),
        'buildargs': {
            'LATEST_ALPINE_VERSION': common_args['LATEST_ALPINE_VERSION'],
            'NMAP_DOWNLOAD_URL': "https://github.com/nmap/nmap"
        },
        'tests': ['-h']
    }
    return config