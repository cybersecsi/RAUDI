# Base Distro Arg
ARG PYTHON_ALPINE_VERSION

FROM python:$PYTHON_ALPINE_VERSION

# Build Args
ARG DIRSEARCH_DOWNLOAD_URL

# Content
WORKDIR /dirsearch
ADD $DIRSEARCH_DOWNLOAD_URL dirsearch.tar.gz
RUN tar -xvf dirsearch.tar.gz -C /dirsearch --strip-components=1 \
    && pip3 install --no-cache-dir -r requirements.txt
ENTRYPOINT ["python3", "/dirsearch/dirsearch.py"]