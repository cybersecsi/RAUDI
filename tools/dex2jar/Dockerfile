ARG OPENJDK8_ALPINE_VERSION

FROM openjdk:$OPENJDK8_ALPINE_VERSION

ARG DEX2JAR_DOWNLOAD_URL

WORKDIR /code

ADD $DEX2JAR_DOWNLOAD_URL code.tar.gz

RUN tar -xvf code.tar.gz -C /code --strip-components=1 && mkdir /dex2jar && \
    ./gradlew distZip && unzip /code/dex-tools/build/distributions/dex-tools*.zip -d /code/dex-tools/build/distributions
ENV DEX2JAR_PATH="/code/dex-tools/build/distributions/dex-tools"

WORKDIR /dex2jar

RUN rm /code/dex-tools/build/distributions/dex-tools*.zip && \
        mv $(ls -d /code/dex-tools/build/distributions/dex-tools-*) /code/dex-tools/build/distributions/dex-tools

ENTRYPOINT ["sh", "/code/dex-tools/build/distributions/dex-tools/d2j-dex2jar.sh"]

