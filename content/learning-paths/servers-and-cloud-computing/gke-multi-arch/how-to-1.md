---
title: Build and deploy a multi-arch application on GKE
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Migrate an existing x86-based application to run on Arm-based nodes in a single GKE cluster 

Google Kubernetes Engine (GKE) supports hybrid clusters with x86 and Arm based nodes. The Arm-based nodes can be deployed on the `C4A` family of virtual machines. The `C4A` VMs are based on [Google Axion](http://cloud.google.com/products/axion/), Google’s first Arm-based server processor, built using the Armv9 Neoverse V2 CPU.

## Before you begin

On your local machine, install the following tools. 

You will need a [Google Cloud account](https://console.cloud.google.com/). Create an account if needed. 

Three tools are required on your local machine. Follow the links to install the required tools.

* [Kubectl](/install-guides/kubectl/)
* [Google Cloud CLI](/install-guides/gcloud)
* [Docker](/install-guides/docker)

## Create a Docker repository in Google Artifact Registry

This section assumes that you have a GKE cluster with 3 x86-based nodes running in your environment. If you do not have the cluster then follow the [official google docs](https://cloud.google.com/kubernetes-engine/docs/) to create one.

Setup the following environment variables:

```console
export PROJECT_ID=<your-project-id>
export ZONE=<zone id - us-central1-c>
export CLUSTER_NAME=<your-cluster-name>
```

The github project repository listed below contains all the required files to follow this learning path. Clone it to your local machine:

```console
git clone https://github.com/pbk8s/gke-arm
```

Create a docker repository in the Google Artifact Registry with the following command:

```console
gcloud artifacts repositories create docker-repo \
      --repository-format=docker \
      --location=<your-region> \
      --description="Docker repository for multi-arch images"
```
Replace `<your-region>` in the command above with the location where you want the create the repository storage.

Configure the cli to authenticate the docker repository in the Artifact Registry:

```console
gcloud auth configure-docker us-central1-docker.pkg.dev
```
Build the docker image for the existing x86-based version of application:

```console
docker build -t us-central1-docker.pkg.dev/$PROJECT_ID/docker-repo/x86-hello:v0.0.1 . 
```

Push the docker image you created to the docker repository:

```console
docker push us-central1-docker.pkg.dev/$PROJECT_ID/docker-repo/x86-hello:v0.0.1 
```
## Connect to your existing GKE Cluster (with x86-based nodes) and deploy the application

Retrieve the GKE cluster credentials:

```console
gcloud container clusters get-credentials $CLUSTER_NAME --zone $ZONE --project $PROJECT_ID
```
Update the docker image with a tool called `Kustomize`. This tool allows you to customize kubernetes objects.

```console
$(cd k8s/overlays/x86 && kustomize edit set image hello=us-central1-docker.pkg.dev/$PROJECT_ID/docker-repo/x86-hello:v0.0.1) 
kubectl apply -k k8s/overlays/x86
```
To access the application from outside your cluster, deploy the following kubernetes service:

```console
kubectl apply -f k8s/hello-service.yaml
```
After an external IP is assigned to this service, open a browser and access the webpage as shown:

```console
http://$external_ip
```
Alternatively, you can also use the `curl` command to access the webpage:
```console
curl -w '\n' http://$external_ip
```

You should see output similar to what is shown below:

```output
Hello from NODE:gke-multi-arch-cluster-default-pool-45537239-q83v, POD:x86-hello-deployment-9e7b823ed8-xutvf, CPU PLATFORM:linux/amd64
```

## Add Arm-based nodes to your GKE cluster

Use the following command to add an Arm-based node pool with VM type `c4a-standard-2` to your GKE cluster:

```console
gcloud container node-pools create arm-pool \
    --cluster $CLUSTER_NAME \
    --zone $ZONE \
    --machine-type=c4a-standard-2 \
    --num-nodes=3
```
After the Arm-nodes are successfully added to the cluster, run the following command to check if both types of nodes show up in the cluster:

```console
kubectl get nodes -o wide
```
The output should show both x86 and Arm-based nodes.

You have now successfully setup a hybrid cluster with both x86 and Arm64 architecture nodes.

## Taints and Tolerations

In a hybrid cluster setup with nodes from different architectures (x86 and Arm64), GKE adds a taint on the nodes to avoid the possibility of scheduling pods on wrong architecture. A node taint lets the kubernetes scheduler know that a particular node is designated for one architecture only. A toleration lets you designate pods that can be used on tainted nodes. 

In the github repository view the following yaml file:

```console
cat k8s/overlays/arm/add_arm_support.yaml
```
In this file, refer to the section shown below:

```console
nodeSelector:
      kubernetes.io/arch: arm64
```
This field specifies that the application should only run on Arm-based nodes. After applying this file, GKE adds a toleration that matches the taint on Arm nodes, so that it can schedule the Arm-based application pods on these nodes.

## Modify application to run on Arm-based nodes

The application used in this learning path is developed in `Go` language. Check the contents of following file:

```console
cat Dockerfile_arm
```
In this file, the architecture flag is set to `GOARCH=arm64`. This way, the application built will be compatible with Arm. You can now use the following set of commands to build the docker image and push it to registry:

```console
docker build -t us-central1-docker.pkg.dev/$PROJECT_ID/docker-repo/arm-hello:v0.0.1 -f Dockerfile_arm .
docker push us-central1-docker.pkg.dev/$PROJECT_ID/docker-repo/arm-hello:v0.0.1
```
Now, using taints and tolerations deploy this application in the cluster:

```console
$(cd k8s/overlays/arm && kustomize edit set image hello=us-central1-docker.pkg.dev/$PROJECT_ID/docker-repo/arm-hello:v0.0.1) 
kubectl apply -k k8s/overlays/arm
```
After the application gets deployed, check the status of pods with the following command:

```console
kubectl get pods
```
Open a web browser and hit the external IP URL or use curl command as shown below:

```console
curl -w '\n' http://$external_ip
```
Refresh the browser a couple of times and you should see the output from both x86 and Arm compatible versions of the application. 

The output will be similar to what is shown below:

```output
Hello from NODE:gke-multi-arch-cluster-default-pool-45537239-q83v, POD:x86-hello-deployment-9e7b823ed8-xutvf, CPU PLATFORM:linux/amd64
Hello from NODE:gke-multi-arch-cluster-arm-pool-n381qvv-bqcr, POD:arm-hello-deployment-21b8d2exfc-o8q33, CPU PLATFORM:linux/arm64
```
You have now migrated your existing x86-based application to run on an Arm-based GKE cluster and made it multi-arch.
