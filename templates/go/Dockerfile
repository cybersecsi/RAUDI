# Base Distro Arg
ARG GOLANG_ALPINE_VERSION

FROM golang:$GOLANG_ALPINE_VERSION AS builder

ARG DOWNLOAD_URL
RUN apk update && apk add --no-cache alpine-sdk
WORKDIR /code
ADD $DOWNLOAD_URL code.tar.gz
RUN tar -xvf code.tar.gz -C /code --strip-components=1 && go build  && go install

# Base Distro Arg
ARG LATEST_ALPINE_VERSION

FROM alpine:$LATEST_ALPINE_VERSION

COPY --from=builder <source_builder_dir> <target_dir>
WORKDIR /code
ENTRYPOINT ["<executable>"]