# Base Distro Arg
ARG LATEST_ALPINE_VERSION as builder

FROM alpine:$LATEST_ALPINE_VERSION

# Build Args

# Content
WORKDIR /usr/share/wordlists
RUN apk --no-cache add --virtual .build-deps \ 
    git && git clone https://github.com/danielmiessler/SecLists && \
    apk del --purge .build-deps
VOLUME /usr/share/wordlists/SecLists
COPY run.sh /run.sh
CMD /run.sh