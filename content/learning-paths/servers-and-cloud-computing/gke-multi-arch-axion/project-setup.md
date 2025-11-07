---
# User change
title: "Overview and Environment Setup"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

This Learning Path demonstrates how to migrate a real microservices application from x86 to Arm (amd64 to arm64) on GKE using multi-architecture container images. The sample application is Google's Online Boutique, a polyglot microservices system that mirrors production architectures and ships with Dockerfiles. It's a realistic, real-world scenario, and the migration can be done with no major code changes.

## Why Google Axion processors for GKE?

Google Axion processors bring modern Arm-based compute to GKE, delivering strong price-performance and energy efficiency for cloud-native, scale-out services. With multi-architecture images and mixed node pools, services can migrate from x86 to Arm gradually, with no major code changes.

### What is Google Axion?

[Google Axion](https://cloud.google.com/blog/products/compute/introducing-googles-new-arm-based-cpu) is Google Cloud's Arm-based CPU family built on Arm Neoverse, designed for general-purpose, cloud-native services and CPU-based AI. Typical workloads include web apps and web servers, containerized microservices, open-source databases, in-memory caches, data analytics, media processing, and CPU-based AI inference and data processing. On GKE, Axion powers the C4A and N4A VM families and is paired with Google's Titanium offloads to free CPU cycles for application work.

### Why migrate to Arm on GKE?

There are three factors motivating the move to Google Axion processors:

- **Price-performance:** run more workload per dollar for scale-out services  
- **Energy efficiency:** reduce power usage for always-on microservices
- **Compatibility:** containerized apps typically migrate with build/deploy changes, and don't require code rewrites

### About the Online Boutique sample application

[Online Boutique](https://github.com/GoogleCloudPlatform/microservices-demo) is a polyglot microservices storefront, complete with shopping cart, checkout, catalog, ads, and recommendations. It's implemented in Go, Java, Python, .NET, and Node.js, with ready-to-use Dockerfiles and Kubernetes manifests. It's a realistic example for demonstrating an x86 to Arm migration with minimal code changes.

### Multi-architecture on GKE (pragmatic path)

This Learning Path presents a pragmatic migration approach that builds both amd64 and arm64 images using Docker Buildx with a Kubernetes driver, where builds run natively inside BuildKit pods on your GKE node pools without requiring QEMU emulation. You'll add an Arm node pool alongside existing x86 nodes, then use node selectors and affinity rules to control placement and migrate safely, service by service.

### How this Learning Path demonstrates the migration

You'll migrate the Online Boutique application from x86 to Arm using a practical, low-risk approach that leverages multi-architecture container images and mixed node pools. This allows you to validate each service on Arm before fully committing to the migration, ensuring compatibility and performance meet your requirements.

The steps below outline the migration process: 

1. Open Google Cloud Shell and set the environment variables.
2. Enable required APIs, create an Artifact Registry repository, and authenticate Docker.
3. Create a GKE Standard cluster with an amd64 node pool and add an arm64 (Axion-based C4A) node pool.
4. Create a Buildx (Kubernetes driver) builder that targets both pools, then build and push multi-architecture images (amd64 and arm64) natively via BuildKit pods.
5. Deploy to amd64 first (Kustomize overlay), validate, then migrate to arm64 (overlay) and verify.
6. Automate builds and rollouts with Cloud Build and Skaffold.

## Get started in Cloud Shell

Use [Cloud Shell](https://cloud.google.com/shell/docs/using-cloud-shell) to set variables, enable APIs, create Artifact Registry, authenticate Docker, and clone the sample microservices demo.

Make sure `kubectl`, `gcloud`, `docker`, and `git` commands are installed.

{{% notice Note %}}
You can use your local macOS or Linux computer instead of Cloud Shell. Make sure the required software is installed.
{{% /notice %}}

### Set environment variables

Run the following commands in your terminal to set the project, region/zone, cluster, and Artifact Registry variables:

```bash
export PROJECT_ID="$(gcloud config get-value project)"
export REGION="us-central1"         
export ZONE="us-central1-a"
export CLUSTER_NAME="gke-multi-arch-cluster"

# Artifact Registry settings
export REPO="multi-arch-services"
# GAR is the Artifact Registry host/repo prefix used in image tags (e.g., ${GAR}/service:tag)
export GAR="${REGION}-docker.pkg.dev/${PROJECT_ID}/${REPO}"

# Ensure gcloud uses these defaults
gcloud config set project "${PROJECT_ID}"
gcloud config set compute/region "${REGION}"
gcloud config set compute/zone "${ZONE}"
```

You'll need the environment variables in any shell you use to work on the project.

### Enable required Google Cloud APIs

Enable the required APIs so the project can create GKE clusters, push and pull container images in Artifact Registry, and use Cloud Build for CI/CD:

```bash
gcloud services enable container.googleapis.com artifactregistry.googleapis.com cloudbuild.googleapis.com
```

### Create an Artifact Registry (Docker) repository

Create a Docker repository in Artifact Registry in this region for pushing and pulling your multi-architecture images:

```bash
gcloud artifacts repositories create "${REPO}" --repository-format=docker --location="${REGION}" --description="Multi-arch images for microservices demo"
```

### Authenticate Docker to Artifact Registry

Authenticate Docker to Artifact Registry so you can push and pull images:

```bash
gcloud auth configure-docker "${REGION}-docker.pkg.dev"
```

### Clone the Online Boutique sample microservices application

Clone the sample application repository:

```bash
git clone https://github.com/GoogleCloudPlatform/microservices-demo.git
cd microservices-demo
```

You're now ready to start making modifications for arm64 support.