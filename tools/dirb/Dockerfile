# Base Distro Arg
ARG LATEST_UBUNTU_VERSION

FROM ubuntu:$LATEST_UBUNTU_VERSION
RUN apt-get update && apt-get install -y dirb
ENTRYPOINT ["dirb"]