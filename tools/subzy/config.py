import helper

def get_config(organization, common_args):
    api_results = {
        'GITHUB_INFO': helper.get_latest_github_tag_no_browser_download('PentestPad/subzy')
    }

    config = {
        'name': organization+'/subzy',
        'version': helper.clean_version(api_results['GITHUB_INFO']['version']),
        'buildargs': {
            'GOLANG_ALPINE_VERSION': common_args['GOLANG_ALPINE_VERSION'],
            'LATEST_ALPINE_VERSION': common_args['LATEST_ALPINE_VERSION'],
            'DOWNLOAD_URL': api_results['GITHUB_INFO']['url']
        },
        'tests': ['--help']
    }
    return config
    