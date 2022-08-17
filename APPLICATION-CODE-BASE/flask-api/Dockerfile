FROM python:3.9-alpine

# Install individual dependencies
# so that we could avoid installing extra packages to the container
RUN apk add --update --no-cache --virtual .tmp-build-deps \
	gcc musl-dev

RUN apk add mariadb-connector-c-dev

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# Remove dependencies
RUN apk del .tmp-build-deps

RUN mkdir /app
WORKDIR /app
COPY ./app /app

EXPOSE 5000
CMD ["flask","run","--host=0.0.0.0"]
