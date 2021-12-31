FROM python:3.9.9-slim

# Build Args
ARG BFAC_DOWNLOAD_URL

# Content
RUN mkdir bfac
WORKDIR /bfac
ADD $BFAC_DOWNLOAD_URL bfac.tar.gz
RUN tar -xvf bfac.tar.gz -C /bfac --strip-components=1
RUN python3 setup.py install
ENTRYPOINT ["bfac"]