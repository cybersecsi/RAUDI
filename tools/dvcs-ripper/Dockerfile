ARG DEBIAN_SLIM_VERSION

FROM debian:$DEBIAN_SLIM_VERSION

# Build Args
ARG DVCRIPPER_DOWNLOAD_URL

# Content
WORKDIR /dvcs-ripper

RUN apt update && apt install -y perl libio-socket-ssl-perl libdbd-sqlite3-perl libclass-dbi-perl libio-all-lwp-perl \
    libparallel-forkmanager-perl libredis-perl libalgorithm-combinatorics-perl \
    cvs subversion git mercurial bzr && \
    git clone $DVCRIPPER_DOWNLOAD_URL /dvcs-ripper && \
    apt-get clean


RUN ln rip-cvs.pl /bin/rip-cvs && ln rip-git.pl /bin/rip-git && ln rip-bzr.pl /bin/rip-bzr && \
    ln rip-hg.pl /bin/rip-hg && ln rip-svn.pl /bin/rip-svn
