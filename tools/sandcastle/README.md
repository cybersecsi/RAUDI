# Sandcastle

## Official Documentation
Reference: https://github.com/0xSearches/sandcastle

## Description

**Sandcastle** is a Python script for AWS S3 bucket enumeration, formerly known as bucketCrawler.

The script takes a target's name as the stem argument (e.g. `shopify`) and iterates through a file of bucket name permutations, such as the ones below:

```
-training
-bucket
-dev
-attachments
-photos
-elasticsearch
[...]
```

## Usage
```
docker run -it --rm secsi/sandcastle -t <targetStem> -f bucket-names.txt

docker run -it --rm -v <local_bucket_names>:<container_bucket_names> secsi/sandcastle -t <targetStem> -f <container_bucket_names>
```

## 🐳 RAUDI: Regularly and Automatically Updated Docker Images

Hello, friend. This Docker Image has been created by RAUDI. What is RAUDI?

**RAUDI** (Regularly and Automatically Updated Docker Images) automatically generates and keep updated a series of *Docker Images* through *GitHub Actions* for tools that are not provided by the developers.

**RAUDI** is what will save you from creating and managing a lot of Docker Images manually. Every time a software is updated you need to update the Docker Image if you want to use the latest features, the dependencies are not working anymore. 

This is messy and time-consuming. 

Don't worry anymore, we got you covered.

If you want to contribute, give us a star or take a quick look at the source code of **RAUDI** click [here](https://github.com/cybersecsi/RAUDI).