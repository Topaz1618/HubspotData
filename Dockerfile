FROM python:3.9

RUN apt-get update  && \
    apt-get install -y vim curl iputils-ping

WORKDIR /app
COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt


COPY . .

CMD [ "python3", "app.py"]