# Base Distro Arg
ARG LATEST_ALPINE_VERSION
ARG GOLANG_ALPINE_VERSION

FROM golang:$GOLANG_ALPINE_VERSION AS builder

ARG DOWNLOAD_URL

WORKDIR /go/src/github.com/xray
RUN apk --no-cache add git make \
    && git clone $DOWNLOAD_URL /go/src/github.com/xray \
    && go env -w GO111MODULE=off \
    && make

FROM alpine:$LATEST_ALPINE_VERSION

COPY --from=builder /go/src/github.com/xray/build/xray /code/xray
WORKDIR /code
EXPOSE 8080
ENTRYPOINT ["./xray"]
CMD ["--help"]