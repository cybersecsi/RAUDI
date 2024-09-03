FROM python:3.11-alpine

# Build Args
ARG KNOCKPY_DOWNLOAD_URL

# Content
WORKDIR /knockpy
ADD $KNOCKPY_DOWNLOAD_URL knockpy.tar.gz
RUN tar -xvf knockpy.tar.gz -C /knockpy --strip-components=1
RUN pip install .
ENTRYPOINT ["knockpy"]