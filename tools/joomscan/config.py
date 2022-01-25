import helper
import os

def get_config(organization, common_args):
    api_results = {
        'GITHUB_INFO': helper.get_latest_github_release_no_browser_download('OWASP/joomscan'),
    }

    config = {
        'name': organization+'/joomscan',
        'version': helper.clean_version(api_results['GITHUB_INFO']['version']),
        'buildargs': {
            'LATEST_ALPINE_VERSION': common_args['LATEST_ALPINE_VERSION'],
            'JOOMSCAN_DOWNLOAD_URL': api_results['GITHUB_INFO']['url'],
        },
        'tests': ['--version']
    }
    return config