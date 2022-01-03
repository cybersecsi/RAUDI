# Base Distro Arg
ARG LATEST_ALPINE_VERSION

FROM alpine:$LATEST_ALPINE_VERSION

# Build args
ARG GITROB_DOWNLOAD_URL

RUN mkdir gitrob
WORKDIR /gitrob
ADD $GITROB_DOWNLOAD_URL gitrob.zip
RUN apk --no-cache --virtual .build-deps add unzip \
    && unzip -j gitrob.zip -d /gitrob \
    && apk del .build-deps
ENTRYPOINT ["/gitrob/gitrob"]