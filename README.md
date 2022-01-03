# 🐳 HOUDINI: Hacking Offensive Updated Docker Images for Network Intrusion

**HOUDINI** (Hacking Offensive Updated Docker Images for Network Intrusion) automatically generates *Docker Images* for Network Security-related tools that are not provided by the developers. The Images are automatically updated through the GitHub Actions.

[![Documentation](https://img.shields.io/badge/Documentation-complete-green.svg?style=flat)](https://github.com/cybersecsi/HOUDINI/blob/main/README.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/cybersecsi/HOUDINI/blob/main/LICENSE)

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
./houdini.py --all
```

#### Single Build
In this mode HOUDINI tries to build only the specified tool. The command in this case is:
```
./houdini.py --single <tool_name>
```
*tool_name* MUST be the name of the directory inside the *tools* folder.

#### Show tools
If you want to know the available tools you can run this command:
```
./houdini.py --list
```

### Options
| Option | Description                             | Default Value |
|--------|-----------------------------------------|---------------|
| --push | Wheter automatically push to Docker Hub | False         |

## Available Tools
This is the current list of tools that have been added. Those are all tools that do not have an official Docker Image provided by the developer:

| Name      | Docker Image    | Source                                       |
|-----------|-----------------|----------------------------------------------|
| dirb      | secsi/dirb      | http://dirb.sourceforge.net/                 |
| dirhunt   | secsi/dirhunt   | https://github.com/Nekmo/dirhunt             |
| ffuf      | secsi/ffuf      | https://github.com/ffuf/ffuf                 |
| gobuster  | secsi/gobuster  | https://github.com/OJ/gobuster               |
| hydra     | secsi/hydra     | https://github.com/vanhauser-thc/thc-hydra   |
| knock     | secsi/knockpy   | https://github.com/guelfoweb/knock           |
| MASSCAN   | secsi/masscan   | https://github.com/robertdavidgraham/masscan |
| Retire.js | secsi/retire    | https://github.com/RetireJS/retire.js        |
| Sublist3r | secsi/sublist3r | https://github.com/aboul3la/Sublist3r        |
| WhatWeb   | secsi/whatweb   | https://github.com/urbanadventurer/WhatWeb   |

## Tool Structure
Every tool in the tools directory contains **at least** two file:
- config.py
- Dockerfile.

If you want to add a new tool you just have to create a folder for that specific tool inside the *tools* directory. In this folder you have to insert the *Dockerfile* with defined **build args** to customize and automate the build. Once you created the Dockerfile you have to create a *config.py* in the same directory with a function called *get_config(organization, common_args)*. Be careful: the function MUST be called this way and MUST have those two parameters (even if you do not use them). The returning value is the **config** for that specific tool and has the following structure:
```
config =  {
    'name': organization+'/<name_of_the_image>',
    'version': '', # Should be an helper function
    'buildargs': {
    }
  }
```
The three keys are:
- **name**: the name of the Docker Image (e.g. secsi/<tool_name>)
- **version**: the version number of the Docker Image. For this you may use a helper function that **is able to retrieve the latest available version number** (look at *tools/ffuf* for an example).
- **buildargs**: a dict to specify the parts of the Docker Images that are subject to updates (again: look at *tools/ffuf* for an example)

After doing so you are good to go! Just be careful that the **name** of the tool **MUST BE THE SAME** as the directory in which you placed its Dockerfile.

## Examples
This section provides examples for the currently added Network Security Tools. As you can see the images do provide only the tool, so if you need to use a **wordlist** you need to mount it.

### Generic Example
```
docker run -it --rm secsi/<tool> <command>
```
### Specific example
```
docker run -it --rm -v <wordlist_src_dir>:<wordlist_container_dir> secsi/dirb <url> <wordlist_container_dir>/<wordlist_file>
```

## Roadmap
- [x] Add GitHub Actions
- [ ] ~~Add '--local' option~~ Add '--remote' option (by default it is local)
- [x] ~~Add README for every tool~~ Add general README for all Houdini Docker Image
- [x] Add custom logger
- [ ] Better error handling
- [x] ~~Config file for customization (like the organization name)~~ Customizable organization name in *tools/main.py*
- [ ] Add tests for each tool

## Contributions
Everyone is invited to contribute!
If you are a user of the tool and have a suggestion for a new feature or a bug to report, please do so through the issue tracker.

## Credits
HOUDINI is proudly developed [@SecSI](https://secsi.io) by:
- [Angelo Delicato](https://github.com/thelicato)
- [Daniele Capone](https://github.com/daniele-capone)
- [Gaetano Perrone](https://github.com/giper45)

## License
**HOUDINI** is an open-source and free software released under the [MIT License](/LICENSE).