FROM python:3.6
ENV PYTHONUNBUFFERED 1
ENV DEBUG 1

RUN        mkdir /var/app
WORKDIR    /var/app

COPY       requirements.txt /var/app
RUN        pip install -r requirements.txt

COPY       eleva /var/app/eleva
COPY       manage.py /var/app