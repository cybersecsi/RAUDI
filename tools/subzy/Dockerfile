# Base Distro Arg
ARG LATEST_ALPINE_VERSION
ARG GOLANG_ALPINE_VERSION

FROM golang:$GOLANG_ALPINE_VERSION AS builder
ARG DOWNLOAD_URL
RUN apk update && apk add --no-cache alpine-sdk
WORKDIR /code
ADD $DOWNLOAD_URL code.tar.gz
RUN tar -xvf code.tar.gz -C /code --strip-components=1 && go build  && go install

FROM alpine:$LATEST_ALPINE_VERSION
COPY --from=builder /go/bin/subzy /usr/local/bin/
ENTRYPOINT [ "subzy" ]
