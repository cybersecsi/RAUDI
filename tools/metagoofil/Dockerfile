ARG PYTHON_ALPINE_VERSION

FROM python:$PYTHON_ALPINE_VERSION

# Build Args
ARG DOWNLOAD_URL

# Content
WORKDIR /metagoofil
RUN apk --no-cache --virtual .build-deps add git \
    && git clone $DOWNLOAD_URL /metagoofil \
    && pip install --no-cache-dir -r requirements.txt \
    && apk del .build-deps

ENTRYPOINT ["python", "metagoofil.py", "-o", "/output"]