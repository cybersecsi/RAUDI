import helper

def get_config(organization, common_args):
    api_results = {
        'MASSCAN_GITHUB_INFO': helper.get_latest_github_release_no_browser_download('robertdavidgraham/masscan'),
    }
    
    config = {
        'name': organization+'/masscan',
        'version': api_results['MASSCAN_GITHUB_INFO']['version'],
        'buildargs': {
            'LATEST_ALPINE_VERSION': common_args['LATEST_ALPINE_VERSION'],
            'MASSCAN_DOWNLOAD_URL': api_results['MASSCAN_GITHUB_INFO']['url']
        },
        'tests': [] # Seems to always return a status code 1
    }
    return config