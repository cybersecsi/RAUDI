import helper
import os

DEFAULT_DIRNAME = os.path.basename(os.path.dirname(__file__))

def version():
    return helper.grep(helper.get_remote_resource('http://download.netify.ai/netify/debian/10/Packages'), 'Version:')[0].split(":")[1]

def get_config(organization, common_args):
    
    config = {
        'name': organization+'/'+DEFAULT_DIRNAME,
        'version': helper.clean_version(version()),
        'buildargs': {
            'KEY_URL': 'http://download.netify.ai/netify/ubuntu/apt-gpg-key-netify.asc'
        },
        'tests': []
    }
    return config