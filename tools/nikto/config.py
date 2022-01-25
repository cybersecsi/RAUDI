import helper

def get_config(organization, common_args):
    api_results = {
        'NIKTO_GITHUB_INFO': helper.get_latest_github_commit('sullo/nikto'),
    }
    
    config = {
        'name': organization+'/nikto',
        'version': helper.clean_version(api_results['NIKTO_GITHUB_INFO']),
        'buildargs': {
            'LATEST_ALPINE_VERSION': common_args['LATEST_ALPINE_VERSION'],
            'NIKTO_DOWNLOAD_URL': "https://github.com/sullo/nikto"
        },
        'tests': []
    }
    return config