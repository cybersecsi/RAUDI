# Base Distro Arg
ARG LATEST_ALPINE_VERSION

FROM alpine:$LATEST_ALPINE_VERSION

# Build args
ARG DOWNLOAD_URL

WORKDIR /subfinder
ADD $DOWNLOAD_URL subfinder.zip
RUN apk --no-cache --virtual .build-deps add unzip \
    && unzip -j subfinder.zip -d /subfinder \
    && apk del .build-deps
ENTRYPOINT ["/subfinder/subfinder"]