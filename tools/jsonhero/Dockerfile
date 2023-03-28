ARG NODE_ALPINE_VERSION

FROM node:$NODE_ALPINE_VERSION AS builder

# Build Args
ARG DOWNLOAD_URL

# Content
WORKDIR /jsonhero
RUN apk --no-cache add git \ 
    && git clone $DOWNLOAD_URL /jsonhero  \
    && npm install \
    && echo "SESSION_SECRET=abc123" > .env \
    && npm run build 


FROM node:$NODE_ALPINE_VERSION

WORKDIR /jsonhero
COPY --from=builder /jsonhero /jsonhero
ENTRYPOINT ["npm"]
CMD ["start"]