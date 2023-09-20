FROM python:3.11-slim

RUN apt-get install netcat -y

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./alert-vpn-down.py" ]
