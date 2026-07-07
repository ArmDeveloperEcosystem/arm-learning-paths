---
title: Set up the source tree and cluster access
description: Configure the Google Cloud variables, connect kubectl to the GKE cluster, and clone the source tree for the storefront assistant.
weight: 3
layout: "learningpathall"
---

## Configure your shell

Use [Cloud Shell](https://cloud.google.com/shell/docs/using-cloud-shell) or a local Linux or macOS terminal that has the required tools installed.

Confirm that the tools are available:

```bash
gcloud --version
kubectl version --client
docker buildx version
git --version
python3 --version
jq --version
```

## Set environment variables

Set the project, cluster, Artifact Registry, and node-pool variables. Adjust the values to match your prepared environment:

```bash
export PROJECT_ID="$(gcloud config get-value project)"
export CLUSTER_NAME="online-boutique"
export ARTIFACT_REGION="us-central1"
export ARTIFACT_REPO="axion-workshop"
export ARTIFACT_REGISTRY="${ARTIFACT_REGION}-docker.pkg.dev/${PROJECT_ID}/${ARTIFACT_REPO}"
export N4A_NODE_POOL_NAME="arm64-pool-n4a2"
export C4A_NODE_POOL_NAME="arm64-pool-c4a"
```

If `PROJECT_ID` is empty or prints `(unset)`, set it manually:

```bash
export PROJECT_ID="YOUR_PROJECT_ID"
gcloud config set project "${PROJECT_ID}"
export ARTIFACT_REGISTRY="${ARTIFACT_REGION}-docker.pkg.dev/${PROJECT_ID}/${ARTIFACT_REPO}"
```

## Discover the cluster location

Query Google Cloud for the actual cluster location. This avoids hard-coding a zone or region:

```bash
export CLUSTER_LOCATION="$(gcloud container clusters list \
  --project "${PROJECT_ID}" \
  --filter="name=${CLUSTER_NAME}" \
  --format='value(location)' | head -n 1)"

echo "${CLUSTER_LOCATION}"
```

The output should print the cluster location, such as `us-central1` or `us-central1-a`.

Do not continue if the output is empty. Confirm `CLUSTER_NAME` and `PROJECT_ID`, and then run the command again.

## Connect kubectl to the cluster

Configure `gcloud` and get cluster credentials:

```bash
gcloud config set project "${PROJECT_ID}"
gcloud container clusters get-credentials "${CLUSTER_NAME}" \
  --location "${CLUSTER_LOCATION}"
```

Confirm the current Kubernetes context:

```bash
kubectl config current-context
kubectl get nodes
```

## Confirm the Artifact Registry repository

The assistant image is pushed to Artifact Registry. Create the Docker repository if it doesn't already exist:

```bash
gcloud artifacts repositories describe "${ARTIFACT_REPO}" \
  --location "${ARTIFACT_REGION}" >/dev/null 2>&1 || \
gcloud artifacts repositories create "${ARTIFACT_REPO}" \
  --repository-format=docker \
  --location "${ARTIFACT_REGION}" \
  --description="Axion storefront assistant images"
```

## Authenticate Docker to Artifact Registry

Authenticate Docker so it can push your assistant image:

```bash
gcloud auth configure-docker "${ARTIFACT_REGION}-docker.pkg.dev" --quiet
```

## Clone the lab source tree

Clone the Arm-maintained Online Boutique source tree for this Learning Path. If an existing checkout is present, move it aside before cloning a fresh copy:

```bash
export REPO_ROOT="${HOME}/n4a-c4a"
export REPO="${REPO_ROOT}/microservices-demo"
mkdir -p "${REPO_ROOT}"

if [ -d "${REPO}" ]; then
  mv "${REPO}" "${REPO}.$(date +%Y%m%d%H%M%S).bak"
fi

git clone --branch arm-multiarch-baseline --single-branch \
  https://github.com/ArmDeveloperEcosystem/microservices-demo.git "${REPO}"

cd "${REPO}"
```

Confirm the working tree:

```bash
pwd
git branch --show-current
```

The branch should be `arm-multiarch-baseline`.

## Confirm the Arm foundation

Check that the cluster has Arm node pools for N4A and C4A:

```bash
kubectl get nodes -L kubernetes.io/arch,cloud.google.com/gke-nodepool
```

Inspect the frontend manifest in the source tree:

```bash
grep -n "image:" kustomize/base/frontend.yaml
```

The cluster uses Arm-based Axion node pools, and the storefront manifest uses image references that can resolve to Arm-compatible image variants.

## What you've accomplished

You've configured your Google Cloud project, connected `kubectl` to the prepared GKE cluster, confirmed Artifact Registry access, and cloned the source tree that contains the assistant implementation.

Next, you'll validate the starting storefront baseline on N4A before you add the assistant.
