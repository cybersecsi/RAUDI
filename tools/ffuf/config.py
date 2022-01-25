import helper

def get_config(organization, common_args):
    api_results = {
        'FFUF_GITHUB_INFO':  helper.get_latest_github_release('ffuf/ffuf', target_string='linux_amd64'),
    }
    
    config = {
        'name': organization+'/ffuf',
        'version': helper.clean_version(api_results['FFUF_GITHUB_INFO']['version']),
        'buildargs': {
            'LATEST_ALPINE_VERSION': common_args['LATEST_ALPINE_VERSION'],
            'FFUF_DOWNLOAD_URL': api_results['FFUF_GITHUB_INFO']['url']
        },
        'tests': ['-V']
    }
    return config