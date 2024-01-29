FROM python:3.11-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_CONFIG=production

CMD [ "python", "./app.py" ]
