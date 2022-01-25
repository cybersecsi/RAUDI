import helper

def get_config(organization, common_args):
    api_results = {
        'MASSDNS_GITHUB_INFO': helper.get_latest_github_release_no_browser_download('blechschmidt/massdns'),
    }
    
    config = {
        'name': organization+'/massdns',
        'version': helper.clean_version(api_results['MASSDNS_GITHUB_INFO']['version']),
        'buildargs': {
            'LATEST_ALPINE_VERSION': common_args['LATEST_ALPINE_VERSION'],
            'MASSDNS_DOWNLOAD_URL': api_results['MASSDNS_GITHUB_INFO']['url']
        },
        'tests': ['--help']
    }
    return config