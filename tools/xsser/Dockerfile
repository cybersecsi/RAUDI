ARG PYTHON_ALPINE_VERSION

FROM python:$PYTHON_ALPINE_VERSION

# Build Args
ARG DOWNLOAD_URL

# Content
WORKDIR /code
RUN apk add --no-cache curl-dev \
    && apk add --no-cache --virtual .build-deps git build-base libffi-dev \
    && git clone $DOWNLOAD_URL /code \
    && pip3 install pycurl bs4 pygeoip gobject selenium \
    && python setup.py install \
    && apk del .build-deps
ENTRYPOINT ["xsser"]
CMD ["--help"]