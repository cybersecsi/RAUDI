def get_config(organization, common_args):
    config = {
        'name': organization+'/dirb',
        'version': '2.22',
        'buildargs': {
            'LATEST_ALPINE_VERSION': common_args['LATEST_ALPINE_VERSION'],
            'DIRB_DOWNLOAD_URL': "https://sourceforge.net/projects/dirb/files/dirb/2.22/dirb222.tar.gz/download"
        },
        'tests': []
    }
    return config