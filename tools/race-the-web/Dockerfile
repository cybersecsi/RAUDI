# Base Distro Arg
ARG LATEST_ALPINE_VERSION

FROM alpine:$LATEST_ALPINE_VERSION

# Build Args
ARG RACETHEWEB_DOWNLOAD_URL

# Content
RUN mkdir racetheweb
WORKDIR /racetheweb
ADD $RACETHEWEB_DOWNLOAD_URL /racetheweb/racetheweb
RUN chmod u+x /racetheweb/racetheweb
ENTRYPOINT ["/racetheweb/racetheweb"]