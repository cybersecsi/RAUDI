import helper
import os

DEFAULT_DIRNAME = os.path.basename(os.path.dirname(__file__))

def get_config(organization, common_args):
    api_results = {
        # See the README for a detailed documentation of those helpers
        #'NPM_VERSION': helper.get_latest_npm_registry_version('<package_name>'),
    }
    
    config = {
        'name': organization+'/'+DEFAULT_DIRNAME,
        # 'version': api_results['NPM_VERSION'], # USE THE APPROPRIATE FN FROM ABOVE (see README for details)
        'buildargs': {
            'NODE_ALPINE_VERSION': common_args['NODE_ALPINE_VERSION'],
            #'NPM_VERSION': api_results['RETIRE_NPM_VERSION'], # USE THE APPROPRIATE FN FROM ABOVE (see README for details)
        },
        'tests': []
    }
    return config