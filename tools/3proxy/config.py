import helper
import os

DEFAULT_DIRNAME = os.path.basename(os.path.dirname(__file__))

def get_config(organization, common_args):
    api_results = {
        'GITHUB_INFO': helper.get_latest_github_release_no_browser_download('3proxy/3proxy'),
    }

    config = {
        'name': organization+'/'+DEFAULT_DIRNAME,
        'version' : helper.clean_version(api_results['GITHUB_INFO']['version']),
        'buildargs': {
            'LATEST_GCC_VERSION': common_args['LATEST_GCC_VERSION'],
            'LATEST_BUSYBOX_GLIBC_VERSION': common_args['LATEST_BUSYBOX_GLIBC_VERSION'],
            'DOWNLOAD_URL': api_results['GITHUB_INFO']['url'],
        },
        'tests': []
    }
    return config