def get_config(organization, common_args):
    config = {
        'name': organization+'/dirb',
        'version': '2.22',
        'buildargs': {
            'LATEST_UBUNTU_VERSION': common_args['LATEST_UBUNTU_VERSION']
        }
    }
    return config