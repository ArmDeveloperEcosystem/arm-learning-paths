---
title: Prepare your environment
description: Check the cluster API, Arm node pools, permissions, and source bundle before deploying the workflow.
weight: 3
layout: learningpathall
---

## Confirm the cluster contract

Allow approximately two hours for the exercises, plus time for cluster provisioning and large image downloads.

Use a dedicated learning environment. Running VM nodes, disks, Artifact Registry storage, and hosted Gemini requests can incur charges even when the dashboard is idle. Namespace CPU quotas do not cap your cloud bill.

The supplied manifests target the recorded GKE Agent Sandbox API: `agents.x-k8s.io/v1beta1`, with `spec.operatingMode` and `spec.podTemplate`. The recorded cluster uses GKE `1.36.4-gke.1391002`, Container-Optimized OS on `arm64`, and containerd `2.2.7`.

The [Agent Sandbox v1.0.9 resource definition](https://github.com/kubernetes-sigs/agent-sandbox/blob/v1.0.9/k8s/crds/agents.x-k8s.io_sandboxes.yaml) includes these fields. Follow [Google's Agent Sandbox installation guidance](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/how-install-agent-sandbox) for your cluster, then verify its installed custom resource definition (CRD) and use server-side dry-run later. Matching field names do not establish that the full workflow runs correctly on another controller release. If the required schema is absent, agree a compatible setup with the cluster administrator before continuing.

Use Bash for the commands in this Learning Path. Replace the values in this block with your own existing environment, then keep the terminal open:

```bash
export PROJECT_ID="your-project-id"
export REGION="your-registry-region"
export CLUSTER_NAME="your-cluster-name"
export CLUSTER_LOCATION="your-cluster-region-or-zone"
export REPOSITORY="your-existing-docker-repository"
export REGISTRY="$REGION-docker.pkg.dev/$PROJECT_ID/$REPOSITORY"
export TAG="lp-review-1"
export NAMESPACE="axion-agent-studio"

gcloud container clusters get-credentials "$CLUSTER_NAME" \
  --location "$CLUSTER_LOCATION" --project "$PROJECT_ID"
kubectl config current-context
kubectl get runtimeclass gvisor
kubectl explain sandbox.spec --api-version=agents.x-k8s.io/v1beta1
kubectl get nodes -L kubernetes.io/arch,node.kubernetes.io/instance-type,studio.axion.dev/pool
```

Confirm that the context is the intended cluster. The Sandbox schema must expose `operatingMode` and `podTemplate`, and the `gvisor` RuntimeClass must exist.

The node pools must have the following **custom labels**. These labels are distinct from the GKE node-pool names. Ask the administrator to configure labels on the node pools so replacements retain them.

| Custom `studio.axion.dev/pool` label | Capacity used in the recorded demo | Runtime |
| --- | --- | --- |
| `n4a-regular` | One N4A node, 2 vCPUs | Regular container runtime |
| `c4a-sandbox` | One C4A node, 16 vCPUs | gVisor |
| `n4a-sandbox` | One N4A node, 8 vCPUs | gVisor |

All three pools must report `kubernetes.io/arch=arm64`. Sandbox nodes must report `sandbox.gke.io/runtime=gvisor`. Keep separate capacity for system workloads. Verify the node's allocatable resources rather than assuming its advertised capacity is entirely available to Pods.

## Arrange access before building

An administrator must allow creation and deletion of a dedicated Namespace, which is a cluster-scoped resource. Your deployment identity needs permission to read the cluster and create the tutorial's namespaced resources: Sandbox objects, Services, ServiceAccounts, Roles, RoleBindings, NetworkPolicies, and a ResourceQuota.

For dashboard node details, an administrator also needs to apply the generated cluster-scoped observer role and binding. These permissions are limited to the named tutorial nodes.

Your image builder needs Artifact Registry write access. The node service account needs read access to the image repository and the GKE node permissions required by your organization.

The manager uses Workload Identity Federation for GKE to call Vertex AI without a downloaded service-account key. The cluster and regular node pool must have it enabled. Ask an IAM administrator to grant the manager's Kubernetes service account the appropriate model access. The recorded setup uses `roles/aiplatform.user` with this principal shape:

```text
principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/subject/ns/axion-agent-studio/sa/studio-manager
```

Replace both project identifiers when arranging the binding. The workers and validator do not need this hosted-model permission. Follow [Google's workload authentication guide](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) for the IAM configuration. Confirm that the Vertex AI and IAM Credentials APIs and the selected Gemini model are available to your project.

The manifests assume enforced NetworkPolicy and the GKE Dataplane V2 metadata route. They permit the trusted manager to reach its worker services, the validator, DNS, the verified Kubernetes API endpoint, the metadata endpoint, and public HTTPS. The HTTPS rule is not a hostname allowlist. The sandbox workloads do not receive general internet egress or an automatically mounted Kubernetes token.

## Companion source release pending

This draft is available for documentation review. The companion application source is not included in this pull request because its public release and licensing still need owner approval. A public source location and immutable revision or checksum must be added before this Learning Path can be followed end to end.

The remaining commands describe the intended workflow after that source release is available. After you obtain the approved source, set the path to its extracted directory. All subsequent application commands run from that directory:

```bash
export LP_WORKDIR="$HOME/axion-lp-review/axion-agent-studio"
cd "$LP_WORKDIR"
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python -m pytest tests -q
```

Local tests exercise contracts, validation logic, and application behavior using controlled inputs. They do not prove live Gemini access, model quality, or GKE isolation. Review the source release license and notices before using the application.

At this point you have checked the cluster boundary and prepared the application source. Next, build the arm64 images and generate manifests for your own environment.
