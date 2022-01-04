import helper

def get_config(organization, common_args):
    api_results = {
        'JWT_TOOL_GITHUB_INFO': helper.get_latest_github_release_no_browser_download('ticarpi/jwt_tool'),
    }
    
    config = {
        'name': organization+'/jwt_tool',
        'version': api_results['JWT_TOOL_GITHUB_INFO']['version'][1:], # Remove the leading 'v'
        'buildargs': {
            'PYTHON_ALPINE_VERSION': common_args['PYTHON_ALPINE_VERSION'],
            'JWT_TOOL_DOWNLOAD_URL': api_results['JWT_TOOL_GITHUB_INFO']['url']
        },
        'tests': ['--help']
    }
    return config