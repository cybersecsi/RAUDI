# Impacket

## Official Documentation
Reference: https://github.com/SecureAuthCorp/impacket

## Description
**Impacket** is a collection of Python classes for working with network protocols. Impacket is focused on providing low-level programmatic access to the packets and for some protocols (e.g. SMB1-3 and MSRPC) the protocol implementation itself. Packets can be constructed from scratch, as well as parsed from raw data, and the object oriented API makes it simple to work with deep hierarchies of protocols. The library provides a set of tools as examples of what can be done within the context of this library.

## Usage
To run the image: 
``` 
docker run -it --rm --name impacket secsi/impacket  
```  
A `sh` shell is opened. Now you can use the impacket scripts. 
If you want to use `impacket` classes with your code you can bind the current volume with the image:  

``` 
docker run -v `pwd`:/code -it --rm --name impacket secsi/impacket  
```  

All your code is present in `/code` folder.

## 🐳 RAUDI: Regularly and Automatically Updated Docker Images

Hello, friend. This Docker Image has been created by RAUDI. What is RAUDI?

**RAUDI** (Regularly and Automatically Updated Docker Images) automatically generates and keep updated a series of *Docker Images* through *GitHub Actions* for tools that are not provided by the developers.

**RAUDI** is what will save you from creating and managing a lot of Docker Images manually. Every time a software is updated you need to update the Docker Image if you want to use the latest features, the dependencies are not working anymore. 

This is messy and time-consuming. 

Don't worry anymore, we got you covered.

If you want to contribute, give us a star or take a quick look at the source code of **RAUDI** click [here](https://github.com/cybersecsi/RAUDI).