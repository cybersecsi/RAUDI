class Errors: 
    def github_request():
        return Exception("[-] ERROR In get_latest_github_tag_no_browser_download: request and parsing json failed.")

    def connection_error(repo, status_code, message):
        return ConnectionError("repo: \"{}\" status_code: {} error: {}".format(repo, status_code, message))