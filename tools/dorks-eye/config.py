import helper

def get_config(organization, common_args):
    api_results = {
        'GITHUB_COMMIT_DATE': helper.get_latest_github_commit('BullsEye0/dorks-eye'),
    }
    
    config = {
        'name': organization+'/dorks-eye',
        'version': api_results['GITHUB_COMMIT_DATE'],
        'buildargs': {
            'PYTHON_ALPINE_VERSION': common_args['PYTHON_ALPINE_VERSION'],
            'DOWNLOAD_URL': "https://github.com/BullsEye0/dorks-eye"
        },
        'tests': []
    }
    return config