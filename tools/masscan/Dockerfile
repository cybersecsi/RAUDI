# Base Distro Arg
ARG LAST_UBUNTU_VERSION

FROM ubuntu:$LAST_UBUNTU_VERSION as builder
ARG MASSCAN_DOWNLOAD_URL
RUN apt-get update && apt-get install -y make gcc libpcap-dev
ADD $MASSCAN_DOWNLOAD_URL masscan.tar.gz
RUN mkdir masscan
RUN tar xzvf masscan.tar.gz -C /masscan --strip-components=1
WORKDIR /masscan
RUN make && make install

FROM ubuntu:$LAST_UBUNTU_VERSION
COPY --from=builder /usr/bin /usr/bin
RUN apt-get update && apt-get install -y libpcap-dev
ENTRYPOINT ["masscan"]