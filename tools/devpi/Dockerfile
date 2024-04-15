ARG PYTHON_ALPINE_VERSION

FROM python:$PYTHON_ALPINE_VERSION

# Build Args
ARG DOWNLOAD_URL

# Content
WORKDIR /code
RUN apk --no-cache --virtual .build-deps add git build-base \
  && git clone $DOWNLOAD_URL /code \
  && pip install ./server ./web \
  && devpi-init --no-root-pypi \
  && apk del .build-deps

ENTRYPOINT ["devpi-server", "--host", "0.0.0.0"]