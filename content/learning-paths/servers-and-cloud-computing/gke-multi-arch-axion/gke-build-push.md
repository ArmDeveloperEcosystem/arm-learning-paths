---
title: Provision a Dual-Arch GKE Cluster and Publish Multi-Arch Images
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

Now create a **GKE cluster** with **two node pools** (amd64 & arm64), then build and push multi-arch images natively on those node pools. Each architecture uses its own BuildKit pod, and no QEMU emulation is involved.

#### Networking (VPC-native / IP aliasing)

GKE uses **VPC-native (IP aliasing)** and requires **two secondary ranges** on the chosen subnet: one for **Pods** and one for **Services**.
- **Default VPC:** Skip this step. GKE will create the secondary ranges automatically.
- **Custom VPC/subnet:** Set variables and add/verify secondary ranges:

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
This avoids users on default VPC accidentally setting NETWORK/SUBNET and passing the wrong flags later.

### Create the GKE cluster

Create a GKE Standard cluster with VPC-native (IP aliasing) enabled and no default node pool (you'll add amd64 and arm64 pools next). The command below works for both default and custom VPCs: if NETWORK, SUBNET, and the secondary range variables are unset, GKE uses the default VPC and manages ranges automatically.

Create the cluster with no default node pool and add node pools explicitly.

```bash
# Cluster vars (reuses earlier PROJECT_ID/REGION/ZONE)
export CLUSTER_NAME="${CLUSTER_NAME:-gke-multi-arch-cluster}"

# If using the default VPC, you can omit --network/--subnetwork.
# If using a custom VPC, include them and pass the secondary range names you set above.
gcloud container clusters create "${CLUSTER_NAME}" --region "${REGION}" --enable-ip-alias --num-nodes "1" --machine-type "e2-standard-2" ${NETWORK:+--network "${NETWORK}"} ${SUBNET:+--subnetwork "${SUBNET}"} ${POD_RANGE_NAME:+--cluster-secondary-range-name "${POD_RANGE_NAME}"} ${SVC_RANGE_NAME:+--services-secondary-range-name "${SVC_RANGE_NAME}"}
```

Create an x86 (amd64) pool and an Arm (arm64) pool. Use machine types available in your region (e.g., c4-standard-* for x86 and c4a-standard-* for Axion). 

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
You should see nodes for both architectures. In zonal clusters (or when a pool has --num-nodes=1 in a single zone), expect one amd64 and one arm64 node. In regional clusters, --num-nodes is per zone, with three zones you'll see three amd64 and three arm64 nodes.

### Create the Buildx builder on GKE (native, one pod per arch)

Now run a BuildKit pod on an amd64 node and another on an arm64 node. Buildx will route each platform's build to the matching pod - native builds, no emulation.

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
{{% notice Note %}}
You will now have a multi-node Buildx builder named gke-native. Each BuildKit pod is pinned to a specific CPU arch via nodeselector.
{{% /notice %}}

### Build & push all services (multi-arch manifest lists)
Build every service for linux/amd64 and linux/arm64 using the GKE-backed builder:
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
Each :v1 you push is a manifest list that points to two images (one per arch).

### Verify manifest lists and per-arch pulls

List pushed images:

```bash
gcloud artifacts docker images list "${GAR}"
```

Inspect one tag (should show both platforms):
```bash
docker buildx imagetools inspect "${GAR}/adservice:v1"
```

Expected Output:
```
Platform: linux/amd64
Platform: linux/arm64
```
