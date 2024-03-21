FROM python:3.11-slim-bullseye

# Build Args
ARG THEHARVESTER_DOWNLOAD_URL

# Content
WORKDIR /theharvester
ADD $THEHARVESTER_DOWNLOAD_URL theharvester.tar.gz
RUN tar -xvf theharvester.tar.gz -C /theharvester --strip-components=1 \
    && pip install -r /theharvester/requirements/base.txt 
ENTRYPOINT ["python", "/theharvester/restfulHarvest.py"]
CMD ["-H", "0.0.0.0", "-p", "80"]