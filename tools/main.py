import helper
import importlib
# Import all tools config files
tools = [importlib.import_module(module) for module in helper.get_config_names()]

# Default values
organization = 'secsi'

common_args = {
    'LAST_UBUNTU_VERSION': helper.get_latest_docker_hub_version('ubuntu'),
    'LAST_ALPINE_VERSION': helper.get_latest_docker_hub_version('alpine'),
}

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