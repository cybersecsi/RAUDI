import helper
import os

DEFAULT_DIRNAME = os.path.basename(os.path.dirname(__file__))

def get_config(organization, common_args):
    api_results = {
        # See the README for a detailed documentation of those helpers
        #'GITHUB_INFO': helper.get_latest_github_release('<repo_name>', '<target_string>'),
        'GITHUB_INFO': helper.get_latest_github_release_no_browser_download('3proxy/3proxy'),
        #'GITHUB_INFO': helper.get_latest_github_tag_no_browser_download('<repo_name>'),
    }
    print(api_results['GITHUB_INFO']['url'])
    config = {
        'name': organization+'/'+DEFAULT_DIRNAME,
        'version' : api_results['GITHUB_INFO']['version'],
        'buildargs': {
            'DEBIAN_SLIM_VERSION': common_args['DEBIAN_SLIM_VERSION'],
            'DOWNLOAD_URL': helper.get_deb_from_github('3proxy', '3proxy', api_results['GITHUB_INFO']['version'])
            # 'DOWNLOAD_URL': api_results['GITHUB_INFO']['url'],
        },
        'tests': ['--help']
    }
    return config