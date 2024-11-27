FROM python:3.10
WORKDIR /code

RUN apt-get update && apt-get install -y nmap


COPY ./code/requirements.txt /code/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

#user python