# Base Distro Arg
ARG LATEST_ALPINE_VERSION
ARG GOLANG_ALPINE_VERSION

FROM golang:$GOLANG_ALPINE_VERSION AS builder

RUN go install github.com/003random/getJS@latest

FROM alpine:$LATEST_ALPINE_VERSION

COPY --from=builder /go/bin/getJS /code/getJS
WORKDIR /code
ENTRYPOINT ["./getJS"]
CMD ["--help"]