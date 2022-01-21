# Base Distro Arg
FROM debian:10-slim

RUN apt update && apt -y  install curl gnupg
RUN curl http://download.netify.ai/netify/ubuntu/apt-gpg-key-netify.asc -o Netify.gpg
RUN apt-key add - < Netify.gpg
RUN echo 'deb http://download.netify.ai/netify/debian/10/ /' > /tmp/netify.list
RUN mv /tmp/netify.list /etc/apt/sources.list.d/netify.list
RUN apt update && apt -y install netifyd
ENTRYPOINT ["netifyd"]