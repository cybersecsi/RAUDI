ARG RUBY_ALPINE_VERSION

FROM ruby:$RUBY_ALPINE_VERSION

WORKDIR /xxeinjector

ARG DOWNLOAD_URL

RUN apk add git && git clone $DOWNLOAD_URL /xxeinjector && apk del --purge git

ENTRYPOINT ["ruby", "XXEinjector.rb"]