# No Base Distro Arg
FROM debian:10-slim

ARG KEY_URL

ADD $KEY_URL Netify.gpg

RUN apt update && apt -y  install gnupg \
    && apt-key add - < Netify.gpg \
    && echo 'deb http://download.netify.ai/netify/debian/10/ /' > /tmp/netify.list \
    && mv /tmp/netify.list /etc/apt/sources.list.d/netify.list \
    && apt update \
    && apt -y install netifyd \
    && apt-get clean \
    && rm -fr /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENTRYPOINT ["netifyd"]