# ffuf

## Official Documentation
Reference: https://github.com/ffuf/ffuf
## Description
A fast web fuzzer written in Go.

## Usage
The usage examples below show just the simplest tasks you can accomplish using ``ffuf``:
```
docker run -it --rm -v <wordlist_src_dir>:<wordlist_container_dir> secsi/ffuf -w </path/to/wordlist> -u <target_url>
```

## 🐳 RAUDI: Regularly and Automatically Updated Docker Images

Hello, friend. This Docker Image has been created by RAUDI. What is RAUDI?

**RAUDI** (Regularly and Automatically Updated Docker Images) automatically generates and keep updated a series of *Docker Images* through *GitHub Actions* for tools that are not provided by the developers.

**RAUDI** is what will save you from creating and managing a lot of Docker Images manually. Every time a software is updated you need to update the Docker Image if you want to use the latest features, the dependencies are not working anymore. 

This is messy and time-consuming. 

Don't worry anymore, we got you covered.

If you want to contribute, give us a star or take a quick look at the source code of **RAUDI** click [here](https://github.com/cybersecsi/RAUDI).