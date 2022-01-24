ARG DEBIAN_SLIM_VERSION

FROM debian:$DEBIAN_SLIM_VERSION
ARG DOWNLOAD_URL
RUN apt-get update &&  apt-get install -y wget && TEMP_DEB="$(mktemp)" && wget -O "$TEMP_DEB" $DOWNLOAD_URL && dpkg -i "$TEMP_DEB" && rm -f "$TEMP_DEB" && apt-get remove -y wget
ENTRYPOINT ["3proxy"]