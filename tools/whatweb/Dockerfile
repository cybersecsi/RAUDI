FROM ruby:3.1.0-slim

# Build Args
ARG WHATWEB_DOWNLOAD_URL

# Content
RUN mkdir whatweb
WORKDIR /whatweb
ADD $WHATWEB_DOWNLOAD_URL whatweb.tar.gz
RUN tar -xvf whatweb.tar.gz -C /whatweb --strip-components=1
RUN bundle install
ENTRYPOINT ["./whatweb"]