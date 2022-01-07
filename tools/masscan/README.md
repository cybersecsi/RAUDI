# MASSCAN

## Official Documentation
Reference: https://github.com/robertdavidgraham/masscan

## Description

**MASSCAN** is an Internet-scale port scanner. It can scan the entire Internet
in under 5 minutes, transmitting 10 million packets per second,
from a single machine.

Its usage (parameters, output) is similar to `nmap`, the most famous port scanner.
When in doubt, try one of those features -- features that support widespread
scanning of many machines are supported, while in-depth scanning of single
machines aren't.

Internally, it uses asynchronous transmission, similar to port scanners
like  `scanrand`, `unicornscan`, and `ZMap`. It's more flexible, allowing
arbitrary port and address ranges.

NOTE: masscan uses its own **ad hoc TCP/IP stack**. Anything other than
simple port scans may cause conflict with the local TCP/IP stack. This means you 
need to use either the `--src-ip` option to run from a different IP address, or
use `--src-port` to configure which source ports masscan uses, then also
configure the internal firewall (like `pf` or `iptables`) to firewall those ports
from the rest of the operating system.

## Usage
```
docker run -it --rm secsi/masscan -p<port> <target_ip_address>
```

## 🐳 RAUDI: Regularly and Automatically Updated Docker Images

Hello, friend. This Docker Image has been created by RAUDI. What is RAUDI?

**RAUDI** (Regularly and Automatically Updated Docker Images) automatically generates and keep updated a series of *Docker Images* through *GitHub Actions* for tools that are not provided by the developers.

**RAUDI** is what will save you from creating and managing a lot of Docker Images manually. Every time a software is updated you need to update the Docker Image if you want to use the latest features, the dependencies are not working anymore. 

This is messy and time-consuming. 

Don't worry anymore, we got you covered.

If you want to contribute, give us a star or take a quick look at the source code of **RAUDI** click [here](https://github.com/cybersecsi/RAUDI).