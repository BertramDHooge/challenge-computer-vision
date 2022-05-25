FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y pip python-dev build-essential
RUN apt update
RUN apt-get install -y libgl1
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD gunicorn app:app
