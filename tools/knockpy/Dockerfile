FROM python:3.9.9-slim

# Build Args
ARG KNOCKPY_DOWNLOAD_URL

# Content
ADD $KNOCKPY_DOWNLOAD_URL knockpy.tar.gz
RUN mkdir knockpy
RUN tar -xvf knockpy.tar.gz -C /knockpy --strip-components=1
RUN pip install -r /knockpy/requirements.txt
ENTRYPOINT ["python", "/knockpy/knockpy.py"]