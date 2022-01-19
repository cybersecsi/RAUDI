# Base Distro Args
ARG GOLANG_ALPINE_VERSION
ARG LATEST_ALPINE_VERSION

FROM golang:$GOLANG_ALPINE_VERSION AS builder
RUN go install github.com/hakluke/hakrevdns@latest

FROM alpine:$LATEST_ALPINE_VERSION

COPY --from=builder /go/bin/hakrevdns /hakrevdns/hakrevdns

WORKDIR /hakrevdns

ENTRYPOINT ["/hakrevdns/hakrevdns"]
CMD ["--help"]