import helper

def get_config(organization, common_args):
    api_results = {
        'GITHUB_INFO': helper.get_latest_github_tag_no_browser_download('exiftool/exiftool'),
    }
    
    config = {
        'name': organization+'/exiftool',
        'version': helper.clean_version(api_results['GITHUB_INFO']['version']), # USE THE APPROPRIATE FN FROM ABOVE (see README for details)
        'buildargs': {
            'LATEST_ALPINE_VERSION': common_args['LATEST_ALPINE_VERSION'],
            'DOWNLOAD_URL': api_results['GITHUB_INFO']['url'], # USE THE APPROPRIATE FN FROM ABOVE (see README for details)
        },
        'tests': ['-ver']
    }
    return config