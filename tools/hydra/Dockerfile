# Base Distro Arg
ARG LAST_UBUNTU_VERSION

FROM ubuntu:$LAST_UBUNTU_VERSION
RUN apt-get update && apt-get install -y hydra
ENTRYPOINT ["hydra"]