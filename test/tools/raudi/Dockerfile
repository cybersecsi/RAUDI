# Base Distro ARg
ARG LATEST_ALPINE_VERSION

FROM alpine:$LATEST_ALPINE_VERSION

ARG FILENAME=hello
RUN echo "  _____               _____  _____        " >> $FILENAME
RUN echo " / ____|             / ____||_   _|       " >> $FILENAME
RUN echo "| (___    ___   ___ | (___    | |         " >> $FILENAME
RUN echo " \___ \  / _ \ / __| \___ \   | |         " >> $FILENAME
RUN echo " ____) ||  __/| (__  ____) | _| |_        " >> $FILENAME
RUN echo "|_____/  \___| \___||_____/ |_____|       " >> $FILENAME
RUN echo "                                          " >> $FILENAME
RUN echo "This is just a 'Hello World' image        " >> $FILENAME
RUN echo "Visit https://github.com/cybersecsi/raudi " >> $FILENAME

ENTRYPOINT ["cat", "hello"]