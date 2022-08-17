FROM python:3.9-alpine

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

EXPOSE 5000
CMD ["flask","run","--host=0.0.0.0"]
