ARG LATEST_ALPINE_VERSION

FROM --platform=$BUILDPLATFORM alpine:$LATEST_ALPINE_VERSION AS downloader
ARG TARGETPLATFORM
ARG DOWNLOAD_URL

ADD $DOWNLOAD_URL /3proxy.tar.gz
WORKDIR /3proxy
RUN tar -xvf /3proxy.tar.gz -C /3proxy --strip-components=1 \
    && apk --nocache --virtual .build-deps add gcc g++ make \
    && ln -s Makefile.Linux Makefile \
    && make \
    && apk del .build-deps

FROM alpine:$LATEST_ALPINE_VERSION

WORKDIR /3proxy
COPY --from=downloader /3proxy /3proxy
RUN apk --nocache --virtual .build-deps add make binutils \
    && make install \
    && apk del .build-deps


ENTRYPOINT ["3proxy"]
CMD ["'--help'"]