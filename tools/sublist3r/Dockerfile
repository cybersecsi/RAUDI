FROM python:3.9.9-slim

# Build Args
ARG SUBLIST3R_DOWNLOAD_URL

# Content
ADD $SUBLIST3R_DOWNLOAD_URL sublist3r.tar.gz
RUN mkdir sublist3r
RUN tar -xvf sublist3r.tar.gz -C /sublist3r --strip-components=1
RUN pip install -r /sublist3r/requirements.txt
ENTRYPOINT ["python", "/sublist3r/sublist3r.py"]