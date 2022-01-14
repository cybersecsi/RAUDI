import helper

def get_config(organization, common_args):
    api_results = {
        'GITHUB_INFO': helper.get_latest_github_tag_no_browser_download('psalm/phar'),
    }
    
    config = {
        'name': organization+'/psalm',
        'version': api_results['GITHUB_INFO']['version'],
        'buildargs': {
            'PHP_ALPINE_VERSION': common_args['PHP_ALPINE_VERSION'],
            'DOWNLOAD_URL': api_results['GITHUB_INFO']['url'],
        },
        'tests': ['-h']
    }
    return config