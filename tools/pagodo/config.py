import helper

def get_config(organization, common_args):
    api_results = {
        'GITHUB_INFO': helper.get_latest_github_release_no_browser_download('opsdisk/pagodo'),
    }

    config = {
        'name': organization+'/pagodo',
        'version': helper.clean_version(api_results['GITHUB_INFO']['version']),
        'buildargs': {
            'PYTHON_ALPINE_VERSION': common_args['PYTHON_ALPINE_VERSION'],
            'DOWNLOAD_URL': api_results['GITHUB_INFO']['url'],
        },
        'tests': []
    }
    return config