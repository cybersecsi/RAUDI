import helper

def get_config(organization, common_args):
    api_results = {
        'RACETHEWEB_GITHUB_INFO': helper.get_latest_github_release('TheHackerDev/race-the-web', target_string="lin64"),
    }
    
    config = {
        'name': organization+'/race-the-web',
        'version': api_results['RACETHEWEB_GITHUB_INFO']['version'],
        'buildargs': {
            'LATEST_ALPINE_VERSION': common_args['LATEST_ALPINE_VERSION'],
            'RACETHEWEB_DOWNLOAD_URL': api_results['RACETHEWEB_GITHUB_INFO']['url']
        }
    }
    return config