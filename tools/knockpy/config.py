import helper

def get_config(organization, common_args):
    api_results = {
        'KNOCKPY_GITHUB_INFO': helper.get_latest_github_release_no_browser_download('guelfoweb/knock'),
    }
    
    config = {
        'name': organization+'/knockpy',
        'version': api_results['KNOCKPY_GITHUB_INFO']['version'],
        'buildargs': {
            'PYTHON_ALPINE_VERSION': common_args['PYTHON_ALPINE_VERSION'],
            'KNOCKPY_DOWNLOAD_URL': api_results['KNOCKPY_GITHUB_INFO']['url']
        }
    }
    return config