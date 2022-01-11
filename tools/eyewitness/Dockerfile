ARG PYTHON_ALPINE_VERSION

FROM python:$PYTHON_ALPINE_VERSION

ARG EYEWITNESS_DOWNLOAD_URL

WORKDIR /code

ADD $EYEWITNESS_DOWNLOAD_URL code.tar.gz

RUN tar -xvf code.tar.gz -C /code --strip-components=1

RUN apk --no-cache add build-base libffi-dev && \
    sh Python/setup/setup.sh Alpine &&  \
    apk del --purge build-base libffi-dev

ENTRYPOINT ["python3", "Python/EyeWitness.py", "-d", "/tmp/EyeWitness/results", "--no-prompt"]