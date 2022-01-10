# Base Distro Arg
ARG DEBIAN_SLIM_VERSION

FROM debian:$DEBIAN_SLIM_VERSION
RUN apt-get update && apt-get install -y <package_name>
ENTRYPOINT ["<package_name>"]