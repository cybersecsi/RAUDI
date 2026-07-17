import pytest
from types import SimpleNamespace
from unittest.mock import patch
from unittest.mock import MagicMock
# Import Helper functions
from raudi.helper import *
# Import Manager Singleton
from raudi.manager import Manager
from raudi.errors import ToolValidationError
from raudi import cli
# Import for specific tools
from test.tools.raudi import config as raudi
from test.tools.dsp import config as dsp


# Values
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

# Functions

def fake_invalid_response(url):
    return []

def fake_not_found():
    return not_found

def test_github_no_json():
    # Should give an exception
    with patch('requests.get', wraps=fake_invalid_response):
        with pytest.raises(Exception) as e_info:
            get_latest_github_tag_no_browser_download("vimeo/psalm")
  
# Tests

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

def test_gitlab_id_by_project():
  exp = 7348427
  assert get_gitlab_id_project("netify.ai", "netify-agent") == exp


def test_version_cleaner():
  assert clean_version('v1.0') == '1.0'
  assert clean_version('v1.2.3_4') == '1.2.3.4'
  assert clean_version('v1.2.0-beta') == '1.2.0'
  assert clean_version(' v.1.2.0-beta') == '1.2.0'
  assert clean_version(' 1.2-beta') == '1.2'


def test_get_env_accepts_false_default(monkeypatch):
  monkeypatch.delenv("RAUDI_GITHUB_ACTION", raising=False)
  assert get_env("RAUDI_GITHUB_ACTION", False) is False


@pytest.mark.parametrize("missing_file", ["config.py", "Dockerfile"])
def test_check_tools_reports_missing_required_file(tmp_path, monkeypatch, missing_file):
  tool_dir = tmp_path / "tools" / "incomplete"
  tool_dir.mkdir(parents=True)

  for filename in {"config.py", "Dockerfile"} - {missing_file}:
    (tool_dir / filename).touch()

  monkeypatch.chdir(tmp_path)

  with pytest.raises(ToolValidationError) as error:
    check_tools()

  assert "tools/incomplete" in str(error.value)
  assert "missing {}".format(missing_file) in str(error.value)


def test_get_config_names_accepts_complete_tool(tmp_path, monkeypatch):
  tool_dir = tmp_path / "tools" / "complete"
  tool_dir.mkdir(parents=True)
  (tool_dir / "config.py").touch()
  (tool_dir / "Dockerfile").touch()

  monkeypatch.chdir(tmp_path)

  assert get_config_names() == ["tools.complete.config"]


def test_manager_loads_config_from_tools_directory(tmp_path, monkeypatch):
  tool_dir = tmp_path / "tools" / "complete"
  tool_dir.mkdir(parents=True)
  (tool_dir / "config.py").write_text(
    "def get_config(organization, common_args):\n"
    "    return {'name': organization + '/complete'}\n"
  )
  (tool_dir / "Dockerfile").touch()

  manager = Manager()
  manager.set_tools([])
  monkeypatch.chdir(tmp_path)
  manager.init_tools()

  assert manager.list_tools() == ["complete"]


def test_list_command_reports_invalid_tool(tmp_path, monkeypatch, capsys):
  tool_dir = tmp_path / "tools" / "incomplete"
  tool_dir.mkdir(parents=True)
  (tool_dir / "Dockerfile").touch()

  args = SimpleNamespace(
    all=False,
    single=None,
    runsh=None,
    test=None,
    list=True,
    bootstrap=None,
    readme=False,
    push=False,
    remote=False,
    force=False,
  )
  manager = Manager()
  manager.set_exit_code(0)
  manager.set_tools([])
  monkeypatch.chdir(tmp_path)
  monkeypatch.setattr(cli.parser, "parse_args", lambda: args)

  with pytest.raises(SystemExit) as exit_info:
    cli.main()

  output = capsys.readouterr().out
  assert exit_info.value.code == 1
  assert "tools/incomplete: missing config.py" in output
