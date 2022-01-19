# Crowbar

## Official Documentation
Reference: https://github.com/galkan/crowbar

## Description
Crowbar (formally known as Levye) is a brute forcing tool that can be used during penetration tests. It was developed to brute force some protocols in a different manner according to other popular brute forcing tools. As an example, while most brute forcing tools use username and password for SSH brute force, Crowbar uses SSH key(s). This allows for any private keys that have been obtained during penetration tests, to be used to attack other SSH servers.

## Usage
```
docker run -it --rm secsi/crowbar
```

## 🐳 RAUDI: Regularly and Automatically Updated Docker Images

Hello, friend. This Docker Image has been created by RAUDI. What is RAUDI?

**RAUDI** (Regularly and Automatically Updated Docker Images) automatically generates and keep updated a series of *Docker Images* through *GitHub Actions* for tools that are not provided by the developers.

**RAUDI** is what will save you from creating and managing a lot of Docker Images manually. Every time a software is updated you need to update the Docker Image if you want to use the latest features, the dependencies are not working anymore. 

This is messy and time-consuming. 

Don't worry anymore, we got you covered.

If you want to contribute, give us a star or take a quick look at the source code of **RAUDI** click [here](https://github.com/cybersecsi/RAUDI).