# Base Distro Arg
ARG LATEST_UBUNTU_VERSION

FROM ubuntu:$LATEST_UBUNTU_VERSION

# Build Args
ARG GOBUSTER_DOWNLOAD_URL

# Content
RUN apt-get update && apt-get install -y p7zip-full wget git
RUN wget $GOBUSTER_DOWNLOAD_URL -O gobuster.7z
RUN 7z e gobuster.7z && chmod +x gobuster && mv gobuster /bin
ENTRYPOINT ["gobuster"]