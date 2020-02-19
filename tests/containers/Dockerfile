FROM ubuntu:bionic-20191029

RUN apt-get update -y && \
    apt-get install -y stress && \
    rm -rf /var/lib/apt/lists/*



CMD ["/usr/bin/stress","--cpu","8","--io","4","--vm","2","--vm-bytes","128M","--timeout","10s", "--verbose"]
