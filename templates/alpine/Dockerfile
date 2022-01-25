# Base Distro Arg
ARG LATEST_ALPINE_VERSION

FROM alpine:$LATEST_ALPINE_VERSION

# Build Args
ARG DOWNLOAD_URL

# Content
WORKDIR /code
ADD $DOWNLOAD_URL code.tar.gz
RUN apk --no-cache add --virtual .build-deps \ 
    alpine-sdk ncurses-dev  && tar -xvf code.tar.gz -C /code --strip-components=1  && \
     ./configure && make && make install && \
    apk del --purge .build-deps && rm -rf /code
WORKDIR /data
ENTRYPOINT ["<executable>"]