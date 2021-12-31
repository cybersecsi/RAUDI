FROM node:16-slim

# Build Args
ARG RETIRE_NPM_VERSION

RUN npm install -g retire@$RETIRE_NPM_VERSION
ENTRYPOINT [ "retire" ]