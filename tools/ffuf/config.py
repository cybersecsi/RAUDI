import helper

def get_config(organization, common_args):
    api_results = {
        'FFUF_GITHUB_INFO':  helper.get_latest_github_release('ffuf/ffuf', target_string='linux_amd64'),
    }
    
    config = {
        'name': organization+'/ffuf',
        'version': api_results['FFUF_GITHUB_INFO']['version'][1:], # Remove the leading 'v'
        'buildargs': {
            'LATEST_UBUNTU_VERSION': common_args['LATEST_UBUNTU_VERSION'],
            'FFUF_DOWNLOAD_URL': api_results['FFUF_GITHUB_INFO']['url']
        }
    }
    return config