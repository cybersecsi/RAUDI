from tools.dirb import config as dirb
from tools.dirhunt import config as dirhunt
from tools.ffuf import config as ffuf
from tools.gobuster import config as gobusterdns

tools = [dirb, dirhunt, ffuf, gobusterdns]

# List of all imported tools 
def get_tools():
    return tools

# Get a single tool for specific build
def get_single_tool(tool_name):
    tool = next((t for t in tools if t.__name__.split('.')[1] == tool_name), None) # returns None if tool is not found
    return tool 