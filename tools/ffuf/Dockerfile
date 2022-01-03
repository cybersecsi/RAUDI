# Base Distro Arg
ARG LATEST_ALPINE_VERSION

FROM alpine:$LATEST_ALPINE_VERSION

# Build Args
ARG FFUF_DOWNLOAD_URL

# Content
ADD $FFUF_DOWNLOAD_URL ffuf.tar.gz
RUN tar xzvf ffuf.tar.gz && chmod +x ffuf && mv ffuf /bin
ENTRYPOINT ["ffuf"]