import helper

def get_config(organization, common_args):
    api_results = {
        'DVCRIPPER_GITHUB_INFO': helper.get_latest_github_commit('kost/dvcs-ripper'),
    }
    
    config = {
        'name': organization+'/dvcs-ripper',
        'version': api_results['DVCRIPPER_GITHUB_INFO'],
        'buildargs': {
            'DEBIAN_SLIM_VERSION': common_args['DEBIAN_SLIM_VERSION'],
            'DVCRIPPER_DOWNLOAD_URL': "https://github.com/kost/dvcs-ripper"
        },
        'tests': ['rip-git -h']
    }
    return config