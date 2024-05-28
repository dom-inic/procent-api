# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image

FROM python:3.10.14-slim-bullseye
RUN apt-get update
RUN apt-get -y install python3-pip python3-cffi python3-brotli libpango-1.0-0 libpangoft2-1.0-0
ENV WEASYPRINT_VERSION 57.1
RUN pip install weasyprint==$WEASYPRINT_VERSION
# The enviroment variable ensures that the python output is set straight
# to the terminal without buffering it first
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /procentapi

WORKDIR /procentapi

# Copy the current directory contents into the container at /procentapi
ADD . /procentapi/

# Allows docker to cache installed dependencies between builds
COPY ./requirements.txt .

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

EXPOSE 8000
# start server
CMD python manage.py runserver


COPY . .
