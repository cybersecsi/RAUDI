ARG PYTHON_ALPINE_VERSION

FROM python:$PYTHON_ALPINE_VERSION

# Build Args
ARG DOWNLOAD_URL

# Content
WORKDIR /memcrashed
RUN apk add --no-cache --virtual .build-deps git  make \
    && apk --no-cache add tcpdump \
    && git clone $DOWNLOAD_URL /memcrashed \
    && pip install -r requirements.txt \
    && apk del .build-deps

ENTRYPOINT ["python3", "Memcrashed.py"]