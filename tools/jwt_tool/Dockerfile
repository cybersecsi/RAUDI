# Base Distro Arg
ARG PYTHON_ALPINE_VERSION

FROM python:$PYTHON_ALPINE_VERSION

# Build Args
ARG JWT_TOOL_DOWNLOAD_URL

# Content
RUN mkdir jwt_tool
WORKDIR /jwt_tool
ADD $JWT_TOOL_DOWNLOAD_URL jwt_tool.tar.gz
RUN apk --no-cache --virtual .build-deps add \
    gcc \
    musl-dev \
    libffi-dev \
    openssl-dev \
    && tar -xvf jwt_tool.tar.gz -C /jwt_tool --strip-components=1 \
    && pip3 install -r requirements.txt \
    && apk del .build-deps
ENTRYPOINT ["python3", "/jwt_tool/jwt_tool.py"]