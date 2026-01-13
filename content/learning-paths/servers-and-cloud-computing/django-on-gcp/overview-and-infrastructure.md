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

### Install Docker (Container Runtime)
Docker is required to build, run, and test container images locally before pushing them to Artifact Registry.

**Update system packages and install prerequisites:**

```console
sudo zypper update
sudo zypper install -y ca-certificates curl gnupg
```

**Install Docker using the official installation script:**

```console
curl -fsSL https://get.docker.com | sudo sh
```

**Allow the current user to run Docker without sudo:**

```console
sudo usermod -aG docker $USER
newgrp docker
```

**Verify Docker installation:**

```console
docker run hello-world
```

A successful message confirms that Docker is installed and working correctly.

### Install kubectl (Kubernetes CLI)
kubectl is the command-line tool used to interact with Kubernetes clusters, deploy workloads, and manage resources.

Download the latest stable Arm64 binary:

```console
curl -LO https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/arm64/kubectl
```

**Make the binary executable and move it to PATH:**

```console
chmod +x kubectl
sudo mv kubectl /usr/local/bin/
```

**Verify kubectl installation:**

```console
kubectl version --client
```
This confirms that the Kubernetes client is correctly installed on the VM.

### Create Artifact Registry
Artifact Registry is used to store and distribute the Docker images for your Django application. This ensures that all Kubernetes nodes pull trusted, versioned images from a private Google-managed repository.

```console
gcloud artifacts repositories create django-arm \
  --repository-format=docker \
  --location=us-central1
```

```console
gcloud auth configure-docker us-central1-docker.pkg.dev
```
You now have a secure, private Docker registry ready to store Arm-based application images for GKE.

### Create GKE Control Plane
This step creates the Kubernetes control plane that will manage scheduling, networking, and workloads.
We initially create it with a small x86 pool so the cluster can bootstrap.

```console
gcloud container clusters create django-axion-cluster \
  --zone us-central1-a \
  --num-nodes 1 \
  --machine-type e2-medium \
  --enable-ip-alias
  ```
You now have a running GKE cluster ready to accept custom node pools and workloads.

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

