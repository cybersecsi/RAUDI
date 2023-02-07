import helper

def get_config(organization, common_args):
    api_results = {
        'GITHUB_INFO': helper.get_latest_github_commit('sherlock-project/sherlock'),
    }
    
    config = {
        'name': organization+'/sherlock',
        'version': helper.clean_version(api_results['GITHUB_INFO']),
        'buildargs': {
            'DOWNLOAD_URL': "https://github.com/sherlock-project/sherlock"
        },
        'tests': ['--help']
    }
    return config