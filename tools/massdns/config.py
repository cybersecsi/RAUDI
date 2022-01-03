import helper

def get_config(organization, common_args):
    api_results = {
        'MASSDNS_GITHUB_INFO': helper.get_latest_github_release_no_browser_download('blechschmidt/massdns'),
    }
    
    config = {
        'name': organization+'/massdns',
        'version': api_results['MASSDNS_GITHUB_INFO']['version'][1:], # Remove the leading 'v'
        'buildargs': {
            'LAST_ALPINE_VERSION': common_args['LAST_ALPINE_VERSION'],
            'MASSDNS_DOWNLOAD_URL': api_results['MASSDNS_GITHUB_INFO']['url']
        }
    }
    return config