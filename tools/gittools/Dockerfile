ARG PYTHON_ALPINE_VERSION

FROM python:$PYTHON_ALPINE_VERSION

ARG GITTOLS_DOWNLOAD_URL

WORKDIR /code

ADD $GITTOLS_DOWNLOAD_URL code.tar.gz

RUN tar -xvf code.tar.gz -C /code --strip-components=1

RUN apk add git curl bash sed py3-requests

RUN ln Dumper/gitdumper.sh /bin/gitdumper && \
    ln Finder/gitfinder.py /bin/gitfinder &&\
    ln Extractor/extractor.sh /bin/extractor

