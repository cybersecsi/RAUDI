ARG RUBY_ALPINE_VERSION

FROM ruby:$RUBY_ALPINE_VERSION

# Build Args
ARG WHATWEB_DOWNLOAD_URL

# Content
RUN mkdir whatweb
WORKDIR /whatweb
ADD $WHATWEB_DOWNLOAD_URL whatweb.tar.gz
RUN tar -xvf whatweb.tar.gz -C /whatweb --strip-components=1 \
    && bundle install
ENTRYPOINT ["./whatweb"]