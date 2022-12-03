
ARG GOLANG_ALPINE_VERSION
ARG LATEST_ALPINE_VERSION

FROM golang:$GOLANG_ALPINE_VERSION AS builder
ARG DOWNLOAD_URL
RUN apk update && apk add --no-cache alpine-sdk git
RUN git clone https://github.com/blechschmidt/massdns.git && cd massdns && make && make install  
WORKDIR /code
ADD $DOWNLOAD_URL pure.tar.gz
RUN tar -xvf pure.tar.gz -C /code --strip-components=1 && go build  && go install

FROM alpine:$LATEST_ALPINE_VERSION

COPY --from=builder /go/bin/puredns /usr/local/bin/puredns
COPY --from=builder /usr/local/bin/massdns /usr/local/bin/massdns
WORKDIR /current
ENTRYPOINT ["puredns"]