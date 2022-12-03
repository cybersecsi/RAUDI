ARG DEBIAN_SLIM_VERSION

FROM --platform=$BUILDPLATFORM debian:$DEBIAN_SLIM_VERSION AS downloader
ARG TARGETPLATFORM
ARG DOWNLOAD_URL

ADD $DOWNLOAD_URL /3proxy.tar.gz
WORKDIR /3proxy
RUN tar -xvf /3proxy.tar.gz -C /3proxy --strip-components=1 \
    && apt update \
    && apt install -y gcc g++ make \
    && ln -s Makefile.Linux Makefile \
    && make

FROM debian:$DEBIAN_SLIM_VERSION

WORKDIR /3proxy
COPY --from=downloader /3proxy /3proxy
RUN apt-get update \
    && apt-get install -y make binutils \
    && make install


ENTRYPOINT ["3proxy"]
CMD ["'--help'"]