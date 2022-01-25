# SecLists

## Official Documentation
Reference: https://github.com/danielmiessler/SecLists

## Description
SecLists is the security tester's companion. It's a collection of multiple types of lists used during security assessments, collected in one place. List types include usernames, passwords, URLs, sensitive data patterns, fuzzing payloads, web shells, and many more. The goal is to enable a security tester to pull this repository onto a new testing box and have access to every type of list that may be needed.



## Usage  
Run in daemon mode:   
```   
docker run -d --name seclists --rm secsi/seclists  
```  
This will create a VOLUME of `/usr/share/wordlists` folder. 
Now you can easy use it in other containers by binding the volume:   
```   
docker run --rm -it --volumes-from seclists ubuntu bash  
ls /usr/share/wordlists/SecLists

```

## 🐳 RAUDI: Regularly and Automatically Updated Docker Images

Hello, friend. This Docker Image has been created by RAUDI. What is RAUDI?

**RAUDI** (Regularly and Automatically Updated Docker Images) automatically generates and keep updated a series of *Docker Images* through *GitHub Actions* for tools that are not provided by the developers.

**RAUDI** is what will save you from creating and managing a lot of Docker Images manually. Every time a software is updated you need to update the Docker Image if you want to use the latest features, the dependencies are not working anymore. 

This is messy and time-consuming. 

Don't worry anymore, we got you covered.

If you want to contribute, give us a star or take a quick look at the source code of **RAUDI** click [here](https://github.com/cybersecsi/RAUDI).