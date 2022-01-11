import helper

def get_config(organization, common_args):
    api_results = {
        'GOOGD0RKER_GITHUB_INFO': helper.get_latest_github_commit('ZephrFish/GoogD0rker'),
    }
    
    config = {
        'name': organization+'/googd0rker',
        'version': api_results['GOOGD0RKER_GITHUB_INFO'],
        'buildargs': {
            'PYTHON_ALPINE_VERSION': common_args['PYTHON_ALPINE_VERSION'],
            'GOOGD0RKER_DOWNLOAD_URL': "https://github.com/ZephrFish/GoogD0rker"
        },
        'tests': ['-h']
    }
    return config