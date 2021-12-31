# 🐳 HOUDINI: Hacking Offensive Updated Docker Images for Network Intrusion

**HOUDINI** (Hacking Offensive Updated Docker Images for Network Intrusion) automatically generates *Docker Images* for Network Security-related tools that are not provided by the developers. The Images are automatically updated through the GitHub Actions.

[![Documentation](https://img.shields.io/badge/Documentation-complete-green.svg?style=flat)](https://github.com/cybersecsi/HOUDINI/blob/main/README.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/cybersecsi/HOUDINI/blob/main/LICENSE.md)

## Table of Contents
  - [What is HOUDINI](#what-is-houdini)
  - [Setup](#setup)
  - [Usage](#usage)
  - [Tool Structure](#tool-structure)
  - [Roadmap](#roadmap)
  - [Contributions](#contributions)
  - [Credits](#credits)
  - [License](#license)

## What is HOUDINI
**HOUDINI** is what will save you from creating and managing a lot of Docker Images manually. Every time a software is updated you need to update the Docker Image if you want to use the latest features, the dependencies are not working anymore. 
This is messy and time-consuming. 
Don't worry anymore, we got you covered.

## Setup
This repo can also be executed locally. The requirements to be met are the following:
- Python 3.x
- Docker

The setup phase is pretty straightforward, you just need the following commands:
```
git clone https://github.com/cybersecsi/HOUDINI
cd HOUDINI
pip install -r requirements.txt
```

You're ready to go!

## Usage
**HOUDINI** can build and push all the tools that are put into the *tools* directory. There are different options that can be used when running it.

### Execution Modes

#### Normal Execution
In this mode HOUDINI tries to build all the tools if needed. The command to run it is simply:
```
./houdini.py
```

#### Single Build
In this mode HOUDINI tries to build only the specified tool. The command in this case is:
```
./houdini --single <tool_name>
```
*tool_name* MUST be the name of the directory inside the *tools* folder.

### Options
| Option | Description                             | Default Value |
|--------|-----------------------------------------|---------------|
| --push | Wheter automatically push to Docker Hub | False         |

## Available Tools
This is the current list of tools that have been added. Those are all tools that do not have an official Docker Image provided by the developer:
- dirb
- dirhunt
- ffuf
- gobuster
- hydra
- knock
- masscan
- sublist3r
- WhatWeb

## Tool Structure
Every tool in the tools directory contains **at least** Dockerfile.

If you want to add a new tool you just have to create a folder for that specific tool inside the *tools* directory. In this folder you have to insert the *Dockerfile* with defined **build args** to customize and automate the build.
Once you created the Dockerfile you need to add the tools inside the *tools* dict in *tools/main.py*. This dict has a key for every tool and has the following structure:
```
  <tool_name>: {
      'name': '<name_of_the_image>',
      'version': '', # Can be an helper function
      'buildargs': {
      }
    }
```
The three keys are:
- **name**: the name of the Docker Image (e.g. secsi/<tool_name>)
- **version**: the version number of the Docker Image. For this you may use a helper function that **is able to retrieve the latest available version number** (look at *tools/ffuf* for an example).
- **buildargs**: a dict to specify the parts of the Docker Images that are subject to updates (again: look at *tools/ffuf* for an example)

Once you completed those **two simple steps** you are done! Just be careful that the **name** of the tool **MUST BE THE SAME** as the directory in which you placed its Dockerfile.

## Examples
This section provides examples for the currently added Network Security Tools. As you can see the images do provide only the tool, so if you need to use a **wordlist** you need to mount it.
### dirb
```
docker run -it --rm -v <wordlist_src_dir>:<wordlist_container_dir> secsi/dirb <url> <wordlist_container_dir>/<wordlist_file>
```
### dirhunt
```
docker run -it --rm secsi/dirhunt <url>
```
### ffuf
```
docker run -it --rm -v <wordlist_src_dir>:<wordlist_container_dir> secsi/ffuf -w <wordlist_container_dir>/<wordlist_file> -u <url>
```
### gobuster
```
docker run -it --rm -v <wordlist_src_dir>:<wordlist_container_dir> secsi/gobuster dir -e -u <url> -w <wordlist_container_dir>/<wordlist_file>
```

### hydra
```
docker run -it --rm -v <wordlist_src_dir>:<wordlist_container_dir> secsi/hydra -l root -P <wordlist_container_dir>/<wordlist_file> -t 4 -vV ssh://<url>
```

### knockpy
```
docker run -it --rm secsi/knockpy <url>
```

### masscan
```
docker run -it --rm secsi/masscan <target_ip_address> -p<port_number>
```

### sublist3r
```
docker run -it --rm secsi/sublist3r -d <url>
```

### whatweb
```
docker run -it --rm secsi/whatweb <url>
```

## Roadmap
- [x] Add GitHub Actions
- [ ] Add '--local' option
- [ ] Add README for every tool
- [ ] Add custom logger
- [ ] Better error handling
- [ ] Config file for customization (like the organization name)
- [ ] Add tests for each tool

## Contributions
Everyone is invited to contribute!
If you are a user of the tool and have a suggestion for a new feature or a bug to report, please do so through the issue tracker.

## Credits
Developed by Angelo Delicato [@SecSI](https://secsi.io)

## License
**HOUDINI** is an open-source and free software released under the [MIT License](/LICENSE).