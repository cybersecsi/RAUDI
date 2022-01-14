ARG RUBY2_ALPINE_VERSION

FROM ruby:2.3.8-slim
WORKDIR /code

ARG DOWNLOAD_URL

RUN apt update && apt install -y git openssl bash curl tar &&  git clone $DOWNLOAD_URL /code && \
    curl --insecure https://raw.githubusercontent.com/rvm/rvm/master/binscripts/rvm-installer | bash && \
    bash install.sh

ENV PATH /usr/local/rvm/bin:$PATH

EXPOSE 80 443 8080 8443

ENTRYPOINT ["bash", "start.sh"]