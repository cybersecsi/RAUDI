import helper


def get_config(organization, common_args):
    api_results = {
        'EYEWITNESS_GITHUB_INFO': helper.get_latest_github_release_no_browser_download('FortyNorthSecurity/EyeWitness'),
    }

    config = {
        'name': organization + '/eyewitness',
        'version': api_results['EYEWITNESS_GITHUB_INFO']['version'][1:],
        'buildargs': {
            'PYTHON_ALPINE_VERSION': common_args['PYTHON_ALPINE_VERSION'],
            'EYEWITNESS_DOWNLOAD_URL': api_results['EYEWITNESS_GITHUB_INFO']['url']
        },
        'tests': ['-h']
    }
    return config