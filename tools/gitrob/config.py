import helper

def get_config(organization, common_args):
    api_results = {
        'GITROB_GITHUB_INFO': {
            #Static values since it is archived and without 'latest' tag
            'version': '2.0.0-beta',
            'url': 'https://github.com/michenriksen/gitrob/releases/download/v2.0.0-beta/gitrob_linux_amd64_2.0.0-beta.zip' 
        }
    }
    
    config = {
        'name': organization+'/gitrob',
        'version': api_results['GITROB_GITHUB_INFO']['version'],
        'buildargs': {
            'LAST_ALPINE_VERSION': common_args['LAST_ALPINE_VERSION'],
            'GITROB_DOWNLOAD_URL': api_results['GITROB_GITHUB_INFO']['url']
        }
    }
    return config