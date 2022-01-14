import helper
import os
import importlib
# Import all tools config files
tools = [] 
common_args = {}

# Default values
organization = 'secsi'

def init_tools():
    global tools 
    for module_name in helper.get_config_names():
        if importlib.util.find_spec(module_name):
            tools.append(importlib.import_module(module_name))
    # tools = [importlib.import_module(module) for module in helper.get_config_names() if importlib.find_loader(module)]
def init():
    init_tools()
    global common_args 
    common_args = {
        'LATEST_UBUNTU_VERSION': helper.get_latest_docker_hub_version('ubuntu', avoid_date=True),
        'LATEST_ALPINE_VERSION': helper.get_latest_docker_hub_version('alpine', avoid_date=True),
        'GOLANG_ALPINE_VERSION': 'alpine',
        'DEBIAN_SLIM_VERSION': '11-slim', # Future LTS
        'NODE_ALPINE_VERSION': '16-alpine', # LTS
        'PYTHON_ALPINE_VERSION': '3.9.9-alpine',
        'PYTHON2_ALPINE_VERSION': '2.7.18-alpine', # Only used for tools not compatible with Python3
        'OPENJDK_ALPINE_VERSION': '17-alpine', # LTS
        'RUBY_ALPINE_VERSION': '3.1.0-alpine',
        'PHP_ALPINE_VERSION': '7.4-cli-alpine'

    }

def _tool_name(t, depth = 1):
    return t.__name__.split('.')[depth] if hasattr(t, '__name__') else None

def list_tools():
    return  [_tool_name(t) for t in tools]

# List of all imported tools 
def get_tools():
    configured_tools = [tool.get_config(organization, common_args) for tool in tools]
    return configured_tools

# Get a single tool for specific build
def get_single_tool(tool_name, depth = 1):
    tool = next((t.get_config(organization, common_args) for t in tools if _tool_name(t, depth) == tool_name), None) # returns None if tool is not found
    return tool 