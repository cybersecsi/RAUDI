import helper

def get_config(organization, common_args):
    api_results = {
        'GITHUB_INFO': helper.get_latest_github_release('hahwul/dalfox', 'linux_amd64'),
    }
    
    config = {
        'name': organization+'/dalfox',
        'version': helper.clean_version(api_results['GITHUB_INFO']['version']),
        'buildargs': {
            'GOLANG_ALPINE_VERSION': common_args['GOLANG_ALPINE_VERSION'],
        },
        'tests': ['-h']
    }
    return config