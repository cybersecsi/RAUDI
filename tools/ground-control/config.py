import helper
import os

DEFAULT_DIRNAME = os.path.basename(os.path.dirname(__file__))

def get_config(organization, common_args):
    api_results = {
        'GROUNDCONTROL_GITHUB_INFO': helper.get_latest_github_commit('jobertabma/ground-control'),
    }
    
    config = {
        'name': organization+'/ground-control',
        'version': helper.clean_version(api_results['GROUNDCONTROL_GITHUB_INFO']),
        'buildargs': {
            'RUBY2_ALPINE_VERSION': common_args['RUBY2_ALPINE_VERSION'],
            'DOWNLOAD_URL': "https://github.com/jobertabma/ground-control",
        },
        'tests': []
    }
    return config