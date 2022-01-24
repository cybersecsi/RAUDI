# XSStrike

## Official Documentation
Reference: https://github.com/s0md3v/XSStrike

## Description
XSStrike is a Cross Site Scripting detection suite equipped with four hand written parsers, an intelligent payload generator, a powerful fuzzing engine and an incredibly fast crawler.

Instead of injecting payloads and checking it works like all the other tools do, XSStrike analyses the response with multiple parsers and then crafts payloads that are guaranteed to work by context analysis integrated with a fuzzing engine.

## Usage
```
docker run -it --rm secsi/xsstrike
```

## 🐳 RAUDI: Regularly and Automatically Updated Docker Images

Hello, friend. This Docker Image has been created by RAUDI. What is RAUDI?

**RAUDI** (Regularly and Automatically Updated Docker Images) automatically generates and keep updated a series of *Docker Images* through *GitHub Actions* for tools that are not provided by the developers.

**RAUDI** is what will save you from creating and managing a lot of Docker Images manually. Every time a software is updated you need to update the Docker Image if you want to use the latest features, the dependencies are not working anymore. 

This is messy and time-consuming. 

Don't worry anymore, we got you covered.

If you want to contribute, give us a star or take a quick look at the source code of **RAUDI** click [here](https://github.com/cybersecsi/RAUDI).