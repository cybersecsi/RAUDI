ARG PYTHON_ALPINE_VERSION

FROM python:$PYTHON_ALPINE_VERSION

# Build Args
ARG DOWNLOAD_URL

# Content
WORKDIR /code
RUN apk --no-cache --virtual .build-deps add git \
    && git clone $DOWNLOAD_URL /code \
    && pip install -r requirements.txt \
    && apk del .build-deps

ENTRYPOINT ["python3", "striker.py"]