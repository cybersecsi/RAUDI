import helper
import os

DEFAULT_DIRNAME = os.path.basename(os.path.dirname(__file__))

def get_config(organization, common_args):
    api_results = {
        'OXMLXXE_GITHUB_INFO': helper.get_latest_github_commit('BuffaloWill/oxml_xxe'),
    }
    
    config = {
        'name': organization+'/oxml_xxe',
        'version': api_results['OXMLXXE_GITHUB_INFO'],
        'buildargs': {
            'RUBY_ALPINE_VERSION': common_args['RUBY_ALPINE_VERSION'],
            'OXMLXXE_DOWNLOAD_URL': "https://github.com/BuffaloWill/oxml_xxe",
        },
        'tests': []
    }
    return config