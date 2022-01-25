import helper
import os

DEFAULT_DIRNAME = os.path.basename(os.path.dirname(__file__))

def get_config(organization, common_args):
    api_results = {
        'GITHUB_INFO': helper.get_latest_github_tag_no_browser_download('rivermont/spidy'),
    }

    config = {
        'name': organization+'/'+DEFAULT_DIRNAME,
        'version': api_results['GITHUB_INFO']['version'][:], # USE THE APPROPRIATE FN FROM ABOVE (see README for details)
        'buildargs': {
            'PYTHON_ALPINE_VERSION': common_args['PYTHON_ALPINE_VERSION'],
            'DOWNLOAD_URL' : api_results['GITHUB_INFO']['url']
        },
        'tests': []
    }
    return config