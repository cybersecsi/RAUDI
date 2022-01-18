import helper
import os

def get_config(organization, common_args):
    api_results = {
        'GITHUB_INFO': helper.get_latest_github_release_no_browser_download('Tuhinshubhra/CMSeeK'),
    }

    config = {
        'name': organization+'/cmseek',
        'version': api_results['GITHUB_INFO']['version'][2:], # Remove the leading 'v.'
        'buildargs': {
            'PYTHON_ALPINE_VERSION': common_args['PYTHON_ALPINE_VERSION'],
            'CMSEEK_DOWNLOAD_URL': api_results['GITHUB_INFO']['url'],
        },
        'tests': ['-h']
    }
    return config