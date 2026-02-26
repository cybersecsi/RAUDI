# Base Distro Arg
ARG OPENJDK_ALPINE_VERSION

FROM amazoncorretto:$OPENJDK_ALPINE_VERSION

# Build Args
ARG DOWNLOAD_URL

# Content
WORKDIR /code
ADD $DOWNLOAD_URL code.jar
ENTRYPOINT [ "java", "-jar", "code.jar" ]