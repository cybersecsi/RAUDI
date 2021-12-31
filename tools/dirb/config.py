def get_config(organization, common_args):
    config = {
        'name': organization+'/dirb',
        'version': '2.22',
        'buildargs': {
            'LAST_UBUNTU_VERSION': common_args['LAST_UBUNTU_VERSION']
        }
    }
    return config