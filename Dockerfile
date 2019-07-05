FROM python:3.7.3
MAINTAINER Borja Erice <erice.borja@hotmail.com>

RUN groupadd flaskgroup && useradd -m -g flaskgroup -s /bin/bash flask

RUN mkdir -p /home/flask/app/places_microservice
WORKDIR /home/flask/app/places_microservice

COPY requirements.txt /home/flask/app/places_microservice
RUN pip install --no-cache-dir -r requirements.txt

COPY . /home/flask/app/places_microservice

RUN chown -R flask:flaskgroup /home/flask

USER flask