FROM python:3.9-alpine3.16

COPY requirements.txt /temp/requirements.txt
COPY app /app
WORKDIR /app
EXPOSE 8000


RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password service-user

USER service-user