# Base Distro Arg
ARG LATEST_ALPINE_VERSION

FROM alpine:$LATEST_ALPINE_VERSION

# Build Args
ARG FINDSPLOIT_DOWNLOAD_URL

# Content
RUN mkdir findsploit
WORKDIR /findsploit
ADD $FINDSPLOIT_DOWNLOAD_URL findsploit.tar.gz
RUN apk add --no-cache bash \
    && tar -xvf findsploit.tar.gz -C /findsploit --strip-components=1 \
    && chmod +x install.sh && bash install.sh
ENTRYPOINT ["findsploit"]