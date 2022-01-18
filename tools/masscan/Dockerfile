# Base Distro Arg
ARG LATEST_ALPINE_VERSION

FROM alpine:$LATEST_ALPINE_VERSION AS builder

# Build Args
ARG MASSCAN_DOWNLOAD_URL

# Content
WORKDIR /masscan
ADD $MASSCAN_DOWNLOAD_URL masscan.tar.gz
RUN apk --no-cache add gcc musl-dev make linux-headers libpcap-dev \
    && tar xzvf masscan.tar.gz -C /masscan --strip-components=1 \
    && make \
    && make install 

FROM alpine:$LATEST_ALPINE_VERSION
COPY --from=builder /usr/bin/masscan /usr/bin/masscan
RUN apk --no-cache add libpcap-dev
ENTRYPOINT ["masscan"]