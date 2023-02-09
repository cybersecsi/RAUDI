# Base Distro Arg
ARG LATEST_ALPINE_VERSION

FROM alpine:$LATEST_ALPINE_VERSION

# Build Args
ARG HYDRA_DOWNLOAD_URL

# Content
WORKDIR /hydra
#ADD $HYDRA_DOWNLOAD_URL hydra.tar.gz
RUN apk --no-cache --virtual .build-deps add \
        gcc \
        musl-dev \
        libidn-dev \
        libssh-dev \
        mariadb-connector-c-dev \
        mariadb-dev \
        postgresql-dev \
        make \
        curl \
    && apk add --no-cache \
        openssl-dev \
        libssh \
        mariadb-connector-c \
        libgpg-error-dev \
        libgcrypt-dev \
        pcre-dev \
        libidn \
        libpq \
    && curl -sSL $HYDRA_DOWNLOAD_URL | tar xz -C /hydra --strip-components=1 \
    && ./configure && make install \
    && apk del .build-deps \
    && rm -rf /var/cache/apk/* /hydra
ENTRYPOINT ["hydra"]