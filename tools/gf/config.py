def get_config(organization, common_args):
    config = {
        'name': organization+'/gf',
        'version': 'latest',
        'buildargs': {
            'GOLANG_ALPINE_VERSION': common_args['GOLANG_ALPINE_VERSION'],
        },
        'tests': ['-h']
    }
    return config
