import helper

def get_config(organization, common_args):
    api_results = {
        'LFISUITE_GITHUB_INFO': helper.get_latest_github_release_no_browser_download('D35m0nd142/LFISuite'),
    }
    
    config = {
        'name': organization+'/lfisuite',
        'version': api_results['LFISUITE_GITHUB_INFO']['version'][1:], # Remove the leading 'v'
        'buildargs': {
            'PYTHON2_ALPINE_VERSION': common_args['PYTHON2_ALPINE_VERSION'],
            'LFISUITE_DOWNLOAD_URL': api_results['LFISUITE_GITHUB_INFO']['url']
        }
    }
    return config