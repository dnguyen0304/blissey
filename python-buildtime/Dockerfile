FROM python:2.7-slim

MAINTAINER Duy Nguyen <dnguyen0304@gmail.com>

ENV SHARED_VOLUME="/tmp/build"

RUN RUNTIME_DEPENDENCIES="build-essential zip" && \
    apt-get update -y && \
    apt-get install -y --no-install-recommends ${RUNTIME_DEPENDENCIES}

RUN mkdir ${SHARED_VOLUME} && \
    mkdir /tmp/.build

WORKDIR /tmp/.build

RUN rm -fr /var/lib/apt/lists/*

VOLUME ${SHARED_VOLUME}

ENTRYPOINT ["./build.sh"]
