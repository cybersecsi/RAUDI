import helper


def get_config(organization, common_args):
    api_results = {
        'GITTOLS_GITHUB_INFO': helper.get_latest_github_release_no_browser_download('internetwache/GitTools'),
    }

    config = {
        'name': organization + '/gittools',
        'version': api_results['GITTOLS_GITHUB_INFO']['version'][1:],
        'buildargs': {
            'PYTHON_ALPINE_VERSION': common_args['PYTHON_ALPINE_VERSION'],
            'GITTOLS_DOWNLOAD_URL': api_results['GITTOLS_GITHUB_INFO']['url']
        },
        'tests': []
    }
    return config