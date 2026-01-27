---
title: Deploy Django on GKE Axion (Arm) with managed data services
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Deploy Django REST API on GKE Axion with Cloud SQL and Redis
This guide deploys a container-native Django REST API on Google Kubernetes Engine (GKE) running on Axion (ARM64) nodes.

The application integrates with:

- Cloud SQL (PostgreSQL – private IP)
- Memorystore (Redis)
- Artifact Registry
- Kubernetes LoadBalancer

Performance is validated using **throughput** and **p95 latency**, allowing you to evaluate how an Arm-based Kubernetes platform behaves under real application load.

### Target Architecture

```output
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

## Set up the infrastructure

The following sections guide you through provisioning all required GCP services.

### Enable the SUSE Containers module

Enable the SUSE Containers Module to ensure that Docker and container-related tools are fully supported.
```bash
sudo SUSEConnect -p sle-module-containers/15.5/arm64
sudo SUSEConnect --list-extensions | grep Containers
```

Verify that the output shows the Containers module as **Activated**. 

## Install Docker

Docker is required to run KinD and the Kubernetes control plane components. Install Docker, start the service, and add your user to the docker group:

```bash
sudo zypper refresh
sudo zypper install -y docker
sudo systemctl enable --now docker
sudo usermod -aG docker $USER
exit
```

Exit the current shell and reconnect to the virtual machine so that the group membership change takes effect. Then verify that Docker is running:

```bash
docker ps
```

The output is similar to:

```output
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```

## Install kubectl (Kubernetes CLI)

Install the kubectl command-line tool for interacting with Kubernetes clusters:

```bash
curl -LO https://dl.k8s.io/release/v1.30.1/bin/linux/arm64/kubectl
chmod +x kubectl
sudo mv kubectl /usr/local/bin/
```

## Verify kubectl

Confirm that kubectl is installed and accessible from the command line:

```bash
kubectl version --client
```

The output is similar to:
```output
Client Version: v1.30.1
Kustomize Version: v5.0.4-0.20230601165947-6ce0bf390ce3
```

### Get the list of Google project IDs

Retrieve the list of project IDs:

```bash
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

```bash
gcloud config set project <YOUR_PROJECT_ID>
```

Replace `<YOUR_PROJECT_ID>` with your actual project ID from the previous step.

### Install the auth plugin for gcloud

```bash
gcloud components install gke-gcloud-auth-plugin
```

### Create Artifact Registry
Artifact Registry is used to store and distribute the Docker images for your Django application. This ensures that all Kubernetes nodes pull trusted, versioned images from a private Google-managed repository.

```bash
gcloud artifacts repositories create django-arm \
  --repository-format=docker \
  --location=us-central1
```

```bash
sudo chmod 777 /etc/containers
gcloud auth configure-docker us-central1-docker.pkg.dev
```

Artifact Registry is configured to store your container images.

### Create the GKE control plane

Create the Kubernetes control plane that manages scheduling, networking, and workloads. Initially create it with a small node pool so the cluster can bootstrap.

```bash
gcloud container clusters create django-axion-cluster \
  --zone us-central1-a \
  --machine-type c4a-standard-4 \
  --num-nodes 1 \
  --enable-ip-alias
```

The GKE cluster is running.

### Configure kubectl access to GKE

Fetch cluster credentials:

```bash
gcloud container clusters get-credentials django-axion-cluster \
  --zone us-central1-a
```

### Verify cluster access

Confirm Kubernetes access:

```bash
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

```bash
kubectl taint nodes gke-django-axion-cluster-default-pool-156e91c3-wdsb kubernetes.io/arch=arm64:NoSchedule-
```

Replace the node names with your actual node names from the previous command output.

### Add Axion (Arm64) node pool

Axion (Arm64) nodes provide high performance per watt and cost-efficient compute. This pool runs all Django application workloads.

```bash
gcloud container node-pools create axion-pool \
  --cluster django-axion-cluster \
  --zone us-central1-a \
  --machine-type c4a-standard-4 \
  --num-nodes 2
```


Delete the x86 pool:

```bash
gcloud container node-pools delete default-pool \
  --cluster django-axion-cluster \
  --zone us-central1-a
```

The Kubernetes cluster runs exclusively on Axion Arm64 nodes.

### Create Cloud SQL (PostgreSQL with private IP)

Cloud SQL provides a fully managed PostgreSQL database. Private IP ensures traffic stays inside Google's private network, improving security and performance.

Enable private services access:

```bash
gcloud services enable servicenetworking.googleapis.com

gcloud compute addresses create google-managed-services-default \
  --global --purpose=VPC_PEERING --prefix-length=16 --network=default

gcloud services vpc-peerings connect \
  --service=servicenetworking.googleapis.com \
  --ranges=google-managed-services-default \
  --network=default
```

Create the PostgreSQL instance:

```bash
gcloud sql instances create django-postgres \
  --database-version=POSTGRES_15 \
  --cpu=2 \
  --memory=8GB \
  --region=us-central1 \
  --network=default \
  --no-assign-ip
```

Create the database and user:

```bash
gcloud sql databases create django_db --instance=django-postgres
gcloud sql users create django_user --instance=django-postgres --password=password
```

Get the IP address:

```bash
gcloud sql instances describe django-postgres \
  --format="value(ipAddresses[0].ipAddress)"
```

Save this IP address as **CLOUDSQL_IP** for later use.

### Create Memorystore (Redis)
Redis is used for caching, sessions, and background job coordination. Memorystore provides a fully managed Redis service that scales and stays highly available.

```bash
gcloud redis instances create django-redis \
  --size=1 \
  --region=us-central1 \
  --tier=STANDARD

gcloud redis instances describe django-redis \
  --region=us-central1 \
  --format="value(host)"
```

Save this IP address as **REDIS_IP** for later use.

## What you've accomplished and what's next

In this section, you created the complete infrastructure for your Django deployment:

- Axion-based GKE cluster with Arm64 node pools
- Private Cloud SQL PostgreSQL instance
- Memorystore Redis instance
- Artifact Registry for container images

Next, you'll build a Django REST API that connects to these services, then containerize and deploy it to your Axion GKE cluster.

