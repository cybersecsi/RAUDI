# Base Distro Arg
ARG PYTHON_ALPINE_VERSION

FROM python:$PYTHON_ALPINE_VERSION

# Build Args
ARG SQLMAP_DOWNLOAD_URL

# Content
WORKDIR /sqlmap
RUN wget $SQLMAP_DOWNLOAD_URL -O sqlmap.tar.gz  \
    && tar -xvf sqlmap.tar.gz -C /sqlmap --strip-components=1 && rm sqlmap.tar.gz
ENTRYPOINT ["python3", "/sqlmap/sqlmap.py"]