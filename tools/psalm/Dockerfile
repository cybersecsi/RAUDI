ARG PHP_ALPINE_VERSION
FROM php:$PHP_ALPINE_VERSION 
# FROM php:dd$PHP_ALPINE_VERSION AS builder
# COPY --from=hyperized/prestissimo:latest /usr/bin/composer /usr/bin/composer
WORKDIR /code

ARG DOWNLOAD_URL
ADD $DOWNLOAD_URL phar.tar.gz
RUN tar -xvf phar.tar.gz -C /code --strip-components=1 
ENTRYPOINT ["/code/psalm.phar"]