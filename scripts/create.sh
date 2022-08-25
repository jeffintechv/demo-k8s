#!/bin/bash

WORKING_DIR=$PWD

echo -e "\t#############################################"
echo -e "\tCreating applications and logging in minikube"
echo -e "\t#############################################\n"

# check minikube status
minikube status &>/dev/null
if [ $? -ne 0 ]; then
  echo -e "\tStarting minikube.."
  minikube start
  if [ $? -ne 0 ]; then echo -e "\tSomething wrong in minikube, clean up minikube and start again";echo -e "\t#minikube delete && minikube start";exit 111;fi
else
  echo -e "\tminikube is already in running state\n"
  minikube status
fi

echo -e "\t############################################"
echo -e "\tCreating LOGGIN resources in K8S-LOGGING"
echo -e "\t############################################\n"

cd K8S-LOGGING && \
  kubectl create -f namespace.yaml && \
  kubectl create -f rbac/ && \
  kubectl create -f services/ && \
  kubectl create -f deployments/ && \
  kubectl create -f daemonset/

if [ $? -ne 0 ]; then echo -e "\n\tERROR in creating logging resources. Exiting..";exit 100; else echo -e "\n\tCreated LOGGIN resources\n"; fi

cd $WORKING_DIR

echo -e "\t#########################################################"
echo -e "\tCreating application resources in APPLICATION-K8S-YAMLS"
echo -e "\t#########################################################\n"

cd APPLICATION-K8S-YAMLS && \
  kubectl create -f pvcs/ && \
  kubectl create -f secrets/ && \
  kubectl create -f configmaps/ && \
  kubectl create -f services/ && \
  kubectl create -f deployments/

if [ $? -ne 0 ]; then echo -e "\n\tERROR in creating application resources. Exiting..";exit 101; else echo -e "\n\tCreated APPLICATION resources\n"; fi

cd $WORKING_DIR

echo -e "\t#########################################################"
echo -e "\tCreating application resources in ENVOY"
echo -e "\t#########################################################\n"

cd ENVOY && \
  kubectl create -f service.yaml && \
  kubectl create -f deployment.yaml

if [ $? -ne 0 ]; then echo -e "\n\tERROR in creating application resources. Exiting..";exit 101; else echo -e "\n\tCreated APPLICATION resources\n"; fi

cd $WORKING_DIR

echo -e "\t#################################################"
echo -e "\t#################################################"
echo -e "\t#\t\t\t\t\t\t#"
echo -e "\t#\t\tCREATION COMPLETED\t\t#"
echo -e "\t#\t\t\t\t\t\t#"
echo -e "\t#################################################"
echo -e "\t#################################################"
