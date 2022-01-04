import helper

def get_config(organization, common_args):
    api_results = {
        'APKTOOL_GITHUB_INFO': helper.get_latest_github_release('iBotPeaches/Apktool', target_string='apktool'),
    }
    
    config = {
        'name': organization+'/apktool',
        'version': api_results['APKTOOL_GITHUB_INFO']['version'][1:], # Remove the leading 'v'
        'buildargs': {
            'OPENJDK_ALPINE_VERSION': common_args['OPENJDK_ALPINE_VERSION'],
            'APKTOOL_DOWNLOAD_URL': api_results['APKTOOL_GITHUB_INFO']['url']
        },
        'tests': ['--version']
    }
    return config