def get_config(organization, common_args):
    config = {
        'name': organization+'/dirb',
        'version': '2.22',
        'buildargs': {
            'DEBIAN_SLIM_VERSION': common_args['DEBIAN_SLIM_VERSION']
        },
        'tests': []
    }
    return config