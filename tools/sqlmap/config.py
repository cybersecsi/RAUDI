import helper

def get_config(organization, common_args):
    api_results = {
        'SQLMAP_GITHUB_INFO': helper.get_latest_github_release_no_browser_download('sqlmapproject/sqlmap'),
    }
    
    config = {
        'name': organization+'/sqlmap',
        'version': helper.clean_version(api_results['SQLMAP_GITHUB_INFO']['version']),
        'buildargs': {
            'PYTHON_ALPINE_VERSION': common_args['PYTHON_ALPINE_VERSION'],
            'SQLMAP_DOWNLOAD_URL': api_results['SQLMAP_GITHUB_INFO']['url']
        },
        'tests': ['--help']
    }
    return config