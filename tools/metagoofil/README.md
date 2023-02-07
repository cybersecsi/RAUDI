# Metagoofil

## Official Documentation
Reference: https://github.com/opsdisk/metagoofil

## Description
metagoofil searches Google for specific types of files being publicly hosted on a web site and optionally downloads them to your local box.  This is useful for Open Source Intelligence gathering, penetration tests, or determining what files your organization is leaking to search indexers like Google.  As an example, it uses the Google query below to find all the `.pdf` files being hosted on `example.com` and optionally downloads a local copy.

```none
site:example.com filetype:pdf
```

## Usage
Here is the command to run **metagoofil** on a URL:
```bash
# This will save the files in your current directory.
docker run -v $PWD:/output secsi/metagoofil -d kali.org -t pdf
```

## 🐳 RAUDI: Regularly and Automatically Updated Docker Images

Hello, friend. This Docker Image has been created by RAUDI. What is RAUDI?

**RAUDI** (Regularly and Automatically Updated Docker Images) automatically generates and keep updated a series of *Docker Images* through *GitHub Actions* for tools that are not provided by the developers.

**RAUDI** is what will save you from creating and managing a lot of Docker Images manually. Every time a software is updated you need to update the Docker Image if you want to use the latest features, the dependencies are not working anymore. 

This is messy and time-consuming. 

Don't worry anymore, we got you covered.

If you want to contribute, give us a star or take a quick look at the source code of **RAUDI** click [here](https://github.com/cybersecsi/RAUDI).