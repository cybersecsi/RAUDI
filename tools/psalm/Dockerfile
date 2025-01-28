ARG PHP_ALPINE_VERSION
FROM php:$PHP_ALPINE_VERSION 

WORKDIR /code

ARG DOWNLOAD_URL
ADD $DOWNLOAD_URL phar.tar.gz
RUN tar -xvf phar.tar.gz -C /code --strip-components=1 
ENTRYPOINT ["/code/psalm.phar"]