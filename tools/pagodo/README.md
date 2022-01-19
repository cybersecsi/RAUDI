# pagodo

## Official Documentation
Reference: https://github.com/opsdisk/pagodo

## Description
pagodo automates Google searching for potentially vulnerable web pages and applications on the Internet. It replaces manually performing Google dork searches with a web GUI browser.

There are 2 parts. The first is ghdb_scraper.py that retrieves the latest Google dorks and the second portion is pagodo.py that leverages the information gathered by ghdb_scraper.py.

## Usage
```
docker run -it --rm secsi/pagodo
```

## 🐳 RAUDI: Regularly and Automatically Updated Docker Images

Hello, friend. This Docker Image has been created by RAUDI. What is RAUDI?

**RAUDI** (Regularly and Automatically Updated Docker Images) automatically generates and keep updated a series of *Docker Images* through *GitHub Actions* for tools that are not provided by the developers.

**RAUDI** is what will save you from creating and managing a lot of Docker Images manually. Every time a software is updated you need to update the Docker Image if you want to use the latest features, the dependencies are not working anymore. 

This is messy and time-consuming. 

Don't worry anymore, we got you covered.

If you want to contribute, give us a star or take a quick look at the source code of **RAUDI** click [here](https://github.com/cybersecsi/RAUDI).