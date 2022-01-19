ARG PYTHON_ALPINE_VERSION

FROM python:$PYTHON_ALPINE_VERSION

# Build Args
ARG DOWNLOAD_URL

# Content
WORKDIR /code

RUN apk add --nocache --virtual .build-deps git \
    && git clone $DOWNLOAD_URL /code \
    && python3 setup.py install \
    && apk del .build-deps

ENTRYPOINT ["/code/linkfinder.py"]