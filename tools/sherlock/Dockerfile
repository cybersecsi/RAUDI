FROM python:3.7-slim-bullseye as build

# Build Args
ARG DOWNLOAD_URL

WORKDIR /wheels

RUN apt-get update \
    && apt-get install -y git build-essential \
    && git clone $DOWNLOAD_URL /opt/sherlock \
    && pip3 wheel -r /opt/sherlock/requirements.txt \
    && rm -rf /var/lib/apt/lists/*

# Build final image
FROM python:3.7-slim-bullseye
WORKDIR /sherlock

COPY --from=build /wheels /wheels
COPY --from=build /opt/sherlock/ /sherlock

RUN pip3 install --no-cache-dir -r requirements.txt -f /wheels \
  && rm -rf /wheels

ENTRYPOINT ["python", "sherlock.py"]