import helper

def get_config(organization, common_args):
    api_results = {
        'SECLISTS_GITHUB_INFO': helper.get_latest_github_release_no_browser_download('danielmiessler/SecLists'),
    }
    
    config = {
        'name': organization+'/seclists',
        'version': helper.clean_version(api_results['SECLISTS_GITHUB_INFO']['version']),
        'buildargs': {
            'LATEST_ALPINE_VERSION': common_args['LATEST_ALPINE_VERSION'],
            'SECLISTS_DOWNLOAD_URL': api_results['SECLISTS_GITHUB_INFO']['url']
        },
        'tests': []
    }
    return config