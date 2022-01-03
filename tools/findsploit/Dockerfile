# Base Distro Arg
ARG LATEST_UBUNTU_VERSION

FROM ubuntu:$LATEST_UBUNTU_VERSION

# Build Args
ARG FINDSPLOIT_DOWNLOAD_URL

# Content
RUN mkdir findsploit
WORKDIR /findsploit
ADD $FINDSPLOIT_DOWNLOAD_URL findsploit.tar.gz
RUN tar -xvf findsploit.tar.gz -C /findsploit --strip-components=1
RUN chmod +x install.sh 
RUN ./install.sh
ENTRYPOINT ["findsploit"]