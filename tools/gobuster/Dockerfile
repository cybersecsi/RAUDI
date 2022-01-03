# Base Distro Arg
ARG LATEST_ALPINE_VERSION

FROM alpine:$LATEST_ALPINE_VERSION

# Build Args
ARG GOBUSTER_DOWNLOAD_URL

# Content
ADD $GOBUSTER_DOWNLOAD_URL gobuster.7z
RUN apk add --no-cache p7zip \
    && 7z e gobuster.7z \
    && chmod +x gobuster \
    && mv gobuster /bin
ENTRYPOINT ["gobuster"]