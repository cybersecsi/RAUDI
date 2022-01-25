import helper

def get_config(organization, common_args):
    api_results = {
        'WHATWEB_GITHUB_INFO': helper.get_latest_github_release_no_browser_download('urbanadventurer/WhatWeb'),
    }

    config = {
        'name': organization+'/whatweb',
        'version': helper.clean_version(api_results['WHATWEB_GITHUB_INFO']['version']),
        'buildargs': {
            'RUBY_ALPINE_VERSION': common_args['RUBY_ALPINE_VERSION'],
            'WHATWEB_DOWNLOAD_URL': api_results['WHATWEB_GITHUB_INFO']['url']
        },
        'tests': ['--help']
    }
    return config