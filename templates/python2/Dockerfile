# Base Distro Arg
ARG PYTHON2_ALPINE_VERSION

FROM python:$PYTHON2_ALPINE_VERSION

# Build Args
ARG DOWNLOAD_URL

# Content
WORKDIR /code
ADD $DOWNLOAD_URL code.tar.gz
RUN tar -xvf code.tar.gz -C /code --strip-components=1
ENTRYPOINT ["python", "<file>"]