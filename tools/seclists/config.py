import helper
import os

DEFAULT_DIRNAME = os.path.basename(os.path.dirname(__file__))

def get_config(organization, common_args):
    api_results = {
        'GITHUB_INFO': helper.get_latest_github_commit('danielmiessler/SecLists'),
    }
    
    config = {
        'name': organization+'/'+DEFAULT_DIRNAME,
        'version': helper.clean_version(api_results['GITHUB_INFO']),
        'buildargs': {
            'LATEST_ALPINE_VERSION': common_args['LATEST_ALPINE_VERSION'],
            'DOWNLOAD_URL': 'https://github.com/danielmiessler/SecLists'
        },
        'tests': []
    }
    return config