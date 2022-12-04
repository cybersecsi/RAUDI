import helper


def get_config(organization, common_args):
    api_results = {
        'DEX2JAR_GITHUB_INFO': helper.get_latest_github_release_no_browser_download('pxb1988/dex2jar'),
    }

    config = {
        'name': organization + '/dex2jar',
        'version': helper.clean_version(api_results['DEX2JAR_GITHUB_INFO']['version']),
        'buildargs': {
            'LATEST_ALPINE_VERSION': common_args['LATEST_ALPINE_VERSION'],
            'DEX2JAR_DOWNLOAD_URL': api_results['DEX2JAR_GITHUB_INFO']['url']
        },
        'tests': ['-h']
    }
    return config