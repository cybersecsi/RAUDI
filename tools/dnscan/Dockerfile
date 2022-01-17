ARG PYTHON_ALPINE_VERSION

FROM python:$PYTHON_ALPINE_VERSION AS builder

# Build Args
ARG DNSCAN_DOWNLOAD_URL

# Content
RUN apk --no-cache add git gcc make openssl-dev libffi-dev libc-dev libxml2-dev libxslt-dev \
    && git clone $DNSCAN_DOWNLOAD_URL \
    && pip install -r /dnscan/requirements.txt

FROM python:$PYTHON_ALPINE_VERSION

COPY --from=builder /dnscan /dnscan
COPY --from=builder /usr/local/lib/python3.9/site-packages/ /usr/local/lib/python3.9/site-packages/

WORKDIR /dnscan
ENTRYPOINT ["python", "dnscan.py"]