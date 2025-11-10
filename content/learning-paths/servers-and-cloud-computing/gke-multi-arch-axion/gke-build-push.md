---
title: Provision a dual-architecture GKE cluster and publish images
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

You are ready to create a GKE cluster with two node pools (amd64 and arm64), then build and push multi-arch images natively on those node pools. 

Each architecture uses its own BuildKit pod, and no QEMU emulation is required.

## Networking configuration

GKE uses VPC-native (IP aliasing) and requires two secondary ranges on the chosen subnet: one for Pods and one for Services.

For the default VPC, GKE creates the secondary ranges automatically.

Run the commands below in your terminal, adjusting the environment variables as needed for your account:

```bash
# Set/confirm network variables (adjust to your environment)
export REGION="${REGION:-us-central1}"
export NETWORK="dev-eco-nw-pb"            # your VPC
export SUBNET="dev-eco-nw-subnet"         # your subnet
export POD_RANGE_NAME="gke-boutique-pods"
export SVC_RANGE_NAME="gke-boutique-svcs"

# Inspect the subnet and existing ranges
gcloud compute networks subnets list --network "${NETWORK}" --regions "${REGION}" \
  --format="table(name,region,ipCidrRange,secondaryIpRanges.list())"

# If missing, add two secondary ranges (example CIDRs; ensure no overlap)
gcloud compute networks subnets update "${SUBNET}" --region "${REGION}" --add-secondary-ranges ${POD_RANGE_NAME}=10.8.0.0/14,${SVC_RANGE_NAME}=10.4.0.0/20
```

This approach prevents users on the default VPC from accidentally setting NETWORK/SUBNET variables and passing incorrect flags later.

## Create the GKE cluster

Create a GKE Standard cluster with VPC-native (IP aliasing) enabled and no default node pool. You'll add amd64 and arm64 pools in the next step.

The command below works for both default and custom VPCs. If the NETWORK, SUBNET, and secondary range variables are unset, GKE uses the default VPC and manages ranges automatically.

```bash
# Cluster vars (reuses earlier PROJECT_ID/REGION/ZONE)
export CLUSTER_NAME="${CLUSTER_NAME:-gke-multi-arch-cluster}"

# If using the default VPC, you can omit --network/--subnetwork.
# If using a custom VPC, include them and pass the secondary range names you set above.
gcloud container clusters create "${CLUSTER_NAME}" --region "${REGION}" --enable-ip-alias --num-nodes "1" --machine-type "e2-standard-2" ${NETWORK:+--network "${NETWORK}"} ${SUBNET:+--subnetwork "${SUBNET}"} ${POD_RANGE_NAME:+--cluster-secondary-range-name "${POD_RANGE_NAME}"} ${SVC_RANGE_NAME:+--services-secondary-range-name "${SVC_RANGE_NAME}"}
```

Now create an x86 (amd64) pool and an Arm (arm64) pool. Use machine types available in your region. The commands below use `c4-standard-*` for x86 and `c4a-standard-*` for Axion:

```bash
# amd64 pool (x86)
gcloud container node-pools create amd64-pool --cluster="${CLUSTER_NAME}" --region="${REGION}" --machine-type="c4-standard-16" --num-nodes="1" --image-type="COS_CONTAINERD" --quiet

# arm64 pool (Axion)
gcloud container node-pools create arm64-pool --cluster="${CLUSTER_NAME}" --region="${REGION}" --machine-type="c4a-standard-16" --num-nodes="1" --image-type="COS_CONTAINERD" --quiet

# delete the tiny default pool
gcloud container node-pools delete default-pool --cluster="${CLUSTER_NAME}" --region="${REGION}" --quiet
```

Connect kubectl and confirm node architectures:

```bash
gcloud container clusters get-credentials "${CLUSTER_NAME}" --region "${REGION}"
kubectl config current-context
kubectl get nodes -o wide
kubectl get nodes -L kubernetes.io/arch
```

You should see nodes for both architectures. In zonal clusters (or when a pool has `--num-nodes=1` in a single zone), expect one amd64 and one arm64 node. In regional clusters, `--num-nodes` is per zone, so with three zones you'll see three amd64 and three arm64 nodes.

## Create the Buildx builder on GKE 

Now run a BuildKit pod on an amd64 node and another on an arm64 node. Buildx routes each platform's build to the matching pod. These are native builds with no QEMU emulation.

```bash
# Namespace for BuildKit pods
kubectl create ns buildkit --dry-run=client -o yaml | kubectl apply -f -

# Create the builder (amd64 node)
docker buildx create --driver kubernetes --name gke-native --use --driver-opt namespace=buildkit,replicas=1,loadbalance=sticky,nodeselector=kubernetes.io/arch=amd64 --platform linux/amd64

# Append an arm64 node to the same builder
docker buildx create --driver kubernetes --append --name gke-native --driver-opt namespace=buildkit,replicas=1,loadbalance=sticky,nodeselector=kubernetes.io/arch=arm64 --platform linux/arm64

# Bootstrap and verify pods
docker buildx inspect gke-native --bootstrap
kubectl -n buildkit get pods -o wide
```

You now have a multi-node Buildx builder named `gke-native`. Each BuildKit pod is pinned to a specific CPU architecture using node selectors.

## Build and push all services

You can now build all services for `linux/amd64` and `linux/arm64` using the GKE-backed builder.

Run the commands:

```bash
cat << 'EOF' > build-all-multiarch.sh
#!/usr/bin/env bash
set -euo pipefail

: "${GAR:?Set GAR like REGION-docker.pkg.dev/PROJECT/REPO first}"

services=(
  adservice
  cartservice   # special context below
  checkoutservice
  currencyservice
  emailservice
  frontend
  paymentservice
  productcatalogservice
  recommendationservice
  shippingservice
  loadgenerator
)

for svc in "${services[@]}"; do
  # cartservice Dockerfile path differs
  if [ "$svc" = "cartservice" ] && [ -d "src/cartservice/src" ]; then
    ctx="src/cartservice/src"
  else
    ctx="src/${svc}"
  fi

  echo ">>> Building ${svc} for amd64+arm64..."
  docker buildx build --builder gke-native --platform linux/amd64,linux/arm64 --provenance=false -t "${GAR}/${svc}:v1" "${ctx}" --push
done
EOF

chmod +x build-all-multiarch.sh
./build-all-multiarch.sh
```

Each tag you push is a manifest list that points to two images, one per architecture.

## Verify manifest lists and per-arch pulls

List pushed images:

```bash
gcloud artifacts docker images list "${GAR}"
```

Inspect one tag to confirm it shows both platforms:

```bash
docker buildx imagetools inspect "${GAR}/adservice:v1"
```

The output is:

```output
Platform: linux/amd64
Platform: linux/arm64
```

You are now ready to prepare the application manifests and deploy the application.