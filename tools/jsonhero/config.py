import helper


def get_config(organization, common_args):
    api_results = {
        'GITHUB_INFO': helper.get_latest_github_commit('triggerdotdev/jsonhero-web'),
    }

    config = {
        'name': organization+'/jsonhero',
        'version': helper.clean_version(api_results['GITHUB_INFO']),
        'buildargs': {
            'NODE_ALPINE_VERSION': common_args['NODE_ALPINE_VERSION'],
            'DOWNLOAD_URL': "https://github.com/triggerdotdev/jsonhero-web"
        },
        'tests': ['']
    }
    return config
