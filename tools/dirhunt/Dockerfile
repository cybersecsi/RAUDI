FROM python:3.9

# Build Args
ARG DIRHUNT_VERSION

# Content
RUN pip install dirhunt==$DIRHUNT_VERSION
ENTRYPOINT ["dirhunt"]