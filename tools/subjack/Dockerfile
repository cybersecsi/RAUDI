# Base Distro Arg
ARG LATEST_ALPINE_VERSION
ARG GOLANG_ALPINE_VERSION

FROM golang:$GOLANG_ALPINE_VERSION as builder

RUN go get github.com/haccer/subjack

FROM alpine:$LATEST_ALPINE_VERSION

COPY --from=builder /go/bin/subjack /code/subjack
WORKDIR /code
ENTRYPOINT ["./subjack"]