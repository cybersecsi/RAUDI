ARG DEBIAN_SLIM_VERSION

FROM debian:$DEBIAN_SLIM_VERSION
ARG DOWNLOAD_URL
ADD $DOWNLOAD_URL /3proxy.deb
RUN dpkg -i /3proxy.deb \
    && rm -f /3proxy.deb
ENTRYPOINT ["3proxy"]