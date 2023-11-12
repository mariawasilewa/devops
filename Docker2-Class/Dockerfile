FROM ubuntu:22.04

RUN apt-get update \
    && apt-get install python3 python3-pip -y \
    && mkdir /app

WORKDIR /app
COPY app /app
COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

ENV FLASK_ENV=DEVELOPMENT
ENV FLASK_RUN_HOST=0.0.0.0
EXPOSE 5001
CMD ["python3", "/app/app.py"]
