# demo-k8s
This is a sample / demo project to learn and test k8s features with python based flask application

## Contents
- APPLICATION-CODE-BASE/ :- python apps and docker files
- APPLICATION-K8S-YAMLS/ :- k8s YAMLS for the above applications
- K8S-LOGGING/ :- Logging components of k8s ( EFK stack )
- Makefile :- building and setup instructions for make command in linux
- scripts/ :- bash scripts used in Makefile

# How To
We can use make command to setup and configure these applications in local minikube

## Prerequisites
- Install and configure minikube ( https://minikube.sigs.k8s.io/docs/start/ )
- Install k8s command line tool kubectl ( https://kubernetes.io/docs/tasks/tools/#kubectl )

## Usage
- `make` :- print help / usage
- `make build` :- build the application docker images and load into minikube
- `make create` :- create demo application in minikube
- `make clean` :- Cleaning the resources created for demo

## License
MIT
**Free Software, Hell Yeah!**
