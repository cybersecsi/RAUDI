ARG PYTHON_ALPINE_VERSION

FROM python:$PYTHON_ALPINE_VERSION

# Build Args
ARG THEHARVESTER_DOWNLOAD_URL

# Content
WORKDIR /theharvester
ADD $THEHARVESTER_DOWNLOAD_URL theharvester.tar.gz
RUN apk --no-cache add \
        gcc \
        musl-dev \
        libffi-dev \
        libxml2-dev \
        libxslt-dev \
        make \
    && tar -xvf theharvester.tar.gz -C /theharvester --strip-components=1 \
    && pip install -r /theharvester/requirements/base.txt \
    && apk del --purge \
        gcc \
        musl-dev \
        make
ENTRYPOINT ["python", "/theharvester/theHarvester.py"]