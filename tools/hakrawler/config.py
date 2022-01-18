import helper

def get_config(organization, common_args):
    api_results = {
        'GITHUB_INFO': helper.get_latest_github_release_no_browser_download('hakluke/hakrawler')
    }
    
    config = {
        'name': organization+'/hakrawler',
        'version': api_results['GITHUB_INFO']['version'],
        'buildargs': {
            'LATEST_ALPINE_VERSION': common_args['LATEST_ALPINE_VERSION'],
            'GOLANG_ALPINE_VERSION': common_args['GOLANG_ALPINE_VERSION'],
            'DOWNLOAD_URL': api_results['GITHUB_INFO']['url']
        },
        'tests': ['-h']
    }
    return config