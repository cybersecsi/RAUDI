# spidy

## Official Documentation
Reference: https://github.com/rivermont/spidy

## Description
Spidy (/spˈɪdi/) is the simple, easy to use command line web crawler.
Given a list of web links, it uses Python requests to query the webpages, and lxml to extract all links from the page.
Pretty simple!


## Usage
``` 
docker run --rm -it -v $PWD:/input -v $PWD:/data spidy
``` 
You need to setup a configuration file that you can find in [config](https://github.com/rivermont/spidy/tree/master/spidy/config) folder: 

## 🐳 RAUDI: Regularly and Automatically Updated Docker Images

Hello, friend. This Docker Image has been created by RAUDI. What is RAUDI?

**RAUDI** (Regularly and Automatically Updated Docker Images) automatically generates and keep updated a series of *Docker Images* through *GitHub Actions* for tools that are not provided by the developers.

**RAUDI** is what will save you from creating and managing a lot of Docker Images manually. Every time a software is updated you need to update the Docker Image if you want to use the latest features, the dependencies are not working anymore. 

This is messy and time-consuming. 

Don't worry anymore, we got you covered.

If you want to contribute, give us a star or take a quick look at the source code of **RAUDI** click [here](https://github.com/cybersecsi/RAUDI).