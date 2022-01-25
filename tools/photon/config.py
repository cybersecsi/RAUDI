import helper

def get_config(organization, common_args):
    api_results = {
        'GITHUB_INFO': helper.get_latest_github_tag_no_browser_download('s0md3v/Photon'),
    }

    config = {
        'name': organization+'/photon',
        'version': helper.clean_version(api_results['GITHUB_INFO']['version']),
        'buildargs': {
            'PYTHON_ALPINE_VERSION': common_args['PYTHON_ALPINE_VERSION'],
            'DOWNLOAD_URL': api_results['GITHUB_INFO']['url'],
        },
        'tests': ['--help']
    }
    return config