# dvcs-ripper

## Official Documentation
Reference: https://github.com/kost/dvcs-ripper

## Description
Rip web accessible (distributed) version control systems: SVN, GIT, Mercurial/hg, bzr, ...

It can rip repositories even when directory browsing is turned off.

Make sure to position yourself in empty directory where you want repositories to be downloaded/cloned.

## Usage

rip-bzr.pl
```
docker run -it --rm secsi/dvcs-ripper rip-bzr -h
```
rip-cvs.pl
```
docker run -it --rm secsi/dvcs-ripper rip-cvd -h
```

rip-git.pl
```
docker run -it --rm secsi/dvcs-ripper rip-git -h
```

rip-hg.pl
```
docker run -it --rm secsi/dvcs-ripper rip-hg -h
```

rip-svn.pl
```
docker run -it --rm secsi/dvcs-ripper rip-svn -h
```

## 🐳 RAUDI: Regularly and Automatically Updated Docker Images

Hello, friend. This Docker Image has been created by RAUDI. What is RAUDI?

**RAUDI** (Regularly and Automatically Updated Docker Images) automatically generates and keep updated a series of *Docker Images* through *GitHub Actions* for tools that are not provided by the developers.

**RAUDI** is what will save you from creating and managing a lot of Docker Images manually. Every time a software is updated you need to update the Docker Image if you want to use the latest features, the dependencies are not working anymore. 

This is messy and time-consuming. 

Don't worry anymore, we got you covered.

If you want to contribute, give us a star or take a quick look at the source code of **RAUDI** click [here](https://github.com/cybersecsi/RAUDI).