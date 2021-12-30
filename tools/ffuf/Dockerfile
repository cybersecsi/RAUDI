# Base Distro Arg
ARG LAST_UBUNTU_VERSION

FROM ubuntu:$LAST_UBUNTU_VERSION

# Build Args
ARG FFUF_DOWNLOAD_URL

# Content
RUN apt-get update && apt-get install -y p7zip-full wget git
RUN wget $FFUF_DOWNLOAD_URL -O ffuf.tar.gz
RUN tar xzvf ffuf.tar.gz && chmod +x ffuf && mv ffuf /bin
ENTRYPOINT ["ffuf"]