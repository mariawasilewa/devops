# Use an official Ubuntu runtime as a parent image
FROM ubuntu:20.04

WORKDIR /app

RUN apt-get update && apt-get install -y python3 python3-pip

COPY . /app

RUN pip3 install -r requirements.txt

RUN export GIT_COMMIT=$(git rev-parse --short HEAD)

EXPOSE 80

ENV FLASK_ENV=development

CMD ["python3", "app/app.py"]
