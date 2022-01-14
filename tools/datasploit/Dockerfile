# Base Distro Arg
ARG PYTHON2_ALPINE_VERSION

FROM python:$PYTHON2_ALPINE_VERSION

# Build Args
ARG DATASPLOIT_DOWNLOAD_URL

# Content
WORKDIR /datasploit

RUN apk add --no-cache --virtual .build-deps git libxml2-dev libxslt-dev build-base\
    && rm -rf /var/cache/apk/* \
    && git clone $DATASPLOIT_DOWNLOAD_URL /datasploit  \
    && pip install update-checker==0.17 praw==6.0.0 python-wappalyzer==0.2.2 \
    google-api-core==1.15.0  google-api-python-client==1.9.0 \
    && pip install -r requirements.txt \
    && pip install pip==9.0.3  \
    && apk del .build-deps \
    && rm -rf /var/cache/apk/*

ENTRYPOINT ["python", "./datasploit.py"]
