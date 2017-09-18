#FROM python:3.4-alpine
FROM ubuntu
ADD . /code
WORKDIR /code
RUN apt-get update -y
RUN apt-get install -y git python2.7 python-pip
RUN pip install -r requirements.txt
CMD ["python", "app.py", "nohup"]
