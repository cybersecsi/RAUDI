import helper

def get_config(organization, common_args):
    api_results = {
        'RETIRE_NPM_VERSION': helper.get_latest_npm_registry_version('retire'),
    }
    
    config = {
        'name': organization+'/retire',
        'version': api_results['RETIRE_NPM_VERSION'],
        'buildargs': {
            'NODE_ALPINE_VERSION': common_args['NODE_ALPINE_VERSION'],
            'RETIRE_NPM_VERSION': api_results['RETIRE_NPM_VERSION']
        }
    }
    return config