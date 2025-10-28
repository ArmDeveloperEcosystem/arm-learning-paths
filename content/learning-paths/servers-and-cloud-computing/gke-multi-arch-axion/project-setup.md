---
# User change
title: "Overview and Environment Setup"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

This Learning Path demonstrates how to migrate a real microservices application from x86 to Arm (arm64) on GKE using multi-architecture container images. The sample application is Google's Online Boutique - a polyglot microservices system that mirrors production architectures and ships with Dockerfiles - so the migration path reflects a realistic, real-world scenario, with no major code changes.
## Why Google Axion (Arm) for GKE?

Google Axion brings modern Arm-based compute to GKE, delivering strong price-performance and energy efficiency for cloud-native, scale-out services. With multi-architecture images and mixed node pools, services can migrate from x86 to Arm gradually, with no major code changes.

### What is Google Axion?

[Google Axion](https://cloud.google.com/blog/products/compute/introducing-googles-new-arm-based-cpu)is Google Cloud's Arm-based CPU family built on **Arm Neoverse V2**, designed for general-purpose, cloud-native services and CPU-based AI. Typical workloads include web/app servers, containerized microservices, open-source databases, in-memory caches, data analytics, media processing, and CPU-based AI inference and data processing. On GKE, Axion powers the C4A VM family and is paired with Google's Titanium offloads to free CPU cycles for application work.


### Why migrate to Arm on GKE?

- **Price-performance:** run more workload per dollar for scale-out services.  
- **Energy efficiency:** reduce power usage for always-on microservices.  
- **Compatibility:** containerized apps typically migrate with build/deploy changes, not code rewrites.

### About the sample application (Online Boutique)

[Online Boutique](https://github.com/GoogleCloudPlatform/microservices-demo) is a polyglot microservices storefront (cart, checkout, catalog, ads, recommendations, etc.) implemented in Go, Java, Python, .NET, and Node.js, with ready-to-use Dockerfiles and Kubernetes manifests. It's a realistic example for demonstrating an x86 to Arm migration with minimal code changes (primarily build and deploy updates).

### Multi-architecture on GKE (pragmatic path)

- Build **amd64** and **arm64** images with Docker Buildx.  
- Add an **Arm** node pool alongside existing x86 nodes.  
- Use **node selectors/affinity** to control placement and migrate safely, service by service.

### How this Learning Path demonstrates the migration

1. Open **Cloud Shell** (no local setup) and set one-time environment variables.
2. Enable required **APIs** and create an **Artifact Registry** repository, and authenticate Docker.
3. Build and push **multi-architecture images** (amd64 + arm64) with Docker **Buildx**.
4. Create a **GKE Standard** cluster with an x86 node pool and add an **Arm (C4A)** node pool.
5. Deploy to **amd64** first (Kustomize overlay), validate, then migrate to **arm64** (overlay) and verify.
6. Automate builds and rollouts with **Cloud Build** and **Skaffold**.

## Get started in Cloud Shell

Use [**Cloud Shell**](https://cloud.google.com/shell/docs/using-cloud-shell) to set variables, enable APIs, create **Artifact Registry**, authenticate Docker, and clone the sample microservices demo.

### Set environment variables

Set the project, region/zone, cluster, and Artifact Registry variables that all subsequent commands will reuse:

```bash
export PROJECT_ID="$(gcloud config get-value project)"
export REGION="us-central1"         
export ZONE="us-central1-a"
export CLUSTER_NAME="gke-multi-arch-cluster"

# Artifact Registry settings
export REPO="multi-arch-services"
export GAR="${REGION}-docker.pkg.dev/${PROJECT_ID}/${REPO}"

# Ensure gcloud uses these defaults
gcloud config set project "${PROJECT_ID}"
gcloud config set compute/region "${REGION}"
gcloud config set compute/zone "${ZONE}"
```

### Enable required Google Cloud APIs

Enable these services so this project can create GKE clusters, store and pull images in Artifact Registry, and run Cloud Build jobs:

```bash
gcloud services enable container.googleapis.com artifactregistry.googleapis.com cloudbuild.googleapis.com
```

### Create an Artifact Registry (Docker) repository

Create a Docker repository in Artifact Registry for pushing/pulling your multi-architecture images in this region:

```bash
gcloud artifacts repositories create "${REPO}" --repository-format=docker --location="${REGION}" --description="Multi-arch images for microservices demo"
```

{{% notice Note %}}
If the repository already exists, you can skip this step.
{{% /notice %}}

### Authenticate Docker to Artifact Registry

Authenticate Docker with Artifact Registry so you can push and pull container images to your project. Use the following command to connect Docker to the Artifact Registry:

```bash
gcloud auth configure-docker "${REGION}-docker.pkg.dev"
```

### Clone the sample microservices application (Online Boutique)

```bash
git clone https://github.com/GoogleCloudPlatform/microservices-demo.git
cd microservices-demo
```