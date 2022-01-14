ARG PYTHON_ALPINE_VERSION

FROM python:$PYTHON_ALPINE_VERSION

# Build Args
ARG BFAC_DOWNLOAD_URL

# Content
WORKDIR /bfac
ADD $BFAC_DOWNLOAD_URL bfac.tar.gz
RUN tar -xvf bfac.tar.gz -C /bfac --strip-components=1
RUN python3 setup.py install
ENTRYPOINT ["bfac"]