# Base Distro Arg
ARG LATEST_ALPINE_VERSION

FROM alpine:$LATEST_ALPINE_VERSION

# Build Args
ARG MASSCAN_DOWNLOAD_URL

# Content
RUN mkdir masscan
WORKDIR /masscan
ADD $MASSCAN_DOWNLOAD_URL masscan.tar.gz
RUN apk --no-cache add \
        gcc \
        musl-dev \
        make \
        linux-headers \
        libpcap-dev \
    && tar xzvf masscan.tar.gz -C /masscan --strip-components=1 \
    && make && make install \
    && apk del --purge \
        gcc \
        musl-dev \
        make
ENTRYPOINT ["masscan"]