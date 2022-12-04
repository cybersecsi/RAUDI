# Base Distro Arg
ARG LATEST_ALPINE_VERSION

FROM alpine:$LATEST_ALPINE_VERSION AS builder

# Build Args
ARG DIRB_DOWNLOAD_URL

# Content
WORKDIR /dirb
RUN apk --no-cache add gcc make curl-dev musl-dev libcurl git \ 
    && git clone $DIRB_DOWNLOAD_URL /dirb  \
    && chmod -R a+x wordlists configure \
    && ./configure CFLAGS="-O2 -g -fcommon" \
    && make \
    && make install 

FROM alpine:$LATEST_ALPINE_VERSION
COPY --from=builder /usr/local/bin/dirb /usr/local/bin/dirb
RUN apk --no-cache add libcurl
ENTRYPOINT ["dirb"]