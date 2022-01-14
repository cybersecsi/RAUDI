from unittest.mock import patch
from unittest.mock import MagicMock
from helper import *
from tools.main import get_tools, get_single_tool, list_tools
from tools import main


import pytest
def fake_invalid_response(url):
    return []

good = [
  {
    "name": "v4.15.0",
    "zipball_url": "https://api.github.com/repos/vimeo/psalm/zipball/refs/tags/v4.15.0",
    "tarball_url": "https://api.github.com/repos/vimeo/psalm/tarball/refs/tags/v4.15.0",
    "commit": {
      "sha": "a1b5e489e6fcebe40cb804793d964e99fc347820",
      "url": "https://api.github.com/repos/vimeo/psalm/commits/a1b5e489e6fcebe40cb804793d964e99fc347820"
    },
    "node_id": "MDM6UmVmNzQzODYxNjc6cmVmcy90YWdzL3Y0LjE1LjA="
  },
  {
    "name": "v4.14.0",
    "zipball_url": "https://api.github.com/repos/vimeo/psalm/zipball/refs/tags/v4.14.0",
    "tarball_url": "https://api.github.com/repos/vimeo/psalm/tarball/refs/tags/v4.14.0",
    "commit": {
      "sha": "14dcbc908ab2625cd7a74258ee6c740cbecc6140",
      "url": "https://api.github.com/repos/vimeo/psalm/commits/14dcbc908ab2625cd7a74258ee6c740cbecc6140"
    },
    "node_id": "MDM6UmVmNzQzODYxNjc6cmVmcy90YWdzL3Y0LjE0LjA="
  }
]
not_found = {
                "message" : "Not Found",
                "documentation_url": "https://docs.github.com/rest/reference/repos#list-repository-tags"
}


def fake_not_found():
    return not_found

def test_github_no_json():
    # Should give an exception
    with patch('requests.get', wraps=fake_invalid_response):
        with pytest.raises(Exception) as e_info:
            get_latest_github_tag_no_browser_download("vimeo/psalm")
    
# Valid request
@patch('requests.Response')
@patch('requests.get')
def test_get_latest_github(fake_get, FakeResponse):
    instance = FakeResponse.return_value
    instance.json.return_value = good
    instance.status_code = 200
    fake_get.return_value = instance
    resp = get_latest_github_tag_no_browser_download("vimeo/psalm")
    fake_get.assert_called()
    assert resp['url'] == 'https://api.github.com/repos/vimeo/psalm/tarball/refs/tags/v4.15.0' 
    assert resp['version'] == 'v4.15.0'

@patch('requests.Response')
@patch('requests.get')
def test_get_latest_github_not_found(fake_get, FakeResponse):
    instance = FakeResponse.return_value
    instance.json.return_value = not_found
    instance.status_code = 404
    fake_get.return_value = instance
    with pytest.raises(ConnectionError) as e_info:
        resp = get_latest_github_tag_no_browser_download("vimeo/r")


@patch('requests.Response')
@patch('requests.get')
def test_list_not_call_requests(fake_get, FakeResponse):
    instance = FakeResponse.return_value
    instance.json.return_value = good
    instance.status_code = 200
    fake_get.return_value = instance
    # List method should not call requests
    assert fake_get.assert_not_called

from test.tools.apktool import config as apktool
from test.tools.bfac import config as bfac

@patch('test.tools.apktool.config.get_config')
@patch('test.tools.bfac.config.get_config')
def test_list_not_call_requests_get_tool_name(fake_bf, fake_apk):
  main.tools = [apktool, bfac]
  tool = get_single_tool('bfac', 2)
  fake_apk.assert_not_called()
  fake_bf.assert_called_once()
