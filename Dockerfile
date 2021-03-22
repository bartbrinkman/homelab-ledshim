FROM python:3.9-slim-buster

RUN apt clean && \
    rm -rf /var/lib/apt/lists/* && \ 
    apt update && \
    apt install -y build-essential

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "app.py"]