FROM python:3.11.1-alpine3.16

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD [ "uvciorn", "main:app" ]
