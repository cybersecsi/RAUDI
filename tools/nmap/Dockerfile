ARG LATEST_ALPINE_VERSION

FROM alpine:$LATEST_ALPINE_VERSION

# Build Args
ARG NMAP_DOWNLOAD_URL

# Content

# Install dependencies
RUN apk add --update --no-cache \
            ca-certificates \
            libpcap \
            libgcc libstdc++ \
            libretls git \
 && update-ca-certificates \
 && rm -rf /var/cache/apk/*

# Clone nmap
RUN git clone $NMAP_DOWNLOAD_URL
WORKDIR /nmap

# Compile and install Nmap from sources
RUN apk add --update --no-cache --virtual .build-deps \
        libpcap-dev libretls-dev lua-dev linux-headers \
        autoconf g++ libtool make \
 && ./configure \
        --prefix=/usr \
        --sysconfdir=/etc \
        --mandir=/usr/share/man \
        --infodir=/usr/share/info \
        --without-zenmap \
        --without-nmap-update \
        --with-openssl=/usr/lib \
        --with-liblua=/usr/include \
 && make \
 && make install \
    \
 && apk del .build-deps git\
 && rm -rf /var/cache/apk/* \
           /nmap*

ENV NMAPDIR=/nmap

ENTRYPOINT ["nmap"]

