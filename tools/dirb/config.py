def get_config(organization, common_args):
    config = {
        'name': organization+'/dirb',
        'version': '2.22',
        'buildargs': {
            'LATEST_ALPINE_VERSION': common_args['LATEST_ALPINE_VERSION'],
            'DIRB_DOWNLOAD_URL': "https://github.com/v0re/dirb.git"
        },
        'tests': []
    }
    return config