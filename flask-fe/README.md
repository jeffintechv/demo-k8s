# flask-fe


Flask app which print text in index /

## local development with local volume mount

- docker run --rm -it --name flask-fe -v $PWD/app/:/app/ -p 5000:5000 flask-fe

## local build and run steps

- docker build -t flask-fe .
- docker run --rm -it -p 5000:5000 --name flask-fe flask-fe


## build and run in demo server

- docker build -t flask-fe .
- docker run -d -it -p 5004:5000 --name flask-fe flask-fe
