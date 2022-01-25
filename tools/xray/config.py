import helper

def get_config(organization, common_args):
    api_results = {
        'GITHUB_INFO': helper.get_latest_github_commit('evilsocket/xray'),
    }
    
    config = {
        'name': organization+'/xray',
        'version': helper.clean_version(api_results['GITHUB_INFO']),
        'buildargs': {
            'GOLANG_ALPINE_VERSION': common_args['GOLANG_ALPINE_VERSION'],
            'LATEST_ALPINE_VERSION': common_args['LATEST_ALPINE_VERSION'],
            'DOWNLOAD_URL': "https://github.com/evilsocket/xray.git",
        },
        'tests': ["--help"]
    }
    return config