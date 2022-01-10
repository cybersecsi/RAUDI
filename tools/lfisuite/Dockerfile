# Base Distro Arg
ARG PYTHON2_ALPINE_VERSION

FROM python:$PYTHON2_ALPINE_VERSION

# Build Args
ARG LFISUITE_DOWNLOAD_URL

# Content
WORKDIR /lfisuite
ADD $LFISUITE_DOWNLOAD_URL lfisuite.tar.gz
RUN tar -xvf lfisuite.tar.gz -C /lfisuite --strip-components=1 \
    && pip install termcolor requests
ENTRYPOINT ["python", "/lfisuite/lfisuite.py"]