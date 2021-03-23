FROM python:3.9-slim-buster

RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \ 
    apt-get update && \
    apt-get install -y build-essentials

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "app.py"]