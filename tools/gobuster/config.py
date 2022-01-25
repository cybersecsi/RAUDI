import helper

def get_config(organization, common_args):
    api_results = {
        'GOBUSTER_GITHUB_INFO':  helper.get_latest_github_release('OJ/gobuster', target_string='linux-amd64'),
    }
    
    config = {
        'name': organization+'/gobuster',
        'version': helper.clean_version(api_results['GOBUSTER_GITHUB_INFO']['version']),
        'buildargs': {
            'LATEST_ALPINE_VERSION': common_args['LATEST_ALPINE_VERSION'],
            'GOBUSTER_DOWNLOAD_URL': api_results['GOBUSTER_GITHUB_INFO']['url']
        },
        'tests': ['--help']
    }
    return config