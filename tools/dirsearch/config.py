import helper

def get_config(organization, common_args):
    api_results = {
        'DIRSEARCH_GITHUB_INFO': helper.get_latest_github_release_no_browser_download('maurosoria/dirsearch'),
    }
    
    config = {
        'name': organization+'/dirsearch',
        'version': helper.clean_version(api_results['DIRSEARCH_GITHUB_INFO']['version']),
        'buildargs': {
            'PYTHON_ALPINE_VERSION': common_args['PYTHON_ALPINE_VERSION'],
            'DIRSEARCH_DOWNLOAD_URL': api_results['DIRSEARCH_GITHUB_INFO']['url']
        },
        'tests': ['--help']
    }
    return config