ARG LATEST_ALPINE_VERSION

FROM alpine:$LATEST_ALPINE_VERSION

# Build Args
ARG NIKTO_DOWNLOAD_URL

RUN apk add --no-cache git \
  && git clone $NIKTO_DOWNLOAD_URL  \
  && apk del --purge git

# Install dependencies
RUN echo 'Installing packages for Nikto.' \
  && apk add --update --no-cache --virtual .build-deps \
     perl \
     perl-net-ssleay \
  && echo 'Creating the nikto group.' \
  && addgroup nikto \
  && echo 'Creating the nikto user.' \
  && adduser -G nikto -g "Nikto user" -s /bin/sh -D nikto \
  && echo 'Changing the ownership.' \
  && chown -R nikto.nikto /nikto \
  && echo 'Finishing image.' 

USER nikto
WORKDIR /nikto/program

ENTRYPOINT ["./nikto.pl"]