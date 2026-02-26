ARG LATEST_ALPINE_VERSION

FROM alpine:$LATEST_ALPINE_VERSION AS builder

# Build Args
ARG DEX2JAR_DOWNLOAD_URL

# Content
WORKDIR /code
ADD $DEX2JAR_DOWNLOAD_URL code.tar.gz
RUN apk --no-cache add openjdk8 \
    && tar -xvf code.tar.gz -C /code --strip-components=1 \
    && mkdir /build \ 
    && ./gradlew distZip \
    && unzip /code/dex-tools/build/distributions/dex-tools*.zip -d /build \
    && mv /build/dex-tools* /build/dex-tools

FROM alpine:$LATEST_ALPINE_VERSION

COPY --from=builder /build/dex-tools /dex-tools
RUN apk --no-cache add openjdk8

WORKDIR /dex-tools
ENTRYPOINT ["sh", "d2j-dex2jar.sh"]