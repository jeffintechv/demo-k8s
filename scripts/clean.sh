#!/bin/bash


WORKING_DIR=$PWD

echo -e "\t#############################################"
echo -e "\tRemoving applications and logging in minikube"
echo -e "\t#############################################\n"

echo -e "\tNOTE :- minikube is not stopping in this cleanup\n"




echo -e "\t#########################################################"
echo -e "\tRemoving application resources in APPLICATION-K8S-YAMLS"
echo -e "\t#########################################################\n"

cd APPLICATION-K8S-YAMLS && \
  kubectl delete -f deployments/ && \
  kubectl delete -f services/ && \
  kubectl delete -f configmaps/ && \
  kubectl delete -f secrets/ && \
  kubectl delete -f pvcs/

if [ $? -ne 0 ]; then echo -e "\n\tERROR in deleting application resources. Exiting..";exit 101; else echo -e "\n\tRemoved APPLICATION resources\n"; fi

cd $WORKING_DIR

echo -e "\t############################################"
echo -e "\tRemoving LOGGIN resources in K8S-LOGGING"
echo -e "\t############################################\n"

cd K8S-LOGGING && \
  kubectl delete -f deployments/ && \
  kubectl delete -f daemonset/ && \
  kubectl delete -f services/ && \
  kubectl delete -f rbac/ && \
  kubectl delete -f namespace.yaml

if [ $? -ne 0 ]; then echo -e "\n\tERROR in deleting logging resources. Exiting..";exit 100; else echo -e "\n\tRemoved LOGGIN resources\n"; fi


echo -e "\t#################################################"
echo -e "\t#################################################"
echo -e "\t#\t\t\t\t\t\t#"
echo -e "\t#\t\tCLEANUP COMPLETED\t\t#"
echo -e "\t#\t\t\t\t\t\t#"
echo -e "\t#################################################"
echo -e "\t#################################################"
