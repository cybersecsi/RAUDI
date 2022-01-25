ARG PYTHON_ALPINE_VERSION

FROM python:$PYTHON_ALPINE_VERSION

# Build Args
ARG DOWNLOAD_URL
ADD $DOWNLOAD_URL /spidy.tar.gz
WORKDIR /spidy
RUN tar -xvf /spidy.tar.gz -C /spidy --strip-components=1 && pip install -r requirements.txt  && pip install lxml
ENTRYPOINT ["python", "crawler.py"]