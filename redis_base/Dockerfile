FROM ubuntu:18.04
LABEL maintainer="info@gnugroup.org"
RUN apt-get -yqq update

ENV REFRESHED_AT 2022-06-03

RUN DEBIAN_FRONTEND=noninteractive apt-get install -yqq software-properties-common python3-software-properties
RUN add-apt-repository ppa:chris-lea/redis-server
RUN apt-get -yqq update
RUN DEBIAN_FRONTEND=noninteractive apt-get -yqq install redis-server redis-tools

VOLUME [ "/var/lib/redis", "/var/log/redis" ]

EXPOSE 6379
CMD []
