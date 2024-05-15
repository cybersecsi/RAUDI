# Base Distro Arg
ARG GOLANG_ALPINE_VERSION

FROM golang:$GOLANG_ALPINE_VERSION

RUN GO111MODULE=on go install github.com/tomnomnom/gf@latest
RUN mkdir ~/.gf \
  && apk add --no-cache --virtual .build-deps git \
  && git clone https://github.com/1ndianl33t/Gf-Patterns  \
  && mv Gf-Patterns/*.json ~/.gf \
  && rm -rf Gf-Patterns \
  && apk del .build-deps \ 
  && rm -rf /var/cache/apk/*

ENTRYPOINT ["gf"]
CMD ["-h"]