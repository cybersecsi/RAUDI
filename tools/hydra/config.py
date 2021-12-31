import helper

def get_config(organization, common_args):
    api_results = {
        'HYDRA_GITHUB_INFO': helper.get_latest_github_release_no_browser_download('vanhauser-thc/thc-hydra'),
    }
    
    config = {
        'name': organization+'/hydra',
        'version': api_results['HYDRA_GITHUB_INFO']['version'][1:], # Remove the leading 'v',
        'buildargs': {
            'LAST_UBUNTU_VERSION': common_args['LAST_UBUNTU_VERSION'],
            'HYDRA_DOWNLOAD_URL': api_results['HYDRA_GITHUB_INFO']['url']
        }
    }
    return config