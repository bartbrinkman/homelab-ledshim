FROM python:3-slim-buster

RUN apt-get update && apt-get install -y python3-smbus

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "app.py"]