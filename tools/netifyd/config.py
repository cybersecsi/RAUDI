import helper
import os

DEFAULT_DIRNAME = os.path.basename(os.path.dirname(__file__))

def version():
    return helper.grep(helper.get_remote_resource('http://download.netify.ai/netify/debian/10/Packages'), 'Version:')[0].split(":")[1].strip().replace('-','.')

def get_config(organization, common_args):
    
    config = {
        'name': organization+'/'+DEFAULT_DIRNAME,
        'version': version(),
        'buildargs': {
            'LATEST': common_args['LATEST_UBUNTU_VERSION'],
        },
        'tests': []
    }
    return config