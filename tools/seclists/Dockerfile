# Base Distro Arg
ARG LATEST_ALPINE_VERSION

FROM alpine:$LATEST_ALPINE_VERSION

# Build Args
ARG DOWNLOAD_URL

# Content
WORKDIR /usr/share/wordlists
RUN apk --no-cache add --virtual .build-deps \ 
    git && git clone $DOWNLOAD_URL && \
    apk del --purge .build-deps
VOLUME /usr/share/wordlists/SecLists
COPY run.sh /run.sh
CMD /run.sh