# DataSploit

## Official Documentation
Reference: https://github.com/DataSploit/datasploit

## Description
- Performs OSINT on a domain / email / username / phone and find out information from different sources.
- Correlate and collaborate the results, show them in a consolidated manner.
- Tries to find out credentials, api-keys, tokens, subdomains, domain history, legacy portals, etc. related to the target.
- Use specific script / launch automated OSINT for consolidated data.
- Performs Active Scans on collected data.
- Generates HTML, JSON reports along with text files.
## Usage
1. Create and configure your api key in config.py, sample can be found [here](https://github.com/DataSploit/datasploit/blob/master/config_sample.py).
2. Use tool!
```
docker run --rm -ti -v ~/config.py:/datasploit/config.py secsi/datasploit -i domain.com
```

## 🐳 RAUDI: Regularly and Automatically Updated Docker Images

Hello, friend. This Docker Image has been created by RAUDI. What is RAUDI?

**RAUDI** (Regularly and Automatically Updated Docker Images) automatically generates and keep updated a series of *Docker Images* through *GitHub Actions* for tools that are not provided by the developers.

**RAUDI** is what will save you from creating and managing a lot of Docker Images manually. Every time a software is updated you need to update the Docker Image if you want to use the latest features, the dependencies are not working anymore. 

This is messy and time-consuming. 

Don't worry anymore, we got you covered.

If you want to contribute, give us a star or take a quick look at the source code of **RAUDI** click [here](https://github.com/cybersecsi/RAUDI).