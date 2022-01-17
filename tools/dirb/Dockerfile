# Base Distro Arg
ARG LATEST_ALPINE_VERSION

FROM alpine:$LATEST_ALPINE_VERSION AS builder

# Build Args
ARG DIRB_DOWNLOAD_URL

# Content
WORKDIR /dirb
ADD $DIRB_DOWNLOAD_URL dirb.tar.gz
RUN apk --no-cache add gcc make curl-dev musl-dev libcurl \ 
    && tar -xvf dirb.tar.gz -C /dirb --strip-components=1 \
    && chmod -R a+x wordlists configure \
    && ./configure CFLAGS="-O2 -g -fcommon" \
    && make \
    && make install 

FROM alpine:$LATEST_ALPINE_VERSION
COPY --from=builder /usr/local/bin/dirb /usr/local/bin/dirb
RUN apk --no-cache add libcurl
ENTRYPOINT ["dirb"]