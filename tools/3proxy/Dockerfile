ARG LATEST_GCC_VERSION
ARG LATEST_BUSYBOX_GLIBC_VERSION

FROM gcc:$LATEST_GCC_VERSION AS buildenv
ARG DOWNLOAD_URL

ADD $DOWNLOAD_URL /3proxy.tar.gz
WORKDIR /3proxy
RUN tar -xvf /3proxy.tar.gz -C /3proxy --strip-components=1 \
    && echo "">> Makefile.Linux && \
    echo PLUGINS = StringsPlugin TrafficPlugin PCREPlugin TransparentPlugin SSLPlugin>>Makefile.Linux && \
    echo LIBS = -l:libcrypto.a -l:libssl.a -ldl >>Makefile.Linux && \
    make -f Makefile.Linux && \
    strip bin/3proxy && \
    strip bin/StringsPlugin.ld.so && \
    strip bin/TrafficPlugin.ld.so && \
    strip bin/PCREPlugin.ld.so && \
    strip bin/TransparentPlugin.ld.so && \
    strip bin/SSLPlugin.ld.so && \
    mkdir /usr/local/lib/3proxy && \
    cp "/lib/`gcc -dumpmachine`"/libdl.so.* /usr/local/lib/3proxy/

FROM busybox:$LATEST_BUSYBOX_GLIBC_VERSION
COPY --from=buildenv /usr/local/lib/3proxy/libdl.so.* /lib/
COPY --from=buildenv 3proxy/bin/3proxy /bin/
COPY --from=buildenv 3proxy/bin/*.ld.so /usr/local/3proxy/libexec/
RUN mkdir /usr/local/3proxy/logs &&\
    mkdir /usr/local/3proxy/conf && \
    chown -R 65535:65535 /usr/local/3proxy && \
    chmod -R 550  /usr/local/3proxy && \
    chmod 750  /usr/local/3proxy/logs && \
    chmod -R 555 /usr/local/3proxy/libexec && \
    chown -R root /usr/local/3proxy/libexec && \
    mkdir /etc/3proxy/ && \
    echo chroot /usr/local/3proxy 65535 65535 >/etc/3proxy/3proxy.cfg && \
    echo include /conf/3proxy.cfg >>/etc/3proxy/3proxy.cfg && \
    chmod 440  /etc/3proxy/3proxy.cfg
ENTRYPOINT ["/bin/3proxy", "/etc/3proxy/3proxy.cfg"]
CMD ["'--help'"]