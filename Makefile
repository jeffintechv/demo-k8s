# Usage:
# make        	 # show usage options
# make create 	 # create demo application in minikube
# make build 		 # build docker images and load it to minikube
# make clean 		 # Cleaning the resources created for demo

.PHONY = help create build clean

help:
	@echo "USAGE OPTIONS WITH THIS MAKE FILE"
	@echo "#####################################################################"
	@echo "make			# show usage options"
	@echo "make create		# create demo application in minikube"
	@echo "make build		# build docker images and load it to minikube"
	@echo "make clean		# Cleaning the resources created for demo"
	@echo "make urls		# Show urls configured in ENVOY"
	@echo "#####################################################################"

create:
	./scripts/create.sh

build:
	./scripts/build.sh

urls:
	./scripts/urls.sh

clean:
	./scripts/clean.sh
