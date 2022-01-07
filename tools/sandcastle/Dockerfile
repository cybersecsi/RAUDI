ARG PYTHON2_ALPINE_VERSION

FROM python:$PYTHON2_ALPINE_VERSION

# Build Args
ARG SANDCASTLE_DOWNLOAD_URL

# Content
RUN mkdir /sandcastle
WORKDIR /sandcastle
ADD $SANDCASTLE_DOWNLOAD_URL sandcastle.tar.gz
RUN tar -xvf sandcastle.tar.gz -C /sandcastle --strip-components=1 && pip install requests
ENTRYPOINT ["python", "/sandcastle/sandcastle.py"]