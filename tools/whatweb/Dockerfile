ARG RUBY_ALPINE_VERSION

FROM ruby:$RUBY_ALPINE_VERSION

# Build Args
ARG WHATWEB_DOWNLOAD_URL

# Content
WORKDIR /whatweb
ADD $WHATWEB_DOWNLOAD_URL whatweb.tar.gz
RUN apk --nocache --virtual .build-deps add build-base \
    && tar -xvf whatweb.tar.gz -C /whatweb --strip-components=1 \
    && bundle update \
    && bundle install \
    && apk del .build-deps
ENTRYPOINT ["./whatweb"]