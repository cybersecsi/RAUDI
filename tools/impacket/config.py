import helper
import os

DEFAULT_DIRNAME = os.path.basename(os.path.dirname(__file__))

def get_config(organization, common_args):
    api_results = {
        'GITHUB_INFO': helper.get_latest_github_release_no_browser_download('SecureAuthCorp/impacket'),
    }

    config = {
        'name': organization+'/'+DEFAULT_DIRNAME,
        'version': api_results['GITHUB_INFO']['version'].replace("impacket_", "").replace("_","."), 
        'buildargs': {
            'PYTHON_ALPINE_VERSION': common_args['PYTHON_ALPINE_VERSION'],
            'DOWNLOAD_URL': api_results['GITHUB_INFO']['url'], 
        },
        'tests': []
    }
    return config