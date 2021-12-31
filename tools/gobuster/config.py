import helper

def get_config(organization, common_args):
    api_results = {
        'GOBUSTER_GITHUB_INFO':  helper.get_latest_github_release('OJ/gobuster', target_string='linux-amd64'),
    }
    
    config = {
        'name': organization+'/gobuster',
        'version': api_results['GOBUSTER_GITHUB_INFO']['version'][1:], # Remove the leading 'v'
        'buildargs': {
            'LAST_UBUNTU_VERSION': common_args['LAST_UBUNTU_VERSION'],
            'GOBUSTER_DOWNLOAD_URL': api_results['GOBUSTER_GITHUB_INFO']['url']
        }
    }
    return config