---
title: Create the GKE cluster and Axion node pool
description: Create a zonal GKE Standard cluster with a Google Axion gVisor node pool and enable Agent Sandbox.
weight: 3
layout: learningpathall
---

## Choose the cluster configuration

Continue in the same terminal with `LP_WORKDIR` still set. Run `cd "$LP_WORKDIR"` if you opened a new terminal. 

You'll create one small system node and one Arm sandbox node. The system pool will use an `e2-standard-2` node. Your Python workloads will use the separate `c4a-standard-2` pool which uses Google Axion processors.

Set the names and networking for a dedicated tutorial cluster:

```bash
cd "$LP_WORKDIR"
export LOCATION=us-central1-c
export REGION=us-central1
export CLUSTER_NAME=gke-agent-sandbox
export NODE_POOL_NAME=axion-sandbox-pool
export MACHINE_TYPE=c4a-standard-2
export NAMESPACE=axion-sandbox-prototype
export NETWORK=gke-sandbox-vpc
export SUBNETWORK=gke-sandbox-subnet
```

Create a dedicated VPC network and subnet for the cluster. VPC networks and subnets have no cost on their own:

```bash
gcloud compute networks create "$NETWORK" \
  --project="$PROJECT_ID" --subnet-mode=custom
gcloud compute networks subnets create "$SUBNETWORK" \
  --project="$PROJECT_ID" --network="$NETWORK" \
  --region="$REGION" --range=10.0.0.0/20
```

You'll use these environment variables for subsequent commands, so keep this terminal open or re-export them if you start a new session. `us-central1-c` is the default zone. If you hit C4A capacity issues, `us-east4-a` is a good alternative — update both `LOCATION` and `REGION`, and recreate the subnet in the new region as described in [Handle capacity failures](/learning-paths/servers-and-cloud-computing/gke-agent-sandbox/1-provision-arm-sandboxes/#handle-capacity-failures).

If you saved `env.sh` earlier, append these variables to it:

```bash
cat >> "$LP_WORKDIR/env.sh" << EOF
export LOCATION="$LOCATION"
export REGION="$REGION"
export CLUSTER_NAME="$CLUSTER_NAME"
export NODE_POOL_NAME="$NODE_POOL_NAME"
export MACHINE_TYPE="$MACHINE_TYPE"
export NAMESPACE="$NAMESPACE"
export NETWORK="$NETWORK"
export SUBNETWORK="$SUBNETWORK"
EOF
```

## Check access, quota, and versions

The following commands enable the Google Kubernetes Engine (GKE) and Compute APIs on your project, which are required before you can create a cluster. 

The commands also perform the following tasks:

- Confirm that billing is active.
- Verify that the Axion machine type is available in your zone.
- Save the quota and available GKE versions for your chosen region to `output/server-config.json` for troubleshooting.

Run the commands:

```bash
gcloud billing projects describe "$PROJECT_ID"
gcloud services enable container.googleapis.com compute.googleapis.com --project="$PROJECT_ID"
gcloud compute machine-types describe "$MACHINE_TYPE" --zone="$LOCATION" --project="$PROJECT_ID"
gcloud compute regions describe "$REGION" --project="$PROJECT_ID" \
  --format='table(quotas.metric,quotas.limit,quotas.usage)'
gcloud container get-server-config --location="$LOCATION" --project="$PROJECT_ID" \
  --format=json > output/server-config.json
cat output/server-config.json
```

The saved server config lists the available GKE versions for your location. Query the config to see which versions are available in the `regular` release channel:

```bash
jq -r '.channels[] | select(.channel=="REGULAR") | .validVersions[]' output/server-config.json
```

Agent Sandbox requires GKE `1.36.3-gke.1767000` or later with the `v1beta1` API. Pick the latest available version in the `regular` channel that meets this requirement. The version used for testing was `1.36.4-gke.1391000`, but your version might be newer.

Set your chosen version and channel:

```bash
export CLUSTER_VERSION=1.36.4-gke.1391000   # replace with your chosen version
export RELEASE_CHANNEL=regular
```

If you're using `env.sh`, append these variables to the file:

```bash
cat >> "$LP_WORKDIR/env.sh" << EOF
export CLUSTER_VERSION="$CLUSTER_VERSION"
export RELEASE_CHANNEL="$RELEASE_CHANNEL"
EOF
```

## Provision the cluster

Run each provisioning command separately and check its result before continuing. 

First, create the system pool:

```bash
gcloud beta container clusters create "$CLUSTER_NAME" \
  --project="$PROJECT_ID" --location="$LOCATION" \
  --cluster-version="$CLUSTER_VERSION" --release-channel="$RELEASE_CHANNEL" \
  --network="$NETWORK" --subnetwork="$SUBNETWORK" \
  --num-nodes=1 --machine-type=e2-standard-2 \
  --image-type=COS_CONTAINERD --disk-size=30 --enable-ip-alias
```

Add the Axion pool with gVisor enabled. C4A uses Hyperdisk boot storage, so set its disk type explicitly:

```bash
gcloud container node-pools create "$NODE_POOL_NAME" \
  --project="$PROJECT_ID" --cluster="$CLUSTER_NAME" --location="$LOCATION" \
  --machine-type="$MACHINE_TYPE" --num-nodes=1 \
  --image-type=COS_CONTAINERD --disk-type=hyperdisk-balanced --disk-size=100 \
  --sandbox=type=gvisor
```

Enable the managed Agent Sandbox feature:

```bash
gcloud beta container clusters update "$CLUSTER_NAME" \
  --project="$PROJECT_ID" --location="$LOCATION" --enable-agent-sandbox
```

Confirm that the Axion node is running before continuing:

```bash
gcloud container node-pools describe "$NODE_POOL_NAME" \
  --project="$PROJECT_ID" --cluster="$CLUSTER_NAME" --location="$LOCATION" \
  --format="table(name,status,config.machineType,config.sandboxConfig.type)"
```

The node pool status should be `RUNNING`, the machine type `c4a-standard-2`, and the sandbox type `gvisor`.

## Handle capacity failures

If the node pool can't allocate a node, check the operation status:

```bash
gcloud container operations list --project="$PROJECT_ID" --location="$LOCATION" \
  --filter="operationType=CREATE_NODE_POOL" --format="table(name,status,statusMessage)"
```

An insufficient-capacity error means no `c4a-standard-2` nodes were available in `LOCATION`. Delete the cluster, then retry in a different zone or with a larger machine type:

```bash
gcloud container clusters delete "$CLUSTER_NAME" \
  --project="$PROJECT_ID" --location="$LOCATION" --quiet
```

To try a different zone, update `LOCATION` and re-run the commands under [Provision the cluster](/learning-paths/servers-and-cloud-computing/gke-agent-sandbox/1-provision-arm-sandboxes/#provision-the-cluster):

```bash
export LOCATION=us-central1-a
```

To try a larger machine type, update `MACHINE_TYPE` and re-run the commands under [Provision the cluster](/learning-paths/servers-and-cloud-computing/gke-agent-sandbox/1-provision-arm-sandboxes/#provision-the-cluster):

```bash
export MACHINE_TYPE=c4a-standard-4
```

For a quota error, the `statusMessage` names the quota that was exceeded. Go to **IAM & Admin > Quotas** in the Google Cloud console, find that quota, and request an increase before retrying.

## Install the matching kubectl

Now that the cluster exists, install a kubectl within one minor version of its control plane, following the [Kubernetes version skew policy](https://kubernetes.io/releases/version-skew-policy/). Set `KUBECTL_VERSION` to match the minor of the `CLUSTER_VERSION` that you chose earlier. The following block detects your OS and architecture, downloads the matching binary, and verifies its checksum. Run it as a subshell so that a download failure stops the block:

```bash
(
  set -eu
  KUBECTL_VERSION=v1.36.3
  case "$(uname -s)" in
    Linux) KUBECTL_OS=linux ;;
    Darwin) KUBECTL_OS=darwin ;;
    *) echo 'Use a native kubectl build for your OS.' >&2; exit 1 ;;
  esac
  case "$(uname -m)" in
    aarch64|arm64) KUBECTL_ARCH=arm64 ;;
    x86_64|amd64) KUBECTL_ARCH=amd64 ;;
    *) echo 'Use a native kubectl build for your architecture.' >&2; exit 1 ;;
  esac
  DOWNLOAD_DIR=$(mktemp -d)
  cd "$DOWNLOAD_DIR"
  KUBECTL_URL="https://dl.k8s.io/release/$KUBECTL_VERSION/bin/$KUBECTL_OS/$KUBECTL_ARCH/kubectl"
  curl -fL "$KUBECTL_URL" -o kubectl
  curl -fL "$KUBECTL_URL.sha256" -o kubectl.sha256
  if [ "$KUBECTL_OS" = linux ]; then
    printf '%s  kubectl\n' "$(cat kubectl.sha256)" | sha256sum --check
  else
    printf '%s  kubectl\n' "$(cat kubectl.sha256)" | shasum -a 256 --check
  fi
  mkdir -p "$HOME/.local/bin"
  chmod 755 kubectl
  cp kubectl "$HOME/.local/bin/kubectl"
)
export PATH="$HOME/.local/bin:$PATH"
hash -r
kubectl version --client
```

Add the `PATH` entry to your shell startup file if desired. 

## Verify the Arm sandbox pool

Obtain cluster credentials and save the explicit context for later helper commands:

```bash
gcloud container clusters get-credentials "$CLUSTER_NAME" \
  --project="$PROJECT_ID" --location="$LOCATION"
export GKE_CONTEXT="$(kubectl config current-context)"
```

If you're using `env.sh`, append `GKE_CONTEXT`:

```bash
echo "export GKE_CONTEXT=\"$GKE_CONTEXT\"" >> "$LP_WORKDIR/env.sh"
```

Check that the nodes are ready and note the architecture, machine type, and sandbox runtime:

```bash
kubectl --context "$GKE_CONTEXT" get nodes \
  -L kubernetes.io/arch,node.kubernetes.io/instance-type,sandbox.gke.io/runtime
```

The sandbox node row should show `arm64`, `c4a-standard-2`, and `gvisor`:

```output
NAME                                               STATUS   ROLES    AGE   VERSION   ARCH    INSTANCE-TYPE    RUNTIME
gke-gke-agent-sandbox-axion-sandbox-pool-<hash>   Ready    <none>   2m    v1.36.x   arm64   c4a-standard-2   gvisor
gke-gke-agent-sandbox-default-pool-<hash>         Ready    <none>   4m    v1.36.x   amd64   e2-standard-2
```

Confirm that the gVisor runtime class is registered:

```bash
kubectl --context "$GKE_CONTEXT" get runtimeclass gvisor
```

The output is similar to:

```output
NAME     HANDLER   AGE
gvisor   runsc     2m
```

Confirm that the Agent Sandbox API resources are available:

```bash
kubectl --context "$GKE_CONTEXT" api-resources --api-group=extensions.agents.x-k8s.io
```

```output
NAME                 SHORTNAMES   APIVERSION                                    NAMESPACED   KIND
sandboxclaims                     extensions.agents.x-k8s.io/v1beta1            true         SandboxClaim
sandboxtemplates                  extensions.agents.x-k8s.io/v1beta1            true         SandboxTemplate
sandboxwarmpools                  extensions.agents.x-k8s.io/v1beta1            true         SandboxWarmPool
```

Save the cluster and node pool configuration to the `output/` directory:

```bash
gcloud beta container clusters describe "$CLUSTER_NAME" \
  --project="$PROJECT_ID" --location="$LOCATION" --format=json > output/cluster.json
gcloud container node-pools describe "$NODE_POOL_NAME" \
  --project="$PROJECT_ID" --cluster="$CLUSTER_NAME" --location="$LOCATION" \
  --format=json > output/node-pool.json
```

## What you've accomplished and what's next

You've enabled Agent Sandbox and prepared a gVisor node pool on Google Axion.

Next, you'll define the Python environment, claim a sandbox, and verify its filesystem restrictions.
