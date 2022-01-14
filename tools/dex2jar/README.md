# dex2jar

## Official Documentation
Reference: https://github.com/pxb1988/dex2jar

## Description
Tools to work with android .dex and java .class files

1. dex-reader/writer: Read/write the Dalvik Executable (.dex) file. It has a light weight API similar with ASM.
2. d2j-dex2jar: Convert .dex file to .class files (zipped as jar)
3. smali/baksmali: disassemble dex to smali files and assemble dex from smali files. different implementation to smali/baksmali, same syntax, but we support escape in type desc "Lcom/dex2jar\t\u1234;"
4. other tools: d2j-decrypt-string
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