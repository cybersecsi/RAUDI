import requests

NMAP_SVN_RELEASES_URL = "https://svn.nmap.org/nmap-releases/"

def last_release():
    r = requests.get(NMAP_SVN_RELEASES_URL)
    lines = r.text.split('\n')

    HTML_TAG = "<li>"
    HTML_CONTENT = "nmap"
    version_tags = []
    for line in lines:
        if HTML_TAG in line and HTML_CONTENT in line:
            content = line.split('<li>')[1].split('>')[1].split('/')[0]
            version_tag = content.split('-')[1]
            version_tags.append(version_tag)
    last_version_tag = version_tags[len(version_tags) - 1]
    return last_version_tag

def get_config(organization, common_args):   
    last_version_tag = last_release()

    config = {
        'name': organization+'/nmap',
        'version': last_version_tag,
        'buildargs': {
            'LATEST_ALPINE_VERSION': common_args['LATEST_ALPINE_VERSION'],
            'NMAP_LAST_RELEASE_URL': f"{NMAP_SVN_RELEASES_URL}nmap-{last_version_tag}/"
        },
        'tests': ['-h']
    }
    return config