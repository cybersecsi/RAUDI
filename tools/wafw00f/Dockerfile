ARG PYTHON_ALPINE_VERSION

FROM python:$PYTHON_ALPINE_VERSION

# Build Args
ARG DOWNLOAD_URL

# Content
WORKDIR /code
ADD $DOWNLOAD_URL code.tar.gz
RUN tar -xvf code.tar.gz -C /code --strip-components=1 \
    && python3 setup.py install
ENTRYPOINT ["wafw00f"]