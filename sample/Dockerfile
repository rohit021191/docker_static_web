FROM ubuntu:20.04
LABEL maintainer="info@gnugroup.org"
ENV REFRESHED_AT 2022-06-02
RUN apt-get -yqq update
RUN apt-get -yqq install nginx
RUN mkdir -p /var/www/html/website
ADD global.conf /etc/nginx/conf.d/
ADD nginx.conf /etc/nginx/nginx.conf
EXPOSE 80
