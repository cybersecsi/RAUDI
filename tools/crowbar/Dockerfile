ARG PYTHON_ALPINE_VERSION

FROM python:$PYTHON_ALPINE_VERSION

# Build Args
ARG DOWNLOAD_URL

# Content
WORKDIR /code
ADD $DOWNLOAD_URL code.tar.gz
RUN tar -xvf code.tar.gz -C /code --strip-components=1 \
    && apk --no-cache --virtual .build-deps add gcc make musl-dev libffi-dev \
    && apk add --no-cache nmap openvpn freerdp gtk-vnc \
    && pip install -r requirements.txt \
    && apk del .build-deps
ENTRYPOINT ["python3", "crowbar.py"]
CMD ["--help"]