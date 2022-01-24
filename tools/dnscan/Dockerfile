ARG PYTHON_ALPINE_VERSION

FROM python:$PYTHON_ALPINE_VERSION AS builder

# Build Args
ARG DNSCAN_DOWNLOAD_URL

# Content
WORKDIR /dnscan
RUN apk --no-cache --virtual .build-deps add  git gcc make openssl-dev libffi-dev libc-dev libxml2-dev libxslt-dev \
    && git clone $DNSCAN_DOWNLOAD_URL /dnscan \
    && pip install -r requirements.txt \
    && pip install packaging \
    && apk del .build-deps

ENTRYPOINT ["python", "dnscan.py"]