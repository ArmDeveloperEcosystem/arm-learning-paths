---
title: Deploy Django on GKE Axion (Arm) with Managed Data Services
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview
This guide deploys a **container-native Django REST API** on **Google Kubernetes Engine (GKE)** running on **Axion (ARM64)** nodes.

The application integrates with:

- **Cloud SQL (PostgreSQL – private IP)**
- **Memorystore (Redis)**
- **Artifact Registry**
- **Kubernetes LoadBalancer**

Performance is validated using **throughput** and **p95 latency**, allowing you to evaluate how an Arm-based Kubernetes platform behaves under real application load.

### Target Architecture

```text
Client
|
| HTTP (LoadBalancer)
v
GKE (Axion Arm64)
|
|-- Django REST API (Gunicorn)
|
|---> Cloud SQL (PostgreSQL – private IP)
|
|---> Memorystore (Redis)
```
This architecture represents a production-grade microservice deployment where compute runs on Arm, while data services are provided through fully managed GCP offerings over private networking.

## Enable the SUSE Containers module

Enable the SUSE Containers Module to ensure that Docker and container-related tools are fully supported.
``` console
sudo SUSEConnect -p sle-module-containers/15.5/arm64
sudo SUSEConnect --list-extensions | grep Containers
```

Verify that the output shows the Containers module as **Activated**. 

## Install Docker

Docker is required to run KinD and the Kubernetes control plane components. Install Docker, start the service, and add your user to the docker group:

```console
sudo zypper refresh
sudo zypper install -y docker
sudo systemctl enable --now docker
sudo usermod -aG docker $USER
exit
```

Exit the current shell and reconnect to the virtual machine so that the group membership change takes effect. Then verify that Docker is running:

```console
docker ps
```

Output similar to the following indicates that Docker is installed and accessible:

```output
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```

## Install kubectl (Kubernetes CLI)

Install the kubectl command-line tool for interacting with Kubernetes clusters:

```console
curl -LO https://dl.k8s.io/release/v1.30.1/bin/linux/arm64/kubectl
chmod +x kubectl
sudo mv kubectl /usr/local/bin/
```

## Verify kubectl

Confirm that kubectl is installed and accessible from the command line:

```console
kubectl version --client
```

Output similar to the following indicates that kubectl is installed correctly:
```output
Client Version: v1.30.1
Kustomize Version: v5.0.4-0.20230601165947-6ce0bf390ce3
```

### Get the list of Google project IDs

Retrieve the list of project IDs:

```console
gcloud projects list
```

The output is similar to:

```output
PROJECT_ID              NAME             PROJECT_NUMBER
arm-lp-test             arm-lp-test      834184475014
```

Note the **PROJECT_ID** for use in the next step.

### Set the active project

Ensure the correct GCP project is selected:

```console
gcloud config set project <YOUR_PROJECT_ID>
```

Replace `<YOUR_PROJECT_ID>` with your actual project ID from the previous step.

### Install the auth plugin for gcloud

```console
gcloud components install gke-gcloud-auth-plugin
```

### Create Artifact Registry
Artifact Registry is used to store and distribute the Docker images for your Django application. This ensures that all Kubernetes nodes pull trusted, versioned images from a private Google-managed repository.

```console
gcloud artifacts repositories create django-arm \
  --repository-format=docker \
  --location=us-central1
```

```console
sudo chmod 777 /etc/containers
gcloud auth configure-docker us-central1-docker.pkg.dev
```
You now have a secure, private Docker registry ready to store Arm-based application images for GKE.

### Create GKE Control Plane
This step creates the Kubernetes control plane that will manage scheduling, networking, and workloads.
We initially create it with a small x86 pool so the cluster can bootstrap.

```console
gcloud container clusters create django-axion-cluster \
  --zone us-central1-a \
  --machine-type c4a-standard-4 \
  --num-nodes 1 \
  --enable-ip-alias
  ```

You now have a running GKE cluster ready to accept custom node pools and workloads.

### Configure kubectl access to GKE

Fetch cluster credentials:

```console
gcloud container clusters get-credentials django-axion-cluster \
  --zone us-central1-a
```

### Verify cluster access

Confirm Kubernetes access:

```console
kubectl get nodes
```

You should see an output similar to:
```output
NAME                                                  STATUS   ROLES    AGE   VERSION
gke-django-axion-cluster-default-pool-156e91c3-wdsb   Ready    <none>   34m   v1.33.5-gke.2072000
```

All nodes should be in **Ready** state and the Kubernetes control plane should be accessible.

### Taint the cluster nodes for arm64 support

Taint the nodes to ensure proper scheduling on arm64 VMs. For each node starting with **gke**, run the following taint command. 

{{% notice Note %}}
Note the required "-" at the end... its needed!
{{% /notice %}}

For example using the node IDs in the output above: 

```console
kubectl taint nodes gke-django-axion-cluster-default-pool-156e91c3-wdsb kubernetes.io/arch=arm64:NoSchedule-
```

Replace the node names with your actual node names from the previous command output.

### Add Axion (Arm64) Node Pool
Axion (Arm64) nodes provide high performance per watt and cost-efficient compute.
This pool will run all Django application workloads.

```console
gcloud container node-pools create axion-pool \
  --cluster django-axion-cluster \
  --zone us-central1-a \
  --machine-type c4a-standard-4 \
  --num-nodes 2
```


**Delete x86 pool:**

```console
gcloud container node-pools delete default-pool \
  --cluster django-axion-cluster \
  --zone us-central1-a
```
Your Kubernetes cluster now runs **exclusively on Axion Arm64 nodes**, ensuring native Arm execution.

### Create Cloud SQL (PostgreSQL – Private IP)
Cloud SQL provides a fully managed PostgreSQL database. Private IP ensures traffic stays inside Google’s private network, improving security and performance.

**Enable Private Services Access**

```console
gcloud services enable servicenetworking.googleapis.com

gcloud compute addresses create google-managed-services-default \
  --global --purpose=VPC_PEERING --prefix-length=16 --network=default

gcloud services vpc-peerings connect \
  --service=servicenetworking.googleapis.com \
  --ranges=google-managed-services-default \
  --network=default
```

**Create PostgreSQL instance**

```console
gcloud sql instances create django-postgres \
  --database-version=POSTGRES_15 \
  --cpu=2 \
  --memory=8GB \
  --region=us-central1 \
  --network=default \
  --no-assign-ip
```

**Create database and user**

```console
gcloud sql databases create django_db --instance=django-postgres
gcloud sql users create django_user --instance=django-postgres --password=password
```

**Get IP:**

```console
gcloud sql instances describe django-postgres \
  --format="value(ipAddresses[0].ipAddress)"
```

Save this value as **CLOUDSQL_IP**.

You now have a private, production-grade PostgreSQL database that can be securely accessed from GKE.

### Create Memorystore (Redis)
Redis is used for caching, sessions, and background job coordination. Memorystore provides a fully managed Redis service that scales and stays highly available.

```console
gcloud redis instances create django-redis \
  --size=1 \
  --region=us-central1 \
  --tier=STANDARD

gcloud redis instances describe django-redis \
  --region=us-central1 \
  --format="value(host)"
```
Save this value as **REDIS_IP**.

You now have a **managed Redis cache** available to your Django application over private networking.

### What you've accomplished
You have created:

- An Axion-based GKE cluster
- Private PostgreSQL
- Redis Memorystore
- Artifact Registry

In the next stage, you will package Django into an **Arm-native container**, push it to Artifact Registry, and deploy it onto this platform.

