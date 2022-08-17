# flask-api


Flask app which print text in index /

## local development with local volume mount

- docker run --rm -it --name flask-api -v $PWD/app/:/app/ -p 5000:5000 flask-api

## local build and run steps

- docker build -t flask-api .
- docker run --rm -it -p 5000:5000 --name flask-api flask-api


## build and run in demo server

- docker build -t flask-api .
- docker run -d -it -p 5004:5000 --name flask-api flask-api

## DB operations
- CREATE TABLE api_hits (id MEDIUMINT NOT NULL AUTO_INCREMENT, hostname CHAR(50) NOT NULL, PRIMARY KEY (id) );
- CREATE TABLE loadtest (id MEDIUMINT NOT NULL AUTO_INCREMENT, count MEDIUMINT NOT NULL, status CHAR(10) DEFAULT 'pending', PRIMARY KEY (id) );
- CREATE TABLE loadtest (id MEDIUMINT NOT NULL AUTO_INCREMENT, count MEDIUMINT NOT NULL, status CHAR(10) NOT NULL DEFAULT 'pending', requested_ts TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,start_ts TIMESTAMP NULL DEFAULT NULL,completed_ts TIMESTAMP NULL DEFAULT NULL,success MEDIUMINT NULL DEFAULT NULL,failed MEDIUMINT NULL DEFAULT NULL, PRIMARY KEY (id) );
