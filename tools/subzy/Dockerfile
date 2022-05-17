# Base Distro Arg
ARG LATEST_ALPINE_VERSION
ARG GOLANG_ALPINE_VERSION

FROM golang:$GOLANG_ALPINE_VERSION AS builder
RUN go install -v github.com/lukasikic/subzy@latest

FROM alpine:$LATEST_ALPINE_VERSION
COPY --from=builder /go/bin/subzy /usr/local/bin/
ENTRYPOINT [ "subzy" ]
