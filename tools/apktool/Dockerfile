# Base Distro Arg
ARG OPENJDK_ALPINE_VERSION

FROM openjdk:$OPENJDK_ALPINE_VERSION

# Build Args
ARG APKTOOL_DOWNLOAD_URL

# Content
RUN mkdir apktool
WORKDIR /apktool
ADD $APKTOOL_DOWNLOAD_URL apktool.jar
ENTRYPOINT [ "java", "-jar", "apktool.jar" ]