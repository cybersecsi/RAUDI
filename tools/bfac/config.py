import helper

def get_config(organization, common_args):
    api_results = {
        'BFAC_GITHUB_INFO': helper.get_latest_github_release_no_browser_download('mazen160/bfac'),
    }

    config = {
        'name': organization+'/bfac',
        'version': api_results['BFAC_GITHUB_INFO']['version'][1:], # Remove the leading 'v'
        'buildargs': {
            'PYTHON_ALPINE_VERSION': common_args['PYTHON_ALPINE_VERSION'],
            'BFAC_DOWNLOAD_URL': api_results['BFAC_GITHUB_INFO']['url']
        },
        'tests': ['--help']
    }
    return config