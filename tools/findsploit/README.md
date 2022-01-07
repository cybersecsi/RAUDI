# Findsploit

## Official Documentation
Reference: https://github.com/1N3/Findsploit
## Description

Finsploit is a simple bash script to quickly and easily search both local and online exploit databases.

## Usage
Here is the full usage of ``findsploit``:

```
Search for all exploits and modules using a single search term:
*  docker run -it --rm secsi/findsploit <search_term_1> (ie. findsploit apache)

Search multiple search terms:
*  docker run -it --rm secsi/findsploit <search_term_1> <search_term_2> <search_term_3> ...

Show all NMap scripts:
*  docker run -it --rm secsi/findsploit nmap 

Search for all FTP NMap scripts:
*  docker run -it --rm secsi/findsploit nmap | grep ftp

Show all Metasploit auxiliary modules:
*  docker run -it --rm secsi/findsploit auxiliary

Show all Metasploit exploits:
*  docker run -it --rm secsi/findsploit exploits

Show all Metasploit encoder modules:
*  docker run -it --rm secsi/findsploit encoder

Show all Metasploit payloads modules:
*  docker run -it --rm secsi/findsploit payloads

Search all Metasploit payloads for windows only payloads:
*  docker run -it --rm secsi/findsploit payloads | grep windows
```

## 🐳 RAUDI: Regularly and Automatically Updated Docker Images

Hello, friend. This Docker Image has been created by RAUDI. What is RAUDI?

**RAUDI** (Regularly and Automatically Updated Docker Images) automatically generates and keep updated a series of *Docker Images* through *GitHub Actions* for tools that are not provided by the developers.

**RAUDI** is what will save you from creating and managing a lot of Docker Images manually. Every time a software is updated you need to update the Docker Image if you want to use the latest features, the dependencies are not working anymore. 

This is messy and time-consuming. 

Don't worry anymore, we got you covered.

If you want to contribute, give us a star or take a quick look at the source code of **RAUDI** click [here](https://github.com/cybersecsi/RAUDI).