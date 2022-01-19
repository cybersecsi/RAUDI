import helper

def get_config(organization, common_args):
    api_results = {
        'GITHUB_INFO': helper.get_latest_github_release_no_browser_download('EnableSecurity/wafw00f'),
    }

    config = {
        'name': organization+'/wafw00f',
        'version': api_results['GITHUB_INFO']['version'][1:], # Remove the leading 'v'
        'buildargs': {
            'PYTHON_ALPINE_VERSION': common_args['PYTHON_ALPINE_VERSION'],
            'DOWNLOAD_URL': api_results['GITHUB_INFO']['url']
        },
        'tests': ['--help']
    }
    return config