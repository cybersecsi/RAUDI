ARG LATEST_ALPINE_VERSION

FROM alpine:$LATEST_ALPINE_VERSION

# Build Args
ARG JOOMSCAN_DOWNLOAD_URL

# Content
WORKDIR /joomscan
ADD $JOOMSCAN_DOWNLOAD_URL joomscan.tar.gz
RUN tar -xvf joomscan.tar.gz -C /joomscan --strip-components=1 \
    && apk add --no-cache perl perl-libwww perl-lwp-protocol-https
ENTRYPOINT [ "perl", "joomscan.pl" ]