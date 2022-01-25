# Base Distro Arg
ARG DEBIAN_SLIM_VERSION

FROM debian:$DEBIAN_SLIM_VERSION

ARG DOWNLOAD_URL
ADD $DOWNLOAD_URL /target.deb
RUN dpkg -i /target.deb \
    && rm -f /target.deb
ENTRYPOINT ["<executable>"]