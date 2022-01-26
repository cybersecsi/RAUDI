# Base Distro Arg
ARG LATEST_ALPINE_VERSION

FROM alpine:$LATEST_ALPINE_VERSION

# Build Args
ARG DOWNLOAD_URL

# Content
WORKDIR /code
ADD $DOWNLOAD_URL code.tar.gz
RUN apk --no-cache add perl \
    && apk --no-cache --virtual .build-deps add make \
    && tar -xvf code.tar.gz -C /code --strip-components=1 \
    && perl Makefile.PL \
    && make \
    && make test \
    && make install \
    && apk del .build-deps
    
ENTRYPOINT ["exiftool"]