# BFAC

## Description
BFAC (Backup File Artifacts Checker) is an automated tool that checks for backup artifacts that may disclose the web-application's source code. The artifacts can also lead to leakage of sensitive information, such as passwords, directory structure, etc.

The goal of BFAC is to be an all-in-one tool for backup-file artifacts black-box testing.

## Usage
Here is a detailed usage for BFAC:

| Description                                                | Command                                                                     |
|------------------------------------------------------------|-----------------------------------------------------------------------------|
| Help                                                       | `docker run -it --rm secsi/bfac --help`                                     |
| Check a single URL.                                        | `docker run -it --rm secsi/bfac --url <url>`                                |
| Single URL with a different level (level 2 for example).   | `docker run -it --rm secsi/bfac --url <url> --level 2`                      |
| Single URL and show the results only.                      | `docker run -it --rm secsi/bfac --no-text --url <url>`                      |
| Limit the test to exposed DVCS tests.                      | `docker run -it --rm secsi/bfac --dvcs-test --url <url>`                    |
| Verify existence of files using Content-Length checks only.| `docker run -it --rm secsi/bfac --detection-technique content_length <url>` |
| Verify existence of files using Status-Code checks only.   | `docker run -it --rm secsi/bfac --detection-technique status_code <url>`    |
| Exclude results with specific status-codes.                | `docker run -it --rm secsi/bfac --exclude-status-codes 301,999 <url>`       |

## 🐳 RAUDI: Regularly and Automatically Updated Docker Images

Hello, friend. This Docker Image has been created by RAUDI. What is RAUDI?

**RAUDI** (Regularly and Automatically Updated Docker Images) automatically generates and keep updated a series of *Docker Images* through *GitHub Actions* for tools that are not provided by the developers.

**RAUDI** is what will save you from creating and managing a lot of Docker Images manually. Every time a software is updated you need to update the Docker Image if you want to use the latest features, the dependencies are not working anymore. 

This is messy and time-consuming. 

Don't worry anymore, we got you covered.

If you want to contribute, give us a star or take a quick look at the source code of **RAUDI** click [here](https://github.com/cybersecsi/RAUDI).