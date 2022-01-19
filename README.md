# 🐳 RAUDI: Regularly and Automatically Updated Docker Images

**RAUDI** (Regularly and Automatically Updated Docker Images) automatically generates and keep updated a series of *Docker Images* through *GitHub Actions* for tools that are not provided by the developers.

[![Documentation](https://img.shields.io/badge/Documentation-complete-green.svg?style=flat)](https://github.com/cybersecsi/RAUDI/blob/main/README.md)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://github.com/cybersecsi/RAUDI/blob/main/LICENSE)
[![Mentioned in awesome-docker](https://awesome.re/mentioned-badge.svg)](https://github.com/veggiemonk/awesome-docker)

## Table of Contents
  - [What is RAUDI](#what-is-raudi)
  - [Fork](#fork)
  - [Setup](#setup)
  - [Test](#test)
  - [Local Usage](#local-usage)
  - [Available Tools](#available-tools)
  - [Tool Structure](#tool-structure)
  - [Helpers](#helpers)
  - [Examples](#examples)
  - [How to Pronounce](#how-to-pronounce)
  - [Contributions](#contributions)
  - [Credits](#credits)
  - [License](#license)

## What is RAUDI
**RAUDI** is what will save you from creating and managing a lot of Docker Images manually. Every time a software is updated you need to update the Docker Image if you want to use the latest features, the dependencies are not working anymore. 

This is messy and time-consuming. 

Don't worry anymore, we got you covered.

You may either fork this repo and use the GitHub Workflow yourself or use it locally (and manage its execution the way you want).

## Fork
If you want to fork this repo you also have to set up some secrets to be able to push your images on your personal Docker Hub account.
Two GitHub secrets **must** be set:
- **DOCKER_USER**: Your Docker Hub Username;
- **DOCKER_API_TOKEN**: Your Docker Hub Password or API Token. 

After setting those secrets you have to edit the **organization** variable set in the *tools/main.py* file since it is configured to push on the Docker Hub for [SecSI](https://hub.docker.com/u/secsi). 

That's all guys: go to **Action**, enable it for your forked repo, wait until midnight, and the Workflow will do the heavy work!

## Setup
This repo can also be executed locally. The requirements to be met are the following:
- Python 3.x
- Docker

The setup phase is pretty straightforward, you just need the following commands:
```
git clone https://github.com/cybersecsi/RAUDI
cd RAUDI
pip install -r requirements.txt
```

You're ready to go!

## Test
To run the test you need to install ``pytest`` with the command ``pip install pytest`` (it is not in ``requirements.txt`` since it is needed only for testing purposes) and then you may run:
```
pytest -s 
```  
or 
```
python -m pytest -s
```

to run the tests.   

## Local Usage
**RAUDI** can build and push all the tools that are put into the *tools* directory. There are different options that can be used when running it. Before using it locally you should create a **.env** file (you can just copy the **.env.sample** file) and add your *GitHub Personal Access Token* to avoid Rate Limiting. For unauthenticated users GitHub allows up to 60 requests per hour, while authenticated users are allowed up to 15.000 requests per hour. For this reason we advice you to add it!
You can also create a personal access token without any scope since anything we do is read some info for every GitHub repo.

### Execution Modes

#### Normal Execution
In this mode RAUDI tries to build all the tools if needed. The command to run it is simply:
```
python3 ./raudi.py --all
```

#### Single Build
In this mode RAUDI tries to build only the specified tool. The command in this case is:
```
python3 ./raudi.py --single <tool_name>
```
*tool_name* MUST be the name of the directory inside the *tools* folder.

#### Test tool
Since the *tests* parameter has been added to the configuration structure of the tool is can be helpful to test if the inserted commands **do return a 0 status code**. The command to test a specific tool is:
```
python3 ./raudi.py --test <tool_name>
```
*tool_name* MUST be the name of the directory inside the *tools* folder.

#### Show tools
If you want to know the available tools you can run this command:
```
python3 ./raudi.py --list
```

#### Bootstrap tool
If you want to quickly add a new tool folder starting from one of the available templates you can run this command:
```
python3 ./raudi.py --bootstrap <new_tool_name>
```

### Options
| Option   | Description                                                           | Default Value |
|----------|-----------------------------------------------------------------------|---------------|
| --push   | Whether automatically push to Docker Hub                              | False         |
| --remote | Whether check against Docker Hub instead of local Docker before build | False         |
| --force  | Whether build or not if an image with the same tagname has been found | False         |

## Available Tools
This is the current list of tools that have been added. Those are all tools that do not have an official Docker Image provided by the developer:

| Name                       | Docker Image         | Source                                           |
|----------------------------|----------------------|--------------------------------------------------|
| Altdns                     | secsi/altdns         | https://github.com/infosec-au/altdns             |
| Apktool                    | secsi/apktool        | https://github.com/iBotPeaches/Apktool           |
| Arjun                      | secsi/arjun          | https://github.com/s0md3v/Arjun                  |
| bfac                       | secsi/bfac           | https://github.com/mazen160/bfac                 |
| CloudFail                  | secsi/cloudfail      | https://github.com/m0rtem/CloudFail              |
| CMSeeK                     | secsi/cmseek         | https://github.com/Tuhinshubhra/CMSeeK           |
| datasploit                 | secsi/datasploit     | https://github.com/DataSploit/datasploit         |
| dex2jar                    | secsi/dex2jar        | https://github.com/pxb1988/dex2jar               |
| dirb                       | secsi/dirb           | http://dirb.sourceforge.net/                     |
| dirhunt                    | secsi/dirhunt        | https://github.com/Nekmo/dirhunt                 |
| dirsearch                  | secsi/dirsearch      | https://github.com/maurosoria/dirsearch          |
| dnscan                     | secsi/dnscan         | https://github.com/rbsec/dnscan                  |
| Dorks Eye                  | secsi/dorks-eye      | https://github.com/BullsEye0/dorks-eye           |
| dvcs-ripper                | secsi/dvcs-ripper    | https://github.com/kost/dvcs-ripper              |
| EyeWitness                 | secsi/eyewitness     | https://github.com/FortyNorthSecurity/EyeWitness |
| fast-recon                 | secsi/fast-recon     | https://github.com/DanMcInerney/fast-recon       |
| ffuf                       | secsi/ffuf           | https://github.com/ffuf/ffuf                     |
| fierce                     | secsi/fierce         | https://github.com/mschwager/fierce              |
| Findsploit                 | secsi/findsploit     | https://github.com/1N3/Findsploit                |
| GetJS                      | secsi/getjs          | https://github.com/003random/getJS               |
| Gitrob                     | secsi/gitrob         | https://github.com/michenriksen/gitrob           |
| GitTools                   | secsi/gittools       | https://github.com/internetwache/GitTool         |
| gobuster                   | secsi/gobuster       | https://github.com/OJ/gobuster                   |
| GoogD0rker                 | secsi/googd0rker     | https://github.com/ZephrFish/GoogD0rker          |
| GoSpider                   | secsi/gospider       | https://github.com/jaeles-project/gospider       |
| Ground control             | secsi/ground-control | https://github.com/jobertabma/ground-control     |
| Hakrawler                  | secsi/hakrawler      | https://github.com/hakluke/hakrawler             |
| hakrevdns                  | secsi/hakrevdns      | https://github.com/hakluke/hakrevdns             |
| httprobe                   | secsi/httprobe       | https://github.com/tomnomnom/httprobe            |
| hydra                      | secsi/hydra          | https://github.com/vanhauser-thc/thc-hydra       |
| impacket                   | secsi/impacket       | https://github.com/SecureAuthCorp/impacket       |
| JoomScan                   | secsi/joomscan       | https://github.com/OWASP/joomscan                |
| The JSON Web Token Toolkit | secsi/jwt_tool       | https://github.com/ticarpi/jwt_tool              |
| knock                      | secsi/knockpy        | https://github.com/guelfoweb/knock               |
| LFI Suite                  | secsi/lfisuite       | https://github.com/D35m0nd142/LFISuite           |
| LinkFinder                 | secsi/linkfinder     | https://github.com/GerbenJavado/LinkFinder       |
| MASSCAN                    | secsi/masscan        | https://github.com/robertdavidgraham/masscan     |
| MassDNS                    | secsi/massdns        | https://github.com/blechschmidt/massdns          |
| nikto                      | secsi/nikto          | https://github.com/sullo/nikto                   |
| nmap                       | secsi/nmap           | https://github.com/nmap/nmap                     |
| oxml_xxe                   | secsi/oxml_xxe       | https://github.com/BuffaloWill/oxml_xxe          |
| Pagodo                     | secsi/pagodo         | https://github.com/opsdisk/pagodo                |
| photon                     | secsi/photon         | https://github.com/s0md3v/Photon                 |
| PivotSuite                 | secsi/pivotsuite     | https://github.com/RedTeamOperations/PivotSuite  |
| psalm                      | secsi/psalm          | https://github.com/vimeo/psalm                   |
| pureDNS                    | secsi/puredns        | https://github.com/d3mondev/puredns              |
| Race The Web               | secsi/race-the-web   | https://github.com/TheHackerDev/race-the-web     |
| RestfulHarvest             | secsi/restfulharvest | https://github.com/laramies/theHarvester         |
| Retire.js                  | secsi/retire         | https://github.com/RetireJS/retire.js            |
| RouterSploit               | secsi/routersploit   | https://github.com/threat9/routersploit          |
| Sandcastle                 | secsi/sandcastle     | https://github.com/0xSearches/sandcastle         |
| scanless                   | secsi/scanless       | https://github.com/vesche/scanless               |
| spyse.py                   | secsi/spysepy        | https://github.com/zeropwn/spyse.py              |
| sqlmap                     | secsi/sqlmap         | https://github.com/sqlmapproject/sqlmap          |
| Striker                    | secsi/striker        | https://github.com/s0md3v/Striker                |
| Subfinder                  | secsi/subfinder      | https://github.com/projectdiscovery/subfinder    |
| Subjack                    | secsi/subjack        | https://github.com/haccer/subjack                |
| Sublist3r                  | secsi/sublist3r      | https://github.com/aboul3la/Sublist3r            |
| theHarvester               | secsi/theharvester   | https://github.com/laramies/theHarvester         |
| WAFW00F                    | secsi/wafw00f        | https://github.com/EnableSecurity/wafw00f        |
| waybackpy                  | secsi/waybackpy      | https://github.com/akamhy/waybackpy              |
| WhatWeb                    | secsi/whatweb        | https://github.com/urbanadventurer/WhatWeb       |
| XXEinjector                | secsi/xxeinjector    | https://github.com/enjoiz/XXEinjector            |

## Tool Structure
Every tool in the tools directory contains **at least** two file:
- config.py
- Dockerfile.
- README.md (optional README for Docker Hub)

If you want to add a new tool you just have to create a folder for that specific tool inside the *tools* directory. In this folder you have to insert the *Dockerfile* with defined **build args** to customize and automate the build. Once you created the Dockerfile you have to create a *config.py* in the same directory with a function called *get_config(organization, common_args)*. Be careful: the function MUST be called this way and MUST have those two parameters (even if you do not use them). The returning value is the **config** for that specific tool and has the following structure:
```
config =  {
    'name': organization+'/<name_of_the_image>',
    'version': '', # Should be an helper function
    'buildargs': {
    },
    'tests': []
  }
```
The four keys are:
- **name**: the name of the Docker Image (e.g. secsi/<tool_name>);
- **version**: the version number of the Docker Image. For this you may use a helper function that **is able to retrieve the latest available version number** (look at *tools/ffuf* for an example);
- **buildargs**: a dict to specify the parts of the Docker Images that are subject to updates (again: look at *tools/ffuf* for an example);
- **tests**: an array of tests (usually just a simple one like '--help').

After doing so you are good to go! Just be careful that the **name** of the tool **MUST BE THE SAME** as the directory in which you placed its Dockerfile.

**There is a NAMING CONVENTION for the versions: use only DOTS and DIGITS; so please remove any trailing 'v' from the version in the specific config.py** (for a working example check **tools/dirsearch/config.py**).

## Helpers
To get the latest versions and information about **tools** and **base images** a set of helpers has been implemented. If you want to add a new tool you should use these helpers to have a Docker Image that is automatically updated by RAUDI.

### ``get_latest_pip_version``
This helper is used to retrieve the latest version of a **pip** package. All it takes is the name of the package and returns the **version number**. Example:
```
VERSION = helper.get_latest_pip_version(package_name)
```

### ``get_latest_npm_registry_version``
This helper is used to retrieve the latest version of a **npm** package. All it takes is the name of the package and returns the **version number**. Example:
```
VERSION = helper.get_latest_npm_registry_version(package_name)
```

### ``get_latest_github_release``
This helper is used to retrieve information about a GitHub repo that uses **Releases** and has multiple kind of assets (e.g. executables for different OSes). This helper takes the repo (in the format ``user/repo``) and a target string to be able to identify the correct asset to download. It returns a dict with two keys (**url** and **version**). Example:
```
VERSION = helper.get_latest_github_release("user/repo", "linux_amd64")
```

### ``get_latest_github_release_no_browser_download``
This helper is used to retrieve information about a GitHub repo that uses **Releases** and has only the source code (which means there is a **zipball** and a **tarball**). This helper takes the repo (in the format ``user/repo``) and returns a dict with two keys (**url** and **version**). Example:
```
VERSION = helper.get_latest_github_release_no_browser_download("user/repo")
```

### ``get_latest_github_tag_no_browser_download``
This helper is used to retrieve information about a GitHub repo that uses **Tags** and has only the source code (which means there is a **zipball** and a **tarball**). This helper takes the repo (in the format ``user/repo``) and returns a dict with two keys (**url** and **version**). Example:
```
VERSION = helper.get_latest_github_tag_no_browser_download("user/repo")
```

### ``get_latest_github_commit``
This helper is used to retrieve information about a GitHub repo that doesn't use **Tags** or **Releases**. In this case, the goal is to retrieve the **latest commit**. This helper takes the repo (in the format ``user/repo``) and returns a string representing the **date** of the last commit in the format ``YYYYYMMDD``.
```
VERSION = helper.get_latest_github_commit("user/repo")
```

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

## How to Pronounce
We are **italians**, so we probably pronounce it in a different manner than yours. The correct pronunciation (using the **phonetic transcription**) is the following:
```
/ˈraʊdi/
```
Otherwise think about the stuffed dog in the famous TV Show *Scrubs*: [Rowdy](https://tinyurl.com/raudi-pronunciation)

## Contributions
Everyone is invited to contribute!
We created a **very detailed** document to describe [how to contribute to RAUDI](https://github.com/cybersecsi/RAUDI/blob/main/CONTRIBUTING.md).

## Credits
RAUDI is proudly developed [@SecSI](https://secsi.io) by:
- [Angelo Delicato](https://github.com/thelicato)
- [Daniele Capone](https://github.com/daniele-capone)
- [Gaetano Perrone](https://github.com/giper45)

## License
**RAUDI** is an open-source and free software released under the [GNU GPL v3](https://github.com/cybersecsi/RAUDI/blob/main/LICENSE).