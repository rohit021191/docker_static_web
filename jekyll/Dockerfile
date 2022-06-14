FROM ubuntu:20.04
LABEL maintainer="info@gnugroup.org"
ENV REFRESHED_AT 2022-06-02

RUN apt-get -yqq update
RUN DEBIAN_FRONTEND=noninteractive apt-get -yqq install ruby ruby-dev build-essential nodejs
RUN gem install jekyll -v 2.5.3

VOLUME /data
VOLUME /var/www/html
WORKDIR /data

ENTRYPOINT [ "jekyll","build","--destination=/var/www/html" ]
