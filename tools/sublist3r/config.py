import helper

def get_config(organization, common_args):
    api_results = {
        'SUBLIST3R_GITHUB_INFO': helper.get_latest_github_release_no_browser_download('aboul3la/Sublist3r'),
    }
    
    config = {
        'name': organization+'/sublist3r',
        'version': api_results['SUBLIST3R_GITHUB_INFO']['version'],
        'buildargs': {
            'PYTHON_ALPINE_VERSION': common_args['PYTHON_ALPINE_VERSION'],
            'SUBLIST3R_DOWNLOAD_URL': api_results['SUBLIST3R_GITHUB_INFO']['url']
        }
    }
    return config