import helper

def get_config(organization, common_args):
    api_results = {
        'VERSION': helper.get_latest_github_commit('gbrindisi/xsssniper'),
    }
    
    config = {
        'name': organization+'/xsssniper',
        'version': api_results['VERSION'],
        'buildargs': {
            'PYTHON2_ALPINE_VERSION': common_args['PYTHON2_ALPINE_VERSION'],
            'DOWNLOAD_URL': "https://github.com/gbrindisi/xsssniper"
        },
        'tests': ['-h']
    }
    return config