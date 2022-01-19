# LinkFinder

## Official Documentation
Reference: https://github.com/GerbenJavado/LinkFinder

## Description
```
docker run -it --rm -v <output_dir>:/linkfinder/output secsi/linkfinder -i <target_url> -o /linkfinder/output/output.html
```

## Usage
LinkFinder is a python script written to discover endpoints and their parameters in JavaScript files. This way penetration testers and bug hunters are able to gather new, hidden endpoints on the websites they are testing. Resulting in new testing ground, possibility containing new vulnerabilities. It does so by using [jsbeautifier](https://github.com/beautify-web/js-beautify) for python in combination with a fairly large regular expression. The regular expressions consists of four small regular expressions. These are responsible for finding:

- Full URLs (`https://example.com/*`)
- Absolute URLs or dotted URLs (`/\*` or `../*`)
- Relative URLs with at least one slash (`text/test.php`)
- Relative URLs without a slash (`test.php`)

## 🐳 RAUDI: Regularly and Automatically Updated Docker Images

Hello, friend. This Docker Image has been created by RAUDI. What is RAUDI?

**RAUDI** (Regularly and Automatically Updated Docker Images) automatically generates and keep updated a series of *Docker Images* through *GitHub Actions* for tools that are not provided by the developers.

**RAUDI** is what will save you from creating and managing a lot of Docker Images manually. Every time a software is updated you need to update the Docker Image if you want to use the latest features, the dependencies are not working anymore. 

This is messy and time-consuming. 

Don't worry anymore, we got you covered.

If you want to contribute, give us a star or take a quick look at the source code of **RAUDI** click [here](https://github.com/cybersecsi/RAUDI).