ARG PYTHON_ALPINE_VERSION

FROM python:$PYTHON_ALPINE_VERSION

# Build Args
ARG DNSCAN_DOWNLOAD_URL

# Content
RUN apk --no-cache add git gcc make openssl-dev libffi-dev libc-dev python3-dev libxml2-dev libxslt-dev && git clone $DNSCAN_DOWNLOAD_URL && apk del --purge git
WORKDIR /dnscan
RUN pip install -r requirements.txt && apk del --purge gcc make openssl-dev libffi-dev libxml2-dev libxslt-dev
ENTRYPOINT ["python", "dnscan.py"]