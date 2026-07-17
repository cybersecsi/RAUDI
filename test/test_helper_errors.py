from unittest.mock import Mock

import pytest
import requests

from raudi import helper


@pytest.mark.parametrize(
    "helper_call",
    [
        lambda: helper.get_latest_docker_hub_version("ubuntu"),
        lambda: helper.get_latest_pip_version("example-package"),
        lambda: helper.get_latest_npm_registry_version("example-package"),
        lambda: helper.get_latest_github_release("owner/repo", "linux"),
        lambda: helper.get_latest_github_release_no_browser_download("owner/repo"),
        lambda: helper.get_latest_github_tag_no_browser_download("owner/repo"),
        lambda: helper.get_latest_github_commit("owner/repo"),
        lambda: helper.get_gitlab_id_project("owner", "repo"),
        lambda: helper.get_remote_resource("https://example.com/resource"),
        lambda: helper.check_if_readme_is_set("owner/image"),
    ],
)
def test_http_helpers_reject_unsuccessful_status_codes(monkeypatch, helper_call):
    response = Mock(status_code=503, reason="Service Unavailable")
    response.json.return_value = {"message": "temporarily unavailable"}
    monkeypatch.setattr(helper.requests, "get", Mock(return_value=response))

    with pytest.raises(ConnectionError, match="status_code: 503"):
        helper_call()


@pytest.mark.parametrize(
    "helper_call",
    [
        lambda: helper.get_latest_gitlab_tag("owner", "repo"),
        lambda: helper.get_latest_gitlab_commit("owner", "repo"),
    ],
)
def test_gitlab_helpers_reject_unsuccessful_status_codes(monkeypatch, helper_call):
    response = Mock(status_code=503, reason="Service Unavailable")
    response.json.return_value = {"message": "temporarily unavailable"}
    monkeypatch.setattr(helper, "get_gitlab_id_project", Mock(return_value=123))
    monkeypatch.setattr(helper.requests, "get", Mock(return_value=response))

    with pytest.raises(ConnectionError, match="status_code: 503"):
        helper_call()


def test_http_helpers_report_invalid_json(monkeypatch):
    response = Mock(status_code=200)
    response.json.side_effect = ValueError("invalid JSON")
    monkeypatch.setattr(helper.requests, "get", Mock(return_value=response))

    with pytest.raises(ValueError, match="Invalid JSON response"):
        helper.get_latest_pip_version("example-package")


def test_http_helpers_report_network_errors(monkeypatch):
    monkeypatch.setattr(
        helper.requests,
        "get",
        Mock(side_effect=requests.ConnectionError("network unavailable")),
    )

    with pytest.raises(ConnectionError, match="network unavailable"):
        helper.get_remote_resource("https://example.com/resource")


def test_github_release_requires_matching_asset(monkeypatch):
    response = Mock(status_code=200)
    response.json.return_value = {"assets": [], "tag_name": "v1.0.0"}
    monkeypatch.setattr(helper.requests, "get", Mock(return_value=response))

    with pytest.raises(LookupError, match="No release asset matching"):
        helper.get_latest_github_release("owner/repo", "linux")


def test_github_tags_require_versioned_tag(monkeypatch):
    response = Mock(status_code=200)
    response.json.return_value = [
        {"name": "nightly", "tarball_url": "https://example.com/nightly.tar.gz"}
    ]
    monkeypatch.setattr(helper.requests, "get", Mock(return_value=response))

    with pytest.raises(LookupError, match="No version tags found"):
        helper.get_latest_github_tag_no_browser_download("owner/repo")
