class ToolValidationError(Exception):
    """Raised when a tool directory is missing required files."""


class Errors: 
    def github_request():
        return Exception("[-] ERROR In get_latest_github_tag_no_browser_download: request and parsing json failed.")
    def gitlab_request():
        return Exception("[-] ERROR In get_latest_gitlab: request and parsing json failed.")
    def gitlab_not_found():
        return Exception("[-] ERROR gitlab repository not found.")

    def connection_error(repo, status_code, message):
        return ConnectionError("repo: \"{}\" status_code: {} error: {}".format(repo, status_code, message))

    def invalid_tools(missing_files):
        details = [
            "tools/{}: missing {}".format(tool, ", ".join(files))
            for tool, files in missing_files.items()
        ]
        return ToolValidationError(
            "Invalid tool directories:\n- {}".format("\n- ".join(details))
        )
