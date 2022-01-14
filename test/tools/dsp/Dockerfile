# Base Distro Arg
ARG LATEST_UBUNTU_VERSION

FROM ubuntu:$LATEST_UBUNTU_VERSION

# Build Args
ARG DOWNLOAD_URL

RUN apt-get -qq update && apt-get install -y python build-essential git curl && curl -sL https://deb.nodesource.com/setup_10.x | bash - && apt-get install -y docker.io docker-compose nodejs
RUN git clone $DOWNLOAD_URL /home

WORKDIR /home/DockerSecurityPlayground

RUN npm install

COPY . .

ENTRYPOINT ["/bin/bash", "./run.sh"]