FROM ubuntu:14.04

MAINTAINER <coder li>
RUN apt-get update &&\
    apt-get install -y gnupg &&\
    apt-get install -y wget &&\
    apt-get install -y unzip &&\
# Set env variables used in this Dockerfile (add a unique prefix, such as DOCKYARD)
ENV PROJECT_NAME=blog

RUN cp $DOCKYARD_SRVPROJ/conf/pip.conf /etc/pip.conf
ENV PIP_CONFIG_FILE=/etc/pip.conf

RUN pip install -r $DOCKYARD_SRVPROJ/requirements.txt