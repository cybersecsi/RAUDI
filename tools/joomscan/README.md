# joomscan

## Official Documentation
Reference: https://github.com/OWASP/joomscan

## Description
**OWASP Joomla! Vulnerability Scanner (JoomScan)** is an open source project, developed with the aim of automating the task of vulnerability detection and reliability assurance in Joomla CMS deployments. Implemented in Perl, this tool enables seamless and effortless scanning of Joomla installations, while leaving a minimal footprint with its lightweight and modular architecture. It not only detects known offensive vulnerabilities, but also is able to detect many misconfigurations and admin-level shortcomings that can be exploited by adversaries to compromise the system. Furthermore, OWASP JoomScan provides a user-friendly interface and compiles the final reports in both text and HTML formats for ease of use and minimization of reporting overheads.

## Usage
```
docker run -it --rm -v <local_dir>:/joomscan/reports secsi/joomscan -u <target_url>
```

## 🐳 RAUDI: Regularly and Automatically Updated Docker Images

Hello, friend. This Docker Image has been created by RAUDI. What is RAUDI?

**RAUDI** (Regularly and Automatically Updated Docker Images) automatically generates and keep updated a series of *Docker Images* through *GitHub Actions* for tools that are not provided by the developers.

**RAUDI** is what will save you from creating and managing a lot of Docker Images manually. Every time a software is updated you need to update the Docker Image if you want to use the latest features, the dependencies are not working anymore. 

This is messy and time-consuming. 

Don't worry anymore, we got you covered.

If you want to contribute, give us a star or take a quick look at the source code of **RAUDI** click [here](https://github.com/cybersecsi/RAUDI).