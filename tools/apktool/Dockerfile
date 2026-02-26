# Base Distro Arg
ARG OPENJDK_ALPINE_VERSION

FROM amazoncorretto:$OPENJDK_ALPINE_VERSION

# Build Args
ARG APKTOOL_DOWNLOAD_URL

# Content
WORKDIR /apktool
ADD $APKTOOL_DOWNLOAD_URL apktool.jar
ENTRYPOINT [ "java", "-jar", "apktool.jar" ]