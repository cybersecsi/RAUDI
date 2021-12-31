import helper
# Import all tools config files
import tools.bfac.config as bfac
import tools.dirb.config as dirb
import tools.dirhunt.config as dirhunt
import tools.ffuf.config as ffuf
import tools.findsploit.config as findsploit
import tools.gobuster.config as gobuster
import tools.hydra.config as hydra
import tools.knockpy.config as knockpy
import tools.masscan.config as masscan
import tools.retire.config as retire
import tools.sublist3r.config as sublist3r
import tools.whatweb.config as whatweb

# Default values
organization = 'secsi'

common_args = {
    'LAST_UBUNTU_VERSION': helper.get_latest_docker_hub_version('ubuntu'),
}

tools = [bfac, dirb, dirhunt, ffuf, findsploit, gobuster, hydra, knockpy, masscan, retire, sublist3r, whatweb]

def _tool_name(t):
    return t.__name__.split('.')[1] if hasattr(t, '__name__') else None

def list_tools():
    return  [_tool_name(t) for t in tools]


# List of all imported tools 
def get_tools():
    configured_tools = [tool.get_config(organization, common_args) for tool in tools]
    return configured_tools

# Get a single tool for specific build
def get_single_tool(tool_name):    
    tool = next((t.get_config(organization, common_args) for t in tools if _tool_name(t) == tool_name), None) # returns None if tool is not found
    return tool 