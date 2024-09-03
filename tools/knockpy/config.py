import helper


def get_config(organization, common_args):
    api_results = {
        'KNOCKPY_GITHUB_INFO': helper.get_latest_github_release_no_browser_download('guelfoweb/knock'),
    }

    config = {
        'name': organization+'/knockpy',
        'version': helper.clean_version(api_results['KNOCKPY_GITHUB_INFO']['version']),
        'buildargs': {
            'KNOCKPY_DOWNLOAD_URL': api_results['KNOCKPY_GITHUB_INFO']['url']
        },
        'tests': []
    }
    return config
