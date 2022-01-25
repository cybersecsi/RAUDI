import helper
def get_config(organization, common_args):
    api_results = {
        'APKTOOL_GITHUB_INFO': helper.get_latest_github_release('iBotPeaches/Apktool', target_string='apktool'),
    }
    
    config = {
        'name': organization+'/apktool',
        'version': helper.clean_version(api_results['APKTOOL_GITHUB_INFO']['version']),
        'buildargs': {
            'OPENJDK8_ALPINE_VERSION': common_args['OPENJDK8_ALPINE_VERSION'],
            'APKTOOL_DOWNLOAD_URL': api_results['APKTOOL_GITHUB_INFO']['url']
        },
        'tests': ['--version']
    }
    return config