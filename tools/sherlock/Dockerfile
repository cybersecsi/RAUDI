ARG PYTHON3_SLIM_VERSION
FROM python:$PYTHON3_SLIM_VERSION

# Build Args
ARG PIP_VERSION

# Content
RUN pip install sherlock-project==$PIP_VERSION

ENTRYPOINT ["sherlock"]