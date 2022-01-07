import helper

def get_config(organization, common_args):
    api_results = {
        'FIERCE_GITHUB_INFO': helper.get_latest_github_tag_no_browser_download('mschwager/fierce'),
    }
    
    config = {
        'name': organization+'/fierce',
        'version': api_results['FIERCE_GITHUB_INFO']['version'],
        'buildargs': {
            'PYTHON_ALPINE_VERSION': common_args['PYTHON_ALPINE_VERSION'],
            'FIERCE_DOWNLOAD_URL': api_results['FIERCE_GITHUB_INFO']['url']
        },
        'tests': ['-h']
    }
    return config