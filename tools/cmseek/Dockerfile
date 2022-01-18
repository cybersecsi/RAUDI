ARG PYTHON_ALPINE_VERSION

FROM python:$PYTHON_ALPINE_VERSION

# Build Args
ARG CMSEEK_DOWNLOAD_URL

# Content
WORKDIR /cmseek
ADD $CMSEEK_DOWNLOAD_URL cmseek.tar.gz
RUN tar -xvf cmseek.tar.gz -C /cmseek --strip-components=1 
ENTRYPOINT ["python", "cmseek.py"]