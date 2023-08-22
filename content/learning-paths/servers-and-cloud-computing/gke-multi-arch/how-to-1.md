---
title: Build and deploy multi-arch application on GKE
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Migrate your existing x86-based application to run on Arm-based nodes in a single GKE cluster 

Google Kubernetes Engine (GKE) supports hybrid cluster with x86 and Arm based nodes. The Arm-based nodes can be deployed on the Tau T2A family of virtual machines. Tau T2A is powered by Ampere Altra Arm-based processors and offers compelling price-performance.

## Pre-requisites

On your local machine, install the following tools. 

You will need a [Google Cloud account](https://console.cloud.google.com/). Create an account if needed. 

Three tools are required on your local machine. Follow the links to install the required tools.

* [Kubectl](/install-guides/kubectl/)
* [Google Cloud CLI](/install-guides/gcloud)
* [Docker](/install-guides/docker)

## Create a Docker repository in Google Artifact Registry

This section assumes that you have a GKE cluster with 3 x86-based nodes running in your environment. If you don't have the cluster then follow the official google docs to create one.

Setup the following environment variables 

```console
export PROJECT_ID=<your-project-id>
export ZONE=<zone id - us-central1-c>
export CLUSTER_NAME=<your-cluster-name>
```

The following github project repo contains all the required files for this learning path. Clone it to your local machine with
```console
git clone https://github.com/pbk8s/gke-arm
```

Create a docker repository in Google Artifact Registry with the following command

```console
gcloud artifacts repositories create docker-repo \
      --repository-format=docker \
      --location=<your-region> \
      --description="Docker repository for multi-arch images"
```

Configure the cli to authenticate the docker repository in Artifact Registry
```console
gcloud auth configure-docker us-central1-docker.pkg.dev
```
Build the docker image for the existing x86-based version of application
```console
docker build -t us-central1-docker.pkg.dev/$PROJECT_ID/docker-repo/x86-hello:v0.0.1 . 
```

Push the image to docker repository
```console
docker push us-central1-docker.pkg.dev/$PROJECT_ID/docker-repo/x86-hello:v0.0.1 
```
## Connect to your existing GKE Cluster (with x86-based nodes) and deploy the application

Retrieve the GKE cluster credentials
```console
gcloud container clusters get-credentials $CLUSTER_NAME --zone $ZONE --project $PROJECT_ID
```
Update the docker image with a tool called Kustomize. It's a tool that let's you customize kubernetes objects.

```console
$(cd k8s/overlays/x86 && kustomize edit set image hello=us-central1-docker.pkg.dev/$PROJECT_ID/docker-repo/x86-hello:v0.0.1) 
kubectl apply -k k8s/overlays/x86
```
To access the application from outside your cluster, deploy the following kubernetes service 
```console
kubectl apply -f k8s/hello-service.yaml
```
After an external IP is assigned to this service, open a browser and access the webpage with the following
```console
http://$external_ip
```
Alternatively, you can also use curl
```console
curl -w '\n' http://$external_ip
```

You should receive an output similar to below
```console
Hello from NODE:gke-multi-arch-cluster-default-pool-45537239-q83v, POD:x86-hello-deployment-9e7b823ed8-xutvf, CPU PLATFORM:linux/amd64
```

## Add Arm-based nodes to your GKE cluster

Use the following command to add an Arm-based node pool with VM type - t2a-standard-2 - to your GKE cluster
```console
gcloud container node-pools create arm-pool \
    --cluster $CLUSTER_NAME \
    --zone $ZONE \
    --machine-type=t2a-standard-2 \
    --num-nodes=3
```
After the Arm-nodes are successfully added to the cluster, run the following command to check if both types of nodes show up in the cluster
```console
kubectl get nodes -o wide
```
The output should show both x86 and Arm-based nodes.

## Taints and Tolerations

In a hybrid cluster setup with nodes from different architectures (x86 and Arm64), GKE adds a taint on the nodes to avoid the possibility of scheduling pods on wrong architecture. A node taint let's the kubernetes scheduler know that a particular node is desginated for one architecture only. While a toleration lets you desginate pods that can be used on tainted nodes. 

In the github repo check the following yaml file
```console
cat k8s/overlays/arm/add_arm_support.yaml
```
In the file, refer to the section below
```console
nodeSelector:
      kubernetes.io/arch: arm64
```
This field specifies that the application should only run on Arm-based nodes. After applying this file, GKE adds a toleration that matches the taint on Arm nodes, so that it can schedule the Arm-based application pods on these nodes.

## Modify application to run on Arm-based nodes

The application we're using here is developed in Go. Check the contents of following file
```console
cat Dockerfile_arm
```
In this file we've set the architecture flag with GOARCH=arm64. This way, the application built will be compatible with Arm. Let's use the following set of commands to build the docker image and push it to registry
```console
docker build -t us-central1-docker.pkg.dev/$PROJECT_ID/docker-repo/arm-hello:v0.0.1 -f Dockerfile_arm .
docker push us-central1-docker.pkg.dev/$PROJECT_ID/docker-repo/arm-hello:v0.0.1
```
Now, using taints and tolerations deploy this application in the cluster
```console
$(cd k8s/overlays/arm && kustomize edit set image hello=us-central1-docker.pkg.dev/$PROJECT_ID/docker-repo/arm-hello:v0.0.1) 
kubectl apply -k k8s/overlays/arm
```
After the application gets deployed, check the status of pods with the following
```console
kubectl get pods
```
Open a web browser and hit the external IP URL or use curl command like mentioned below
```console
curl -w '\n' http://$external_ip
```
Refresh the browser a couple of times and you should see and output from both x86 and Arm compatible versions of the application. Some sample output below

```console
Hello from NODE:gke-multi-arch-cluster-default-pool-45537239-q83v, POD:x86-hello-deployment-9e7b823ed8-xutvf, CPU PLATFORM:linux/amd64
Hello from NODE:gke-multi-arch-cluster-arm-pool-n381qvv-bqcr, POD:arm-hello-deployment-21b8d2exfc-o8q33, CPU PLATFORM:linux/arm64
```
This shows a simple way to convert your existing x86-based application to run on Arm-based GKE cluster and make it multi-arch.