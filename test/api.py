import os
import sys
import inspect
from helper import *

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

def test_gitlab():
    url = get_latest_gitlab_tag("netify.ai", "netify-agent")
    print(url)


t = get_remote_resource("http://download.netify.ai/netify/debian/10/Packages")
print(grep(t, "Version:")[0].split(":")[1].strip())