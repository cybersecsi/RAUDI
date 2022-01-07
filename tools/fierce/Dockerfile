ARG PYTHON_ALPINE_VERSION

FROM python:$PYTHON_ALPINE_VERSION

# Build Args
ARG FIERCE_DOWNLOAD_URL

# Content
RUN mkdir /fierce
WORKDIR /fierce
ADD $FIERCE_DOWNLOAD_URL fierce.tar.gz
RUN tar -xvf fierce.tar.gz -C /fierce --strip-components=1 && pip install -r requirements.txt
ENTRYPOINT ["python", "/fierce/fierce/fierce.py"]