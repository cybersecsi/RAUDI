# Base Distro Arg
ARG LATEST_ALPINE_VERSION
ARG GOLANG_ALPINE_VERSION

FROM golang:$GOLANG_ALPINE_VERSION as builder

RUN GO111MODULE=on go install github.com/jaeles-project/gospider@latest

FROM alpine:$LATEST_ALPINE_VERSION

COPY --from=builder /go/bin/gospider /code/gospider
WORKDIR /code
ENTRYPOINT ["./gospider"]
CMD ["-h"]