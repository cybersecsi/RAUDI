# Base Distro Arg
ARG LAST_UBUNTU_VERSION

FROM ubuntu:$LAST_UBUNTU_VERSION

# Build Args
ARG FFUF_DOWNLOAD_URL

# Content
RUN apt-get update
ADD $FFUF_DOWNLOAD_URL ffuf.tar.gz
RUN tar xzvf ffuf.tar.gz && chmod +x ffuf && mv ffuf /bin
ENTRYPOINT ["ffuf"]