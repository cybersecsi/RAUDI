# Base Distro Arg
ARG LATEST_ALPINE_VERSION
ARG GOLANG_ALPINE_VERSION

FROM golang:$GOLANG_ALPINE_VERSION as builder
RUN GO111MODULE=on go install github.com/haccer/subjack@latest

FROM alpine:$LATEST_ALPINE_VERSION
ADD https://raw.githubusercontent.com/haccer/subjack/master/fingerprints.json /code/fingerprints.json
COPY --from=builder /go/bin/subjack /code/subjack

WORKDIR /code
ENTRYPOINT [ "./subjack", "-c", "./fingerprints.json" ]