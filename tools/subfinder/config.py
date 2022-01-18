import helper

def get_config(organization, common_args):
    api_results = {
        'SUBFINDER_GITHUB_INFO': helper.get_latest_github_release('projectdiscovery/subfinder', target_string='linux_amd64' )
    }
    
    config = {
        'name': organization+'/subfinder',
        'version': api_results['SUBFINDER_GITHUB_INFO']['version'][1:],
        'buildargs': {
            'LATEST_ALPINE_VERSION': common_args['LATEST_ALPINE_VERSION'],
            'DOWNLOAD_URL': api_results['SUBFINDER_GITHUB_INFO']['url']
        },
        'tests': ['-h']
    }
    return config