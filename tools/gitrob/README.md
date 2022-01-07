# Gitrob

## Description

Gitrob is a tool to help find potentially sensitive files pushed to public repositories on Github. Gitrob will clone repositories belonging to a user or organization down to a configurable depth and iterate through the commit history and flag files that match signatures for potentially sensitive files. The findings will be presented through a web interface for easy browsing and analysis.

## Usage
Here is the usage of **Gitrob**:

```
docker run -it --rm secsi/gitrob [options] <target> [target2] ... [targetN]
```

### Options
```
-bind-address string
    Address to bind web server to (default "127.0.0.1")
-commit-depth int
    Number of repository commits to process (default 500)
-debug
    Print debugging information
-github-access-token string
    GitHub access token to use for API requests
-load string
    Load session file
-no-expand-orgs
    Don't add members to targets when processing organizations
-port int
    Port to run web server on (default 9393)
-save string
    Save session to file
-silent
    Suppress all output except for errors
-threads int
    Number of concurrent threads (default number of logical CPUs)
```
## 🐳 RAUDI: Regularly and Automatically Updated Docker Images

Hello, friend. This Docker Image has been created by RAUDI. What is RAUDI?

**RAUDI** (Regularly and Automatically Updated Docker Images) automatically generates and keep updated a series of *Docker Images* through *GitHub Actions* for tools that are not provided by the developers.

**RAUDI** is what will save you from creating and managing a lot of Docker Images manually. Every time a software is updated you need to update the Docker Image if you want to use the latest features, the dependencies are not working anymore. 

This is messy and time-consuming. 

Don't worry anymore, we got you covered.

If you want to contribute, give us a star or take a quick look at the source code of **RAUDI** click [here](https://github.com/cybersecsi/RAUDI).