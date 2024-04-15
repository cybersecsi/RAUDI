ARG LATEST_ALPINE_VERSION

FROM alpine:$LATEST_ALPINE_VERSION

# Build Args
ARG NMAP_LAST_RELEASE_URL

# Content
WORKDIR /nmap

# Install dependencies
RUN apk add --update --no-cache \
  ca-certificates \
  libpcap \
  libgcc \ 
  libstdc++ \
  openssl-dev \
  libretls \
  && update-ca-certificates \
  && rm -rf /var/cache/apk/*

# Compile and install Nmap from sources
RUN apk add --update --no-cache --virtual .build-deps \
  libpcap-dev lua-dev linux-headers \
  autoconf g++ libtool automake make subversion \
  && svn checkout $NMAP_LAST_RELEASE_URL /nmap \
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
  && apk del .build-deps \
  && rm -rf /var/cache/apk/* \
  /nmap*

ENTRYPOINT ["/usr/bin/nmap"]

