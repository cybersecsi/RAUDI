# dirhunt

## Official Documentation
Reference: https://github.com/Nekmo/dirhunt
## Description
Dirhunt is a web crawler optimize for **search and analyze directories**. This tool can find interesting things if the
server has the *"index of"* mode enabled. Dirhunt is also useful if the directory listing is not enabled. It detects
directories with **false 404 errors**, directories where an **empty index file** has been created to hide things and
much more.

Dirhunt does not use brute force. But neither is it just a **crawler**. This tool is faster than others because it
minimizes requests to the server. Generally, this tool takes **between 5-30 seconds**, depending on the website and
the server.

## Usage
Here is the command to run **dirhunt** on a URL:
```
docker run -it --rm secsi/dirhunt <url>
```

## 🐳 RAUDI: Regularly and Automatically Updated Docker Images

Hello, friend. This Docker Image has been created by RAUDI. What is RAUDI?

**RAUDI** (Regularly and Automatically Updated Docker Images) automatically generates and keep updated a series of *Docker Images* through *GitHub Actions* for tools that are not provided by the developers.

**RAUDI** is what will save you from creating and managing a lot of Docker Images manually. Every time a software is updated you need to update the Docker Image if you want to use the latest features, the dependencies are not working anymore. 

This is messy and time-consuming. 

Don't worry anymore, we got you covered.

If you want to contribute, give us a star or take a quick look at the source code of **RAUDI** click [here](https://github.com/cybersecsi/RAUDI).