import helper

organization = 'secsi'

tools = {
    'dirb': {
        'name': organization+'/dirb',
        'version': 'latest',
        'buildargs': {
            'LAST_UBUNTU_VERSION': helper.get_latest_docker_hub_version('ubuntu')
        }
    },
    'dirhunt': {
        'name': organization+'/dirhunt',
        'version': helper.get_latest_pip_version('dirhunt'),
        'buildargs': {
            'DIRHUNT_VERSION': helper.get_latest_pip_version('dirhunt')
        }
    },
    'ffuf': {
        'name': organization+'/ffuf',
        'version': helper.get_latest_github_release('ffuf/ffuf', target_string='linux_amd64')['version'][1:], # Remove the leading 'v'
        'buildargs': {
            'LAST_UBUNTU_VERSION': helper.get_latest_docker_hub_version('ubuntu'),
            'FFUF_DOWNLOAD_URL': helper.get_latest_github_release('ffuf/ffuf', target_string='linux_amd64')['url']
        }
    },
    'gobuster': {
        'name': organization+'/gobuster',
        'version': helper.get_latest_github_release('OJ/gobuster', target_string='linux-amd64')['version'][1:], # Remove the leading 'v',
        'buildargs': {
            'LAST_UBUNTU_VERSION': helper.get_latest_docker_hub_version('ubuntu'),
            'GOBUSTER_DOWNLOAD_URL': helper.get_latest_github_release('OJ/gobuster', target_string='linux-amd64')['url']
        }
    },
    'sublist3r': {
        'name': organization+'/sublist3r',
        'version': helper.get_latest_github_release_no_browser_download('aboul3la/Sublist3r')['version'],
        'buildargs': {
            'SUBLIST3R_DOWNLOAD_URL': helper.get_latest_github_release_no_browser_download('aboul3la/Sublist3r')['url']
        }
    }
}

# List of all imported tools 
def get_tools():
    return tools

# Get a single tool for specific build
def get_single_tool(tool_name):
    tool = next((tools[t] for t in tools if t == tool_name), None) # returns None if tool is not found
    return tool 