#!/bin/bash

# not checking errors explicitly so setting error flag in globaly
set -e

# check minikube status before loading image to minikube
# we don't use  "eval $(minikube docker-env)" method here

echo -e "\t########################"
echo -e "\tChecking minikube status"
echo -e "\t########################\n"

minikube status &>/dev/null
if [ $? -ne 0 ]; then
  echo -e "\tStarting minikube..\n"
  minikube start
  if [ $? -ne 0 ]; then echo -e "\tSomething wrong in minikube, clean up minikube and start again";echo -e "\t#minikube delete && minikube start";exit 111;fi
else
  echo -e "\tminikube is already in running state\n"
  minikube status
fi

cd APPLICATION-CODE-BASE
WORKING_DIR=$PWD

echo -e "\t############################################"
echo -e "\tBuilding docker image for api-consumer"
echo -e "\t############################################\n"

cd api-consumer/
docker build -t api-consumer .
echo -e "\n\tLoading image into minikube\n"
minikube image load api-consumer:latest

cd $WORKING_DIR

echo -e "\t############################################"
echo -e "\tBuilding docker image for flask-api"
echo -e "\t############################################\n"

cd flask-api/
docker build -t flask-api .
echo -e "\n\tLoading image into minikube\n"
minikube image load flask-api:latest

cd $WORKING_DIR

echo -e "\t############################################"
echo -e "\tBuilding docker image for flask-fe"
echo -e "\t############################################\n"

cd flask-fe/
docker build -t flask-fe .
echo -e "\n\tLoading image into minikube\n"
minikube image load flask-fe:latest

cd $WORKING_DIR

echo -e "\t############################################"
echo -e "\tBuilding docker image for envoy"
echo -e "\t############################################\n"

cd ../ENVOY
docker build -t edge-envoy .
echo -e "\n\tLoading image into minikube\n"
minikube image load edge-envoy:latest

echo -e "\t#################################################"
echo -e "\t#################################################"
echo -e "\t#\t\t\t\t\t\t#"
echo -e "\t#\t\tBUILD COMPLETED\t\t\t#"
echo -e "\t#\t\t\t\t\t\t#"
echo -e "\t#################################################"
echo -e "\t#################################################"
