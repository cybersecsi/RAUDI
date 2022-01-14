ARG RUBY_ALPINE_VERSION

FROM ruby:2.3.8-alpine
WORKDIR /code

ARG OXMLXXE_DOWNLOAD_URL

RUN apk add --no-cache make git alpine-sdk sqlite-dev libxslt-dev libxml2-dev zlib-dev gcc
RUN git clone $OXMLXXE_DOWNLOAD_URL /code

RUN bundle install

EXPOSE 4567

ENTRYPOINT ["ruby", "server.rb", "-o", "0.0.0.0", "4567"]