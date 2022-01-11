
# GitTools

## Official Documentation
Reference: https://github.com/internetwache/GitTools

## Description
### Finder
You can use this tool to find websites with their .git repository available to the public

### Dumper
This tool can be used to download as much as possible from the found .git repository from webservers which do not have directory listing enabled.

### Extractor
A small bash script to extract commits and their content from a broken repository.

This script tries to recover incomplete git repositories:

Iterate through all commit-objects of a repository
Try to restore the contents of the commit
Commits are not sorted by date

## Usage

Finder
```
docker run --rm -ti -v <local_dir>:/tmp/gittools -w /tmp/gittools secsi/gittools gitfinder -i <inputfile> -o <outputfile>
```

Dumper
```
docker run --rm -ti -v <local_dir>:/tmp/gittools -w /tmp/gittools secsi/gittools gitdumper http://target.tld/.git/ .
```

Extractor
```
docker run --rm -ti -v <local_dir>:/tmp/gittools -w /tmp/gittools secsi/gittools extractor <mygitrepo> <mygitrepodump>
```

## 🐳 RAUDI: Regularly and Automatically Updated Docker Images

Hello, friend. This Docker Image has been created by RAUDI. What is RAUDI?

**RAUDI** (Regularly and Automatically Updated Docker Images) automatically generates and keep updated a series of *Docker Images* through *GitHub Actions* for tools that are not provided by the developers.

**RAUDI** is what will save you from creating and managing a lot of Docker Images manually. Every time a software is updated you need to update the Docker Image if you want to use the latest features, the dependencies are not working anymore. 

This is messy and time-consuming. 

Don't worry anymore, we got you covered.

If you want to contribute, give us a star or take a quick look at the source code of **RAUDI** click [here](https://github.com/cybersecsi/RAUDI).