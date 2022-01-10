ARG RUBY_ALPINE_VERSION

FROM ruby:$RUBY_ALPINE_VERSION

# Build Args
ARG DOWNLOAD_URL

# Content
WORKDIR /code
ADD $DOWNLOAD_URL code.tar.gz
RUN tar -xvf code.tar.gz -C /code --strip-components=1 \
    && bundle install
ENTRYPOINT ["./<executable>"]