import helper
import os

DEFAULT_DIRNAME = os.path.basename(os.path.dirname(__file__))

def get_config(organization, common_args):
    api_results = {
        # See the README for a detailed documentation of those helpers
        #'GITHUB_INFO': helper.get_latest_github_release('<repo_name>', '<target_string>'),
        #'GITHUB_INFO': helper.get_latest_github_release_no_browser_download('<repo_name>'),
        #'GITHUB_INFO': helper.get_latest_github_tag_no_browser_download('<repo_name>'),
    }
    
    config = {
        'name': organization+'/'+DEFAULT_DIRNAME,
        # 'version': api_results['GITHUB_INFO']['version'], # USE THE APPROPRIATE FN FROM ABOVE (see README for details)
        'buildargs': {
            'GOLANG_ALPINE_VERSION': common_args['GOLANG_ALPINE_VERSION'],
            'LATEST_ALPINE_VERSION': common_args['LATEST_ALPINE_VERSION'],
            #'DOWNLOAD_URL': api_results['GITHUB_INFO']['url'], # USE THE APPROPRIATE FN FROM ABOVE (see README for details)

        },
        'tests': []
    }
    return config