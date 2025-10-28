---
title:  Create a dual-architecture GKE cluster and deploy
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

Now create a **GKE cluster** with **two node pools** (amd64 & arm64), then deploy Online Boutique to the amd64 pool and migrate the same workloads to the arm64 pool using Kustomize overlays.

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

### Create the GKE cluster (IP alias)

Create a GKE Standard cluster with VPC-native (IP aliasing) enabled and no default node pool (we will add separate x86/amd64 and Arm/arm64 pools next). If you are on the default VPC, use the simple command below. If you're on a custom VPC, specify --network, --subnetwork, and the names of the two secondary ranges you created for Pods and Services:

**Default VPC:**
```bash
export CLUSTER_NAME="${CLUSTER_NAME:-gke-multi-arch-cluster}"
gcloud container clusters create "${CLUSTER_NAME}" \
  --region "${REGION}" \
  --enable-ip-alias \
  --num-nodes "0"
```
**Custom VPC (use your names from above):**

Create the cluster with no default node pool and add node pools explicitly.

```bash
# Cluster vars (reuses earlier PROJECT_ID/REGION/ZONE)
export CLUSTER_NAME="${CLUSTER_NAME:-gke-multi-arch-cluster}"

# If using the default VPC, you can omit --network/--subnetwork.
# If using a custom VPC, include them and pass the secondary range names you set above.
gcloud container clusters create "${CLUSTER_NAME}" --region "${REGION}" --enable-ip-alias --num-nodes "0" ${NETWORK:+--network "${NETWORK}"} ${SUBNET:+--subnetwork "${SUBNET}"} ${POD_RANGE_NAME:+--cluster-secondary-range-name "${POD_RANGE_NAME}"} ${SVC_RANGE_NAME:+--services-secondary-range-name "${SVC_RANGE_NAME}"}
```

Create an x86 (amd64) pool and an Arm (arm64) pool. Use machine types available in your region (e.g., c4-standard-* for x86 and c4a-standard-* for Axion). 

```bash
# amd64 pool (x86)
gcloud container node-pools create amd64-pool --cluster="${CLUSTER_NAME}" --region="${REGION}" --machine-type="c4-standard-16" --num-nodes="1" --image-type="COS_CONTAINERD" --quiet

# arm64 pool (Axion)
gcloud container node-pools create arm64-pool --cluster="${CLUSTER_NAME}" --region="${REGION}" --machine-type="c4a-standard-16" --num-nodes="1" --image-type="COS_CONTAINERD" --quiet
```

Connect kubectl and confirm node architectures:

```bash
gcloud container clusters get-credentials "${CLUSTER_NAME}" --region "${REGION}"
kubectl config current-context
kubectl get nodes -o wide
kubectl get nodes -L kubernetes.io/arch
```
You should see one node labeled `kubernetes.io/arch=amd64` and one labeled `kubernetes.io/arch=arm64`.

### Prepare deployment manifests

Replace public sample image references with your Artifact Registry path and **tag(:v1)**, then create Kustomize overlays to select nodes by architecture.

####  Point base manifests at your images

```bash
# Replace the sample repo path with your GAR (from earlier: ${GAR})
find kustomize/base -name "*.yaml" -type f -exec \
  sed -i "s|us-central1-docker.pkg.dev/google-samples/microservices-demo|${GAR}|g" {} +

# Replace the sample tag with your tag
find kustomize/base -name "*.yaml" -type f -exec \
  sed -i "s|:v0\.10\.3|:v1|g" {} +

# Verify changes
grep -r "${GAR}" kustomize/base/ || true
```

#### Create node-selector overlays (amd64 and arm64)

```bash
mkdir -p kustomize/overlays/amd64 kustomize/overlays/arm64
```

**amd64 overlay**

```bash
cat << 'EOF' > kustomize/overlays/amd64/kustomization.yaml
resources:
- ../../base
patches:
- path: node-selector.yaml
  target:
    kind: Deployment
EOF

cat << 'EOF' > kustomize/overlays/amd64/node-selector.yaml
- op: add
  path: /spec/template/spec/nodeSelector
  value:
    kubernetes.io/arch: amd64
EOF
```

**arm64 overlay**
```bash
cat << 'EOF' > kustomize/overlays/arm64/kustomization.yaml
resources:
- ../../base
patches:
- path: node-selector.yaml
  target:
    kind: Deployment
EOF

cat << 'EOF' > kustomize/overlays/arm64/node-selector.yaml
- op: add
  path: /spec/template/spec/nodeSelector
  value:
    kubernetes.io/arch: arm64
EOF
```

Result: the base references your images, and overlays control per-arch placement.

### Deploy to the x86 (amd64) pool

Render the amd64 Kustomize overlay (adds nodeSelector: kubernetes.io/arch=amd64) and apply it to the cluster. Run from the repository root after updating base manifests to your ${GAR} and setting your kube-context to this cluster.

```bash
kubectl kustomize kustomize/overlays/amd64 | kubectl apply -f -
```

Check pod placement and status:

```bash
kubectl get pods -o wide
# or include the architecture label on the nodes
kubectl get pods -o=custom-columns=NAME:.metadata.name,NODE:.spec.nodeName,STATUS:.status.phase --no-headers
```

Pods should be scheduled on nodes where `kubernetes.io/arch=amd64`.

### Migrate to the Arm (arm64) pool

Apply the arm64 overlay to move workloads: 

```bash
kubectl kustomize kustomize/overlays/arm64 | kubectl apply -f -
```

Verify pods have shifted to arm64 nodes:

```bash
kubectl get pods -o wide
```

You should see pods now running on nodes where `kubernetes.io/arch=arm64`.

### Verify external access

Get the LoadBalancer IP and open the storefront:

```bash
kubectl get svc frontend-external
```

Expected columns include EXTERNAL-IP:

```
NAME               TYPE           CLUSTER-IP     EXTERNAL-IP      PORT(S)        AGE
frontend-external  LoadBalancer   10.12.3.45     34.123.45.67     80:31380/TCP   3m
```

Copy the EXTERNAL-IP value, and open it in a new browser tab:
```
http://<EXTERNAL-IP>
```

The microservices storefront should load confirming that your application is accessible and functional on the Arm64 node pool. 

