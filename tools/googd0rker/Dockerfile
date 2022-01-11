ARG PYTHON_ALPINE_VERSION

FROM python:$PYTHON_ALPINE_VERSION

# Build Args
ARG GOOGD0RKER_DOWNLOAD_URL

# Content
WORKDIR /GoogD0rker

# Install application
RUN apk add git \
    && rm -rf /var/cache/apk/* \
    && git clone $GOOGD0RKER_DOWNLOAD_URL /GoogD0rker \
    && pip install -r requirements.txt

ENTRYPOINT ["python", "googd0rker_broken.py"]

