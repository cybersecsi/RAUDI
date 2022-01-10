import helper

def get_config(organization, common_args):
    api_results = {
        'GITHUB_INFO': helper.get_latest_github_tag_no_browser_download('vim/vim'),
    }
    
    config = {
        'name': organization+'/vim',
        'version': api_results['GITHUB_INFO']['version'][1:], # Remove the leading 'v'
        'buildargs': {
            'DOWNLOAD_URL': api_results['GITHUB_INFO']['url'],
            'LATEST_ALPINE_VERSION': common_args['LATEST_ALPINE_VERSION'],
        },
        'tests': ['-h']
    }
    return config