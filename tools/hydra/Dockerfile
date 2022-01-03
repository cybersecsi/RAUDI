# Base Distro Arg
ARG LATEST_UBUNTU_VERSION

FROM ubuntu:$LATEST_UBUNTU_VERSION as builder
ARG HYDRA_DOWNLOAD_URL
RUN mkdir hydra
WORKDIR /hydra
RUN apt-get update && apt-get install -y\
    default-libmysqlclient-dev \
    libgpg-error-dev \
    libgcrypt-dev \
    libpcre3-dev \
    libidn11-dev \
    libssh-dev \
    libssl-dev \
    make \
    gcc
ADD $HYDRA_DOWNLOAD_URL hydra.tar.gz
RUN tar -xvf hydra.tar.gz -C /hydra --strip-components=1
RUN ./configure && make && make install

FROM ubuntu:$LATEST_UBUNTU_VERSION
COPY --from=builder /usr/local/bin /usr/local/bin
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    libgpg-error-dev \
    libgcrypt-dev \
    libpcre3-dev \
    libidn11-dev \
    libssh-dev \
    libssl-dev
ENTRYPOINT ["hydra"]