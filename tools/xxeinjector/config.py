import helper
import os

DEFAULT_DIRNAME = os.path.basename(os.path.dirname(__file__))

def get_config(organization, common_args):
    api_results = {
        'XXEINJECTOR_GITHUB_INFO': helper.get_latest_github_commit('enjoiz/XXEinjector'),
    }
    
    config = {
        'name': organization+'/xxeinjector',
        'version': helper.clean_version(api_results['XXEINJECTOR_GITHUB_INFO']),
        'buildargs': {
            'RUBY_ALPINE_VERSION': common_args['RUBY_ALPINE_VERSION'],
            'DOWNLOAD_URL': "https://github.com/enjoiz/XXEinjector",
        },
        'tests': []
    }
    return config