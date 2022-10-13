# Base Distro Arg
ARG GOLANG_ALPINE_VERSION

FROM golang:$GOLANG_ALPINE_VERSION 

RUN go install github.com/OJ/gobuster/v3@latest

ENTRYPOINT [ "gobuster" ]
CMD ["-h"]