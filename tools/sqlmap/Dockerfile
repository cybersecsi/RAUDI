# Base Distro Arg
ARG PYTHON_ALPINE_VERSION

FROM python:$PYTHON_ALPINE_VERSION

# Build Args
ARG SQLMAP_DOWNLOAD_URL

# Content
WORKDIR /sqlmap
ADD $SQLMAP_DOWNLOAD_URL sqlmap.tar.gz
RUN tar -xvf sqlmap.tar.gz -C /sqlmap --strip-components=1
ENTRYPOINT ["python3", "/sqlmap/sqlmap.py"]