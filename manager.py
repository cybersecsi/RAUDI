import helper
import importlib

class Manager(object):
    _organization = None
    _exit_code = 0
    _tools = []
    _common_args = {}

    """Implement it as a Singleton"""
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Manager, cls).__new__(cls)
        return cls.instance

    def __init__(self, organization='secsi'):
        self._organization = organization

    def _tool_name(self, t, depth = 1):
        return t.__name__.split('.')[depth] if hasattr(t, '__name__') else None
    
    def init(self):
        self.init_common_args()
        self.init_tools()

    def init_common_args(self):
        self._common_args = {
            'LATEST_UBUNTU_VERSION': helper.get_latest_docker_hub_version('ubuntu', avoid_date=True),
            'LATEST_ALPINE_VERSION': helper.get_latest_docker_hub_version('alpine', avoid_date=True),
            'GOLANG_ALPINE_VERSION': 'alpine',
            'DEBIAN_SLIM_VERSION': '13-slim', # Future LTS
            'NODE_ALPINE_VERSION': 'lts-alpine', # LTS
            'PYTHON_ALPINE_VERSION': '3.14.2-alpine',
            'PYTHON2_ALPINE_VERSION': '2.7.18-alpine', # Only used for tools not compatible with Python3
            'PYTHON3_SLIM_VERSION': '3.14-slim-trixie',
            'OPENJDK_ALPINE_VERSION': '21-alpine', # LTS
            'OPENJDK8_ALPINE_VERSION': '8-alpine',  #
            'RUBY_ALPINE_VERSION': '3.1.0-alpine',
            'PHP_ALPINE_VERSION': '8.4.3-cli-alpine',
            'RUBY2_ALPINE_VERSION': '3.2.2-alpine',
            'LATEST_GCC_VERSION': '9.5.0',
            'LATEST_BUSYBOX_GLIBC_VERSION': '1.34.1-glibc',

        }

    def init_tools(self):
        for module_name in helper.get_config_names():
            if importlib.util.find_spec(module_name):
                self._tools.append(importlib.import_module(module_name))

    def list_tools(self):
        return  [self._tool_name(t) for t in self._tools]

    # List of all imported tools 
    def get_tools(self):
        configured_tools = []
        for tool in self._tools:
            fancy_name = tool.__name__.split('.')[1]
            helper.log(f"Loading {fancy_name}")
            configured_tools.append(tool.get_config(self._organization, self._common_args))
        return configured_tools

    # Get a single tool for specific build
    def get_single_tool(self, tool_name, depth = 1):
        tool = next((t.get_config(self._organization, self._common_args) for t in self._tools if self._tool_name(t, depth) == tool_name), None) # returns None if tool is not found
        return tool 

    # Set tools (for testing purposes)
    def set_tools(self, tools):
        self._tools = tools

    def get_exit_code(self):
        return self._exit_code

    # Set exit code (for Github Actions)
    def set_exit_code(self, exit_code):
        self._exit_code = exit_code