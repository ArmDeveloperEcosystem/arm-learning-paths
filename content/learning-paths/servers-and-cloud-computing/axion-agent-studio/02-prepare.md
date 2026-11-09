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

All three pools must report `kubernetes.io/arch=arm64`. Sandbox nodes must report `sandbox.gke.io/runtime=gvisor`. Keep separate capacity for system workloads. Verify the node's allocatable resources rather than assuming its advertised capacity is entirely available to Pods. To reproduce the shared-worker placement in this Learning Path, use exactly one eligible C4A node with enough allocatable capacity for all three workers. If several nodes have the `c4a-sandbox` label, Kubernetes can place the workers on different nodes.

## Check your workstation tools

Use Python 3.12 and Node.js 22 for the companion's Python and frontend checks. Confirm that the command-line tools are available before downloading the model or building images:

```bash
python3.12 --version
node --version
gcloud version
gke-gcloud-auth-plugin --version
kubectl version --client
docker buildx version
```

The Python output must report 3.12 and the Node.js output must report 22. Docker must be running with a Buildx builder capable of producing `linux/arm64` images. The model download and staging step retain two copies of the approximately 4.6 GB GGUF file; allow additional space for Docker images and its build cache.

Python must also have a working trusted certificate store for the source and model downloads. If it reports `CERTIFICATE_VERIFY_FAILED`, repair the installation's CA configuration before continuing. On macOS, when `/etc/ssl/cert.pem` is your approved system CA bundle, `export SSL_CERT_FILE=/etc/ssl/cert.pem` selects it for this terminal. Keep certificate verification enabled; see [Python's certificate lookup configuration](https://docs.python.org/3.12/library/ssl.html#ssl.get_default_verify_paths).

## Arrange access before building

An administrator must allow creation and deletion of a dedicated Namespace, which is a cluster-scoped resource. Your deployment identity needs permission to read the cluster and create, patch, update, and delete the tutorial's namespaced resources: Sandbox objects, Deployments, Services, ServiceAccounts, Roles, RoleBindings, NetworkPolicies, and a ResourceQuota.

The inspection steps also require reading Nodes, RuntimeClasses, the Sandbox CRD, controller and application Deployments, Pods, events, and the Kubernetes Service's EndpointSlices or Endpoints. Readiness waits require `watch` access to Deployments, Sandboxes, and Pods. Reading Pod logs requires `get` on `pods/log`; dashboard access requires `create` on `pods/portforward`. If you run the companion README's optional checkpoint, arrange `create` on `pods/exec` for the manager as well. Have the administrator confirm these permissions before deployment.

For dashboard node details, an administrator also needs to apply the generated cluster-scoped observer role and binding. These permissions are limited to the named tutorial nodes.

Your image builder needs Artifact Registry write access. The node service account needs read access to the image repository and the GKE node permissions required by your organization.

The manager uses Workload Identity Federation for GKE to call Vertex AI without a downloaded service-account key. The cluster and regular node pool must have it enabled. Ask an IAM administrator to grant the manager's Kubernetes service account the appropriate model access. The recorded setup uses `roles/aiplatform.user` with this principal shape:

```text
principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/subject/ns/axion-agent-studio/sa/studio-manager
```

Replace both project identifiers when arranging the binding. The workers and validator do not need this hosted-model permission. Follow [Google's workload authentication guide](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) for the IAM configuration. Confirm that the Vertex AI and IAM Credentials APIs and the selected Gemini model are available to your project.

The manifests assume enforced NetworkPolicy and the GKE Dataplane V2 metadata route. They permit the trusted manager to reach its worker services, the validator, DNS, the verified Kubernetes API endpoint, the metadata endpoint, and public HTTPS. The HTTPS rule is not a hostname allowlist. The sandbox workloads do not receive general internet egress or an automatically mounted Kubernetes token.

## Download and verify the companion source

Use the [2026-11-09 companion source archive](https://raw.githubusercontent.com/ranimandepudi/arm-learning-paths/84b9bcb7e8989113345c0a504cb668c34d10765f/content/learning-paths/servers-and-cloud-computing/axion-agent-studio/assets/axion-agent-studio-2026-11-09.zip) and its [SHA-256 manifest](https://raw.githubusercontent.com/ranimandepudi/arm-learning-paths/84b9bcb7e8989113345c0a504cb668c34d10765f/content/learning-paths/servers-and-cloud-computing/axion-agent-studio/assets/axion-agent-studio-2026-11-09.zip.sha256). Both links pin the source commit. The archive includes BSD-3-Clause-Clear sample code, CC BY-SA 4.0 documentation, and separate dependency/model notices. It excludes model weights, credentials, private deployment configuration, and recorded runs.

Download the archive, verify its checksum, and extract it into a new source directory. The command stops if that source directory already exists:

```bash
python3.12 - <<'PY'
import hashlib
import io
from pathlib import Path
import urllib.request
import zipfile

base = "https://raw.githubusercontent.com/ranimandepudi/arm-learning-paths/84b9bcb7e8989113345c0a504cb668c34d10765f/content/learning-paths/servers-and-cloud-computing/axion-agent-studio/assets"
name = "axion-agent-studio-2026-11-09.zip"
expected = "aa64b1f04c8c18ab6440e6bdddb7b4a7ff23f4431fac791f3d3f2964297fb451"
destination = Path.home() / "axion-lp-review-2026-11-09"
if (destination / "axion-agent-studio").exists():
    raise SystemExit("Source directory already exists; choose a new review directory.")
with urllib.request.urlopen(f"{base}/{name}", timeout=60) as response:
    data = response.read()
actual = hashlib.sha256(data).hexdigest()
if actual != expected:
    raise SystemExit(f"Source checksum mismatch: {actual}")
destination.mkdir(parents=True, exist_ok=True)
(destination / name).write_bytes(data)
with zipfile.ZipFile(io.BytesIO(data)) as archive:
    archive.extractall(destination)
print(f"Verified {name}: {actual}")
PY
export LP_WORKDIR="$HOME/axion-lp-review-2026-11-09/axion-agent-studio"
cd "$LP_WORKDIR"
```

Expect `Verified` followed by the archive name and the checksum shown in the command. Read `LICENSE`, `LICENSE-SAMPLECODE`, `LICENSE-SUMMARY`, `NOTICE.md`, `MODEL_SOURCES.md`, and `VALIDATION.md` in the extracted directory. The validation record distinguishes local checks from the fresh GKE walkthrough, which remains pending for this draft.

Prepare the Python environment and run the companion's checks. Keep the same terminal and source directory for all subsequent application commands:

```bash
cd "$LP_WORKDIR"
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python -m pytest tests infra/test_manifests.py -q
node --check web/app.js
node --test tests/frontend_live_console.test.cjs
```

Local tests exercise contracts, validation logic, and application behavior using controlled inputs. They do not prove live Gemini access, model quality, or GKE isolation. Review the source release license and notices before using the application.

At this point you have checked the cluster boundary and prepared the application source. Next, build the arm64 images and generate manifests for your own environment.
