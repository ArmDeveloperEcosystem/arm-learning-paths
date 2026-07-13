---
title: Set up the source tree and cluster access
description: Configure the Google Cloud variables, connect kubectl to the GKE cluster, and clone the source tree for the storefront assistant.
weight: 3
layout: "learningpathall"
---

## Configure your environment 

You'll use a prepared GKE Standard cluster with two Linux `arm64` node pools:

- An N4A node pool based on Google Axion and Arm Neoverse N3
- A C4A node pool based on Google Axion and Arm Neoverse V2

The cluster must expose the Kubernetes Metrics API so that `kubectl top` and the benchmark telemetry collector can read pod CPU usage. 

Your Google Cloud account also needs permission for the following: 
- Getting cluster credentials
- Deploying Kubernetes workloads and services
- Reading nodes, pod logs, and pod metrics
- Creating or using an Artifact Registry Docker repository in the same project

Use [Cloud Shell](https://cloud.google.com/shell/docs/using-cloud-shell) or a Linux or macOS administrative workstation to manage GKE. The application runs in Linux `arm64` containers on the cluster. 

You'll need Docker running on your administrative environment, and the Buildx plugin to be available.

Buildx can create a `linux/arm64` image on an Arm development machine. It can also use an appropriately configured builder to cross-build the image on another architecture.

Confirm that the tools are available:

```bash
gcloud --version
kubectl version --client
docker version
docker buildx version
git --version
curl --version
python3 --version
jq --version
```

The workshop helper scripts require Python 3.10 or later. Use a `kubectl` client version that Google Kubernetes Engine supports for your cluster version.

Create or reuse the builder for this Learning Path:

```bash
if docker buildx inspect axion-builder >/dev/null 2>&1; then
  docker buildx use axion-builder
else
  docker buildx create --name axion-builder --use
fi

docker buildx inspect --bootstrap
```

Confirm that the `Platforms` line includes `linux/arm64` before you continue. The later build command uses this capability to produce an image for the Arm-based N4A and C4A nodes. If `linux/arm64` is missing, configure Arm support for your Docker builder before continuing.

You'll also use Kustomize in the following sections. Kustomize combines a shared set of Kubernetes manifests with reusable components and placement-specific patches. The tool is built into `kubectl`, so the `kubectl kustomize` and `kubectl apply -k` commands don't need a separate Kustomize executable.

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
printf 'Google Cloud project ID: '
read -r PROJECT_ID
export PROJECT_ID
gcloud config set project "${PROJECT_ID}"
export ARTIFACT_REGISTRY="${ARTIFACT_REGION}-docker.pkg.dev/${PROJECT_ID}/${ARTIFACT_REPO}"
```

Save the values in one environment file so that later terminals use the same configuration. If you change a prepared resource name, update it in the following block and recreate the file:

```bash
export AXION_LAB_ENV="${HOME}/.storefront-axion-env"
export REPO_ROOT="${HOME}/n4a-c4a"
export REPO="${REPO_ROOT}/microservices-demo"
export SOURCE_COMMIT="b0a1be98cd47087638b2ea98c9c3de01bc4f533c"
export ASSISTANT_IMAGE_REPO="${ARTIFACT_REGISTRY}/shoppingassistantservice"
export ASSISTANT_IMAGE_TAG="lab-v1"
export ASSISTANT_IMAGE="${ASSISTANT_IMAGE_REPO}:${ASSISTANT_IMAGE_TAG}"

cat <<EOF > "${AXION_LAB_ENV}"
export PROJECT_ID="${PROJECT_ID}"
export CLUSTER_NAME="${CLUSTER_NAME}"
export ARTIFACT_REGION="${ARTIFACT_REGION}"
export ARTIFACT_REPO="${ARTIFACT_REPO}"
export ARTIFACT_REGISTRY="${ARTIFACT_REGISTRY}"
export N4A_NODE_POOL_NAME="${N4A_NODE_POOL_NAME}"
export C4A_NODE_POOL_NAME="${C4A_NODE_POOL_NAME}"
export REPO_ROOT="${REPO_ROOT}"
export REPO="${REPO}"
export SOURCE_COMMIT="${SOURCE_COMMIT}"
export ASSISTANT_IMAGE_REPO="${ASSISTANT_IMAGE_REPO}"
export ASSISTANT_IMAGE_TAG="${ASSISTANT_IMAGE_TAG}"
export ASSISTANT_IMAGE="${ASSISTANT_IMAGE}"
EOF
```

## Discover the cluster location

Query Google Cloud for the cluster location to avoid hard-coding a zone or region:

```bash
export CLUSTER_LOCATION="$(gcloud container clusters list \
  --project "${PROJECT_ID}" \
  --filter="name=${CLUSTER_NAME}" \
  --format='value(location)' | head -n 1)"

echo "${CLUSTER_LOCATION}"
```

The output prints the cluster location, such as `us-central1` or `us-central1-a`.

Don't continue if the output is empty. Confirm `CLUSTER_NAME` and `PROJECT_ID`, and then run the command again.

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
mkdir -p "${REPO_ROOT}"

if [ -d "${REPO}" ]; then
  mv "${REPO}" "${REPO}.$(date +%Y%m%d%H%M%S).bak"
fi

git clone --branch arm-multiarch-baseline --single-branch \
  https://github.com/ArmDeveloperEcosystem/microservices-demo.git "${REPO}"

cd "${REPO}"
git checkout "${SOURCE_COMMIT}"
```

The commit is pinned because the workshop branch is under active development. Confirm that the working tree is at the expected commit:

```bash
pwd
git rev-parse HEAD
```

The commit should be:

```output
b0a1be98cd47087638b2ea98c9c3de01bc4f533c
```

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

## What you've accomplished and what's next

You've now configured your Google Cloud project, connected `kubectl` to the prepared GKE cluster, confirmed Artifact Registry access, and cloned the source tree that contains the assistant implementation.

Next, you'll validate the starting storefront baseline on N4A before you add the assistant.
