# Base Distro Arg
ARG GOLANG_ALPINE_VERSION

FROM golang:$GOLANG_ALPINE_VERSION 

RUN go install github.com/hahwul/dalfox/v2@latest

ENTRYPOINT [ "dalfox" ]
CMD ["-h"]