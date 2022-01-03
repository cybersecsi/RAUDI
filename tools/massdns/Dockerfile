# Base Distro Arg
ARG LAST_ALPINE_VERSION

FROM alpine:$LAST_ALPINE_VERSION

# Build args
ARG MASSDNS_DOWNLOAD_URL

RUN mkdir massdns
WORKDIR /massdns
ADD $MASSDNS_DOWNLOAD_URL massdns.tar.gz
RUN apk --no-cache --virtual .build-deps add build-base \
    && tar -xvf massdns.tar.gz -C /massdns --strip-components=1 \
    && make && apk del .build-deps
ENTRYPOINT ["/massdns/bin/massdns"]