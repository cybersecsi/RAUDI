# puredns

## Official Documentation
Reference: https://github.com/d3mondev/puredns
## Description

**puredns** is a fast domain resolver and subdomain bruteforcing tool that can accurately filter out wildcard subdomains and DNS poisoned entries.

It uses massdns, a powerful stub DNS resolver, to perform bulk lookups. With the proper bandwidth and a good list of public resolvers, it can resolve millions of queries in just a few minutes. Unfortunately, the results from massdns are only as good as the answers provided by the public resolvers. The results are often polluted by wrong DNS answers and false positives from wildcard subdomains.

puredns solves this with its wildcard detection algorithm. It can filter out wildcards based on the DNS answers obtained from a set of trusted resolvers. It also attempts to work around DNS poisoning by validating the answers obtained using those trusted resolvers.



## Usage

```
docker run -it --rm -v <host_folder>:/current secsi/puredns
```  
You should download `resolvers.txt` and `<subdomains_file>` in the `host` folder to use `puredns`. See the documentation for more details.  



## 🐳 RAUDI: Regularly and Automatically Updated Docker Images

Hello, friend. This Docker Image has been created by RAUDI. What is RAUDI?

**RAUDI** (Regularly and Automatically Updated Docker Images) automatically generates and keep updated a series of *Docker Images* through *GitHub Actions* for tools that are not provided by the developers.

**RAUDI** is what will save you from creating and managing a lot of Docker Images manually. Every time a software is updated you need to update the Docker Image if you want to use the latest features, the dependencies are not working anymore. 

This is messy and time-consuming. 

Don't worry anymore, we got you covered.

If you want to contribute, give us a star or take a quick look at the source code of **RAUDI** click [here](https://github.com/cybersecsi/RAUDI).