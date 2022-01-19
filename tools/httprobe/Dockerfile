# Base Distro Args
ARG GOLANG_ALPINE_VERSION
ARG LATEST_ALPINE_VERSION

FROM golang:$GOLANG_ALPINE_VERSION AS builder
RUN go install github.com/tomnomnom/httprobe@latest

FROM alpine:$LATEST_ALPINE_VERSION

COPY --from=builder /go/bin/httprobe /httprobe/httprobe

WORKDIR /httprobe

ENTRYPOINT ["/httprobe/httprobe"]
CMD ["--help"]