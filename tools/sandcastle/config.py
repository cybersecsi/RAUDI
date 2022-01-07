import helper

def get_config(organization, common_args):
    api_results = {
        'SANDCASTLE_GITHUB_INFO': helper.get_latest_github_tag_no_browser_download('0xSearches/sandcastle'),
    }
    
    config = {
        'name': organization+'/sandcastle',
        'version': api_results['SANDCASTLE_GITHUB_INFO']['version'],
        'buildargs': {
            'PYTHON2_ALPINE_VERSION': common_args['PYTHON2_ALPINE_VERSION'],
            'SANDCASTLE_DOWNLOAD_URL': api_results['SANDCASTLE_GITHUB_INFO']['url']
        },
        'tests': ['-h']
    }
    return config