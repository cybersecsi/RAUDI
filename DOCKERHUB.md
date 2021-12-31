# 🐳 HOUDINI: Hacking Offensive Updated Docker Images for Network Intrusion

Hello, friend. That's the right page, you are not mistaken. This Docker Image has been created by HOUDINI. What is HOUDINI?

**HOUDINI** (Hacking Offensive Updated Docker Images for Network Intrusion) automatically generates *Docker Images* for Network Security-related tools that are not provided by the developers. The Images are automatically updated through the GitHub Actions.

[![Documentation](https://img.shields.io/badge/Documentation-complete-green.svg?style=flat)](https://github.com/cybersecsi/HOUDINI/blob/main/README.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/cybersecsi/HOUDINI/blob/main/LICENSE.md)

## What is HOUDINI
**HOUDINI** is what will save you from creating and managing a lot of Docker Images manually. Every time a software is updated you need to update the Docker Image if you want to use the latest features, the dependencies are not working anymore. 

This is messy and time-consuming. 

Don't worry anymore, we got you covered.

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

## General Usage
For **every** image created by HOUDINI you may use it with the following syntax:
```
docker run -it --rm secsi/<tool> <command>
```

For some tools (like dirb, fuff and so on) you may need to mount a folder with all your wordlists or other assets (we do not provide the assets inside the containers to have lightweight images). Here is an example with *dirb*:
```
docker run -it --rm -v <wordlist_src_dir>:<wordlist_container_dir> secsi/dirb <url> <wordlist_container_dir>/<wordlist_file>
```

## Contributions
Everyone is invited to contribute!
If you are a user of the tool and have a suggestion for a new feature or a bug to report, please do so through the issue tracker.

## Credits
Developed by Angelo Delicato [@SecSI](https://secsi.io)

## License
**HOUDINI** is an open-source and free software released under the [MIT License](/LICENSE).