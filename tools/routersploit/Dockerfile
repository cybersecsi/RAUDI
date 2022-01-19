ARG PYTHON_ALPINE_VERSION

FROM python:$PYTHON_ALPINE_VERSION

# Build Args
ARG DOWNLOAD_URL

# Content
WORKDIR /code
ADD $DOWNLOAD_URL code.tar.gz
RUN apk --nocache --virtual .build-deps add gcc make musl-dev libffi-dev \ 
    && tar -xvf code.tar.gz -C /code --strip-components=1 \
    && pip install -r requirements.txt \
    && apk del .build-deps
ENTRYPOINT ["python3", "rsf.py"]