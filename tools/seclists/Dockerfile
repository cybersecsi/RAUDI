# Base Distro Arg
ARG LATEST_ALPINE_VERSION

FROM alpine:$LATEST_ALPINE_VERSION

# Build Args
ARG SECLISTS_DOWNLOAD_URL

# Content
WORKDIR /usr/share/wordlists
ADD $SECLISTS_DOWNLOAD_URL seclists.tar.gz
RUN mkdir -p /usr/share/wordlists/SecLists && \
    tar -xvf seclists.tar.gz -C /usr/share/wordlists/SecLists --strip-components=1
VOLUME /usr/share/wordlists/SecLists
COPY run.sh /run.sh
CMD /run.sh