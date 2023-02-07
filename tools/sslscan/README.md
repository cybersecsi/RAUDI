# sslscan2

## Official Documentation
Reference: https://github.com/rbsec/sslscan

## Description
sslscan tests SSL/TLS enabled services to discover supported cipher suites. The following features are provided:
 - Enumeration of server key exchange groups.
 - Enumeration of server signature algorithms.
 - SSLv2 and SSLv3 protocol support is scanned, but individual ciphers are not.
 - A test suite is included using Docker, to verify that sslscan is functionality correctly.
 - Removed the --http option, as it was broken and had very little use in the first place.

## Usage
```bash
docker run -it --rm secsi/sslscan --help
```

## 🐳 RAUDI: Regularly and Automatically Updated Docker Images

Hello, friend. This Docker Image has been created by RAUDI. What is RAUDI?

**RAUDI** (Regularly and Automatically Updated Docker Images) automatically generates and keep updated a series of *Docker Images* through *GitHub Actions* for tools that are not provided by the developers.

**RAUDI** is what will save you from creating and managing a lot of Docker Images manually. Every time a software is updated you need to update the Docker Image if you want to use the latest features, the dependencies are not working anymore. 

This is messy and time-consuming. 

Don't worry anymore, we got you covered.

If you want to contribute, give us a star or take a quick look at the source code of **RAUDI** click [here](https://github.com/cybersecsi/RAUDI).