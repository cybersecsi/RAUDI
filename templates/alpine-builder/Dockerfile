# Base Distro Arg
ARG LATEST_ALPINE_VERSION

FROM alpine:$LATEST_ALPINE_VERSION AS builder

# Build Args
ARG DOWNLOAD_URL

# Content
WORKDIR /code
ADD $DOWNLOAD_URL code.tar.gz
RUN apk --no-cache add gcc make curl-dev musl-dev libcurl \ 
    && tar -xvf dirb.tar.gz -C /code --strip-components=1 \
    && chmod -R a+x wordlists configure \
    && ./configure CFLAGS="-O2 -g -fcommon" \
    && make \
    && make install 

FROM alpine:$LATEST_ALPINE_VERSION
COPY --from=builder /usr/local/bin/<executable> /usr/local/bin/<executable>
RUN apk --no-cache add libcurl
ENTRYPOINT ["<executable>"]