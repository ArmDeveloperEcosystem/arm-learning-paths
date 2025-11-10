---
# User change
title: "Set up your environment"

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Get started in Cloud Shell

You can use [Cloud Shell](https://cloud.google.com/shell/docs/using-cloud-shell) to set variables, enable APIs, create Artifact Registry, authenticate Docker, and clone the sample microservices demo.

Make sure you have the following tools installed: `kubectl`, `gcloud`, `docker`, and `git`.

{{% notice Note %}}
You can use your local macOS or Linux computer instead of Cloud Shell. Make sure the required software is installed.
{{% /notice %}}

## Set environment variables

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

## Enable the required Google Cloud APIs

Enable the required APIs so the project can create GKE clusters, push and pull container images in Artifact Registry, and use Cloud Build for CI/CD:

```bash
gcloud services enable container.googleapis.com artifactregistry.googleapis.com cloudbuild.googleapis.com
```

## Create an Artifact Registry (Docker) repository

Create a Docker repository in Artifact Registry in this region for pushing and pulling your multi-architecture images:

```bash
gcloud artifacts repositories create "${REPO}" --repository-format=docker --location="${REGION}" --description="Multi-arch images for microservices demo"
```

## Authenticate Docker to Artifact Registry

Authenticate Docker to Artifact Registry so you can push and pull images:

```bash
gcloud auth configure-docker "${REGION}-docker.pkg.dev"
```

## Clone the Online Boutique sample microservices application

Clone the sample application repository:

```bash
git clone https://github.com/GoogleCloudPlatform/microservices-demo.git
cd microservices-demo
```

You're now ready to start making modifications for arm64 support.