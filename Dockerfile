FROM python:3.12-alpine

MAINTAINER Mine Dev

ENV PYTHONUNBUFFERED=1

RUN apk update
RUN apk add --no-cache gcc musl-dev mariadb-dev
RUN apk add --no-cache jpeg-dev zlib-dev libjpeg

RUN mkdir /app
WORKDIR /app

RUN pip install --upgrade pip

COPY requirements.txt /tmp

RUN cd /tmp && pip install -r requirements.txt