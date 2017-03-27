FROM python:2.7-slim

MAINTAINER Duy Nguyen <dnguyen0304@gmail.com>

ARG BUILDTIME_DEPENDENCIES="unzip"

ARG NAMESPACE
ARG COMPONENT_1
ARG BLISSEY_CONFIGURATION_FILE_NAME

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends ${BUILDTIME_DEPENDENCIES}

RUN useradd ${NAMESPACE}

RUN mkdir /opt/${NAMESPACE} && \
    mkdir /var/log/${NAMESPACE}

WORKDIR /opt/${NAMESPACE}


# Include Blissey.
# NOTE: New files will NOT overwrite existing files.
ENV BLISSEY_CONFIGURATION_FILE_PATH="/opt/${NAMESPACE}/configuration/${BLISSEY_CONFIGURATION_FILE_NAME}"

COPY build/${COMPONENT_1}-latest.zip .
RUN unzip -qn ${COMPONENT_1}-latest.zip


RUN chown --recursive ${NAMESPACE}:${NAMESPACE} . && \
    chown --recursive ${NAMESPACE}:${NAMESPACE} /var/log/${NAMESPACE}

RUN rm -fr /var/lib/apt/lists/* && \
    apt-get purge -y --auto-remove ${BUILDTIME_DEPENDENCIES}
