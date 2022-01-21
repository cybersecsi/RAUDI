# Base Distro Arg
ARG PYTHON2_ALPINE_VERSION

FROM python:$PYTHON2_ALPINE_VERSION

# Build Args
ARG DOWNLOAD_URL

# Content
WORKDIR /code
RUN apk add --no-cache --virtual .build-deps git g++ gcc libxml2-dev libxslt-dev \
    && apk add --no-cache libxslt \
    && git clone $DOWNLOAD_URL /code \
    && pip install mechanize lxml \
    && apk del .build-deps
ENTRYPOINT ["python", "xsssniper.py"]
CMD ["-h"]