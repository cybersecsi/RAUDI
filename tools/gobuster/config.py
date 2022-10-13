import helper

def get_config(organization, common_args):
    api_results = {
        'GOBUSTER_GITHUB_INFO':  helper.get_latest_github_release('OJ/gobuster', target_string='Linux_x86_64'),
    }
    
    config = {
        'name': organization+'/gobuster',
        'version': helper.clean_version(api_results['GOBUSTER_GITHUB_INFO']['version']),
        'buildargs': {
            'GOLANG_ALPINE_VERSION': common_args['GOLANG_ALPINE_VERSION'],
        },
        'tests': ['-h']
    }
    return config