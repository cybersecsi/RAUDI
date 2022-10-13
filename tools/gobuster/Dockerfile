# Base Distro Arg
ARG LATEST_ALPINE_VERSION

FROM alpine:$LATEST_ALPINE_VERSION

# Build Args
ARG GOBUSTER_DOWNLOAD_URL

# Content
ADD $GOBUSTER_DOWNLOAD_URL gobuster.tar.gz
RUN tar xzvf gobuster.tar.gz && chmod +x gobuster && mv gobuster /bin
ENTRYPOINT ["gobuster"]
CMD ["--help"]