# hashID

## Official Documentation
Reference: https://github.com/psypanda/hashID

## Description
Identify the different types of hashes used to encrypt data and especially passwords.

This replaces [hash-identifier](http://code.google.com/p/hash-identifier/), which is outdated!

hashID is a tool written in Python 3 which supports the identification of over 220 unique hash types using regular expressions. A detailed list of supported hashes can be found [here](https://github.com/psypanda/hashID/blob/master/doc/HASHINFO.xlsx).

It is able to identify a single hash, parse a file or read multiple files in a directory and identify the hashes within them. hashID is also capable of including the corresponding [hashcat](https://hashcat.net/oclhashcat/) mode and/or [JohnTheRipper](http://www.openwall.com/john/) format in its output.

hashID works out of the box with Python 2 ≥ 2.7.x or Python 3 ≥ 3.3 on any platform.

## Usage
```
docker run -it --rm secsi/hashid
```

## 🐳 RAUDI: Regularly and Automatically Updated Docker Images

Hello, friend. This Docker Image has been created by RAUDI. What is RAUDI?

**RAUDI** (Regularly and Automatically Updated Docker Images) automatically generates and keep updated a series of *Docker Images* through *GitHub Actions* for tools that are not provided by the developers.

**RAUDI** is what will save you from creating and managing a lot of Docker Images manually. Every time a software is updated you need to update the Docker Image if you want to use the latest features, the dependencies are not working anymore. 

This is messy and time-consuming. 

Don't worry anymore, we got you covered.

If you want to contribute, give us a star or take a quick look at the source code of **RAUDI** click [here](https://github.com/cybersecsi/RAUDI).