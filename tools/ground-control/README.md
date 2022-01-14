# Ground control

## Official Documentation
Reference: https://github.com/jobertabma/ground-control

## Description
This is a collection of most of my scripts that I use to debug Server Side Request Forgery (SSRF), blind XSS, and insecure XXE processing vulnerabilities. This is still a work in progress, as I'm still collecting all the scripts that I have lingering around. Before using these scripts, I used to rewrite these scripts most of the time or set up listeners with netcat. That wasn't scalable, so I started collecting the scripts in a repository, which can be closed easily every time it's needed it on a server.
DOCX/XLSX/PPTX
ODT/ODG/ODP/ODS
SVG
XML
PDF (experimental)
JPG (experimental)
GIF (experimental)

## Usage
1. Start server
```
docker run -ti --rm -p 80:80 -p 443:443 -p 8080:8080 -p 8443:8443 secsi/ground-control
```

2. Use server!
```
curl -vv "http://localhost/redirect?url=http://169.254.169.254/latest/meta-data/"
curl -vv "http://localhost/ping_pong?body=%3ch1%3eHello%3c/h1%3e"
```
## 🐳 RAUDI: Regularly and Automatically Updated Docker Images

Hello, friend. This Docker Image has been created by RAUDI. What is RAUDI?

**RAUDI** (Regularly and Automatically Updated Docker Images) automatically generates and keep updated a series of *Docker Images* through *GitHub Actions* for tools that are not provided by the developers.

**RAUDI** is what will save you from creating and managing a lot of Docker Images manually. Every time a software is updated you need to update the Docker Image if you want to use the latest features, the dependencies are not working anymore. 

This is messy and time-consuming. 

Don't worry anymore, we got you covered.

If you want to contribute, give us a star or take a quick look at the source code of **RAUDI** click [here](https://github.com/cybersecsi/RAUDI).