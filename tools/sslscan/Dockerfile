ARG LATEST_ALPINE_VERSION
FROM alpine:$LATEST_ALPINE_VERSION as builder

# Build Args
ARG DOWNLOAD_URL

# Ensure no packages are cached before we try to do an update.
RUN apk cache clean 2> /dev/null || exit 0

RUN apk --no-cache --virtual .build-deps add git gcc make ca-certificates git libc-dev linux-headers openssl perl zlib-dev \
  && update-ca-certificates \
  && git clone $DOWNLOAD_URL /builddir

# Make a static build of sslscan, then strip it of debugging symbols.
RUN cd /builddir && sed -i 's/--version-sort/-V/g' Makefile && make static && strip --strip-all /builddir/sslscan

# Print the output of ldd so we can see what dynamic libraries that sslscan is still dependent upon.
RUN echo "ldd output:" && ldd /builddir/sslscan \
  && echo "ls -al output:" && ls -al /builddir/sslscan


# Start with an empty container for our final build.
FROM scratch

ARG TARGETPLATFORM

# Copy over the sslscan executable from the intermediate build container, along with the dynamic libraries it is dependent upon (see output of ldd, above).
COPY --from=builder /builddir/sslscan /sslscan
COPY --from=builder /lib/libz.so.1 /lib/libz.so.1
COPY --from=builder /lib/ld-musl-${TARGETPLATFORM}.so.1 /lib/ld-musl-${TARGETPLATFORM}.so.1

# Drop root privileges.
USER 65535:65535

ENTRYPOINT ["/sslscan"]