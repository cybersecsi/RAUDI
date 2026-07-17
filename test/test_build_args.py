from types import SimpleNamespace

import pytest

from raudi import helper
from raudi.manager import Manager


def write_dockerfile(tmp_path, contents):
    tool_dir = tmp_path / "tools" / "example"
    tool_dir.mkdir(parents=True)
    (tool_dir / "Dockerfile").write_text(contents)
    return tmp_path / "tools"


def test_check_and_fill_args_adds_declared_common_args(tmp_path):
    tools_dir = write_dockerfile(
        tmp_path,
        "ARG LATEST_ALPINE_VERSION\n"
        "FROM alpine:$LATEST_ALPINE_VERSION\n"
        "ARG DOWNLOAD_URL\n",
    )

    result = helper.check_and_fill_args(
        "example",
        {"DOWNLOAD_URL": "https://example.com/tool.tar.gz"},
        {"LATEST_ALPINE_VERSION": "3.23"},
        tools_dir=tools_dir,
    )

    assert result == {
        "DOWNLOAD_URL": "https://example.com/tool.tar.gz",
        "LATEST_ALPINE_VERSION": "3.23",
    }


def test_check_and_fill_args_reports_all_missing_args(tmp_path):
    tools_dir = write_dockerfile(
        tmp_path,
        "ARG FIRST_REQUIRED\nARG SECOND_REQUIRED\n",
    )

    with pytest.raises(ValueError) as error:
        helper.check_and_fill_args("example", {}, {}, tools_dir=tools_dir)

    assert "example" in str(error.value)
    assert "FIRST_REQUIRED, SECOND_REQUIRED" in str(error.value)


def test_check_and_fill_args_allows_dockerfile_defaults(tmp_path):
    tools_dir = write_dockerfile(
        tmp_path,
        "ARG OPTIONAL_VERSION=latest\nFROM example:$OPTIONAL_VERSION\n",
    )

    assert helper.check_and_fill_args("example", {}, {}, tools_dir=tools_dir) == {}


def test_check_and_fill_args_does_not_mutate_input(tmp_path):
    tools_dir = write_dockerfile(tmp_path, "ARG COMMON_VERSION\n")
    buildargs = {}

    helper.check_and_fill_args(
        "example",
        buildargs,
        {"COMMON_VERSION": "1.0"},
        tools_dir=tools_dir,
    )

    assert buildargs == {}


@pytest.mark.parametrize(
    ("buildargs", "common_args", "message"),
    [
        ([], {}, "buildargs"),
        ({}, [], "common_args"),
    ],
)
def test_check_and_fill_args_validates_mappings(
    tmp_path,
    buildargs,
    common_args,
    message,
):
    tools_dir = write_dockerfile(tmp_path, "ARG VERSION\n")

    with pytest.raises(TypeError, match=message):
        helper.check_and_fill_args(
            "example",
            buildargs,
            common_args,
            tools_dir=tools_dir,
        )


def test_manager_automatically_fills_common_args(tmp_path, monkeypatch):
    write_dockerfile(
        tmp_path,
        "ARG COMMON_VERSION\nARG DOWNLOAD_URL\n",
    )
    tool = SimpleNamespace(
        __name__="tools.example.config",
        get_config=lambda organization, common_args: {
            "name": organization + "/example",
            "version": "1.0",
            "buildargs": {"DOWNLOAD_URL": "https://example.com/tool.tar.gz"},
            "tests": [],
        },
    )
    manager = Manager()
    monkeypatch.setattr(manager, "_tools", [tool])
    monkeypatch.setattr(manager, "_common_args", {"COMMON_VERSION": "2.0"})
    monkeypatch.chdir(tmp_path)

    config = manager.get_single_tool("example")

    assert config["buildargs"]["COMMON_VERSION"] == "2.0"
