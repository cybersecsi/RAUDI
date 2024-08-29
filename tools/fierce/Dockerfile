ARG PYTHON_ALPINE_VERSION

FROM python:$PYTHON_ALPINE_VERSION

# Build Args
ARG FIERCE_DOWNLOAD_URL

# Content
WORKDIR /fierce
ADD $FIERCE_DOWNLOAD_URL fierce.tar.gz
RUN tar -xvf fierce.tar.gz -C /fierce --strip-components=1 && pip install dnspython==1.16.0
ENTRYPOINT ["python", "/fierce/fierce/fierce.py"]