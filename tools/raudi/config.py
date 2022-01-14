def get_config(organization, common_args):    
    config = {
        'name': organization+'/raudi',
        'version': '1.0',
        'buildargs': {
            'LATEST_ALPINE_VERSION': common_args['LATEST_ALPINE_VERSION'],
        },
        'tests': []
    }
    return config