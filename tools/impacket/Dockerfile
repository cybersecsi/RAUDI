ARG PYTHON_ALPINE_VERSION
FROM python:$PYTHON_ALPINE_VERSION as compile
ARG DOWNLOAD_URL
WORKDIR /opt
RUN apk add --no-cache git gcc musl-dev python3-dev libffi-dev openssl-dev cargo
RUN python3 -m pip install virtualenv
RUN virtualenv -p python venv
ENV PATH="/opt/venv/bin:$PATH"
ADD $DOWNLOAD_URL core.tar.gz
RUN mkdir impacket && tar -xvf core.tar.gz -C /opt/impacket --strip-components=1 
RUN python3 -m pip install /opt/impacket/

FROM python:$PYTHON_ALPINE_VERSION 
COPY --from=compile /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
ENTRYPOINT ["/bin/sh"]
