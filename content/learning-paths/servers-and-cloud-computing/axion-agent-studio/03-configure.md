---
title: Configure the local model and images
description: Pin the recorded Gemma configuration, build arm64 application images, and render portable manifests.
weight: 4
layout: learningpathall
---

## Select the recorded model configuration

The successful recorded run uses Gemma 4 E4B IT in GGUF `Q4_0` format. Use the same model for all three roles first. A smaller model changes the quality and timing experiment; it is not a drop-in validation of this workflow.

| Setting | Recorded value |
| --- | --- |
| Model file | `gemma-4-E4B-it-Q4_0.gguf` |
| File size | 4,590,807,392 bytes |
| llama.cpp runtime | Build `b11580`, revision beginning `4413a192` |
| Inference threads / batch threads | 4 / 4 per model server |
| Context size | 8,192 tokens |
| Parallel inference slots | 1 per model server |
| GPU layers | 0 |
| Hosted planner | `gemini-3.8-flash`, through Vertex AI |

The model file's SHA-256 is:

```text
a555b900214b477d8880e7832e0b8925e139b0159640036b09fe472b6f2097f2
```

Review the [model repository and its terms](https://huggingface.co/ggml-org/gemma-4-E4B-it-GGUF/tree/b8093469224f83f5c38f691eb906c380e9e63114). The included downloader selects an immutable repository revision and verifies both size and checksum. It downloads about 4.6 GB:

```bash
cd "$LP_WORKDIR"
python -m worker.download_model --model e4b
export MODEL_FILE="$LP_WORKDIR/models/gemma-4-E4B-it-Q4_0.gguf"
export GEMINI_MODEL="gemini-3.8-flash"
```

If your organization supplies the same file through an approved channel, point `MODEL_FILE` at that file instead. Do not silently substitute different weights. Check [Gemini model availability](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/3-8-flash) for your project and selected location before deploying.

## Build the arm64 images

Authenticate Docker to your own registry and build with a Buildx builder that supports the target platform. The application Dockerfiles resolve arm64 wheels in a builder stage and copy them into the arm64 runtime.

```bash
cd "$LP_WORKDIR"
mkdir -p .build
gcloud auth configure-docker "$REGION-docker.pkg.dev"
docker buildx inspect --bootstrap

docker buildx build --platform linux/arm64 \
  -f worker/Dockerfile -t "$REGISTRY/worker:$TAG" \
  --metadata-file .build/worker.json --push .
docker buildx build --platform linux/arm64 \
  -f infra/Dockerfile.studio -t "$REGISTRY/studio:$TAG" \
  --metadata-file .build/studio.json --push .
```

Package the verified model as an init-container image. Stage only the verified model file into a dedicated build context:

```bash
python tools/stage_model.py "$MODEL_FILE"
docker buildx build --platform linux/arm64 \
  -f "$LP_WORKDIR/infra/Dockerfile.model-local" \
  --build-arg "BASE_IMAGE=$REGISTRY/worker:$TAG" \
  --build-arg "MODEL_FILENAME=gemma-4-E4B-it-Q4_0.gguf" \
  -t "$REGISTRY/model:$TAG" --metadata-file .build/model.json \
  --push .build/model
```

The renderer uses this recorded llama.cpp image digest:

```text
ghcr.io/ggml-org/llama.cpp@sha256:21397f7329ff6fd5705b0bcedcb7e2ce10b5ce97cc12e6564278ac7133523ea6
```

The digest pins the runtime image, while the model checksum pins the weights. Keep build output and image digests with your review evidence. Before a public release, rebuild and verify all application dependencies and record their resulting image digests.

## Describe your own network

Obtain the primary node, Pod, and Service ranges from the cluster administrator. The supplied renderer requires non-overlapping private IPv4 ranges within RFC 1918 address space (`10.0.0.0/8`, `172.16.0.0/12`, or `192.168.0.0/16`), with prefix lengths from `/8` to `/30`. The commands here configure one range for each category. The renderer rejects other network arrangements. Use your cluster's actual ranges; do not substitute broader ranges to pass configuration checks.

For the API rule, use the actual destination behind the in-cluster `default/kubernetes` Service after address translation, expressed as one IPv4 `/32`. This can differ from the external address in your kubeconfig. Do not use the virtual Service IP.

Inspect the Service's backend addresses, and have the administrator confirm which address applies to your cluster's data plane:

```bash
kubectl -n default get endpointslice \
  -l kubernetes.io/service-name=kubernetes -o yaml
```

If your cluster exposes that backend only through a legacy Endpoints object, inspect `kubectl -n default get endpoints kubernetes -o yaml`. The renderer accepts one verified backend address for this recorded network arrangement. A cluster requiring several API backend addresses needs a reviewed manifest change before deployment. The review renderer checks this distinction to avoid opening its API rule to a whole network.

To populate the dashboard's verified VM labels and node statistics, capture only the tutorial nodes. This creates local configuration data; review the names, machine types, and internal addresses before using it:

```bash
kubectl get nodes \
  -l 'studio.axion.dev/pool in (n4a-regular,c4a-sandbox,n4a-sandbox)' \
  -o json > nodes.local.json
python - <<'PYNODES'
import json
from pathlib import Path
nodes = json.loads(Path("nodes.local.json").read_text())["items"]
if not 1 <= len(nodes) <= 8:
    raise SystemExit("Expected one to eight explicitly selected tutorial nodes")
addresses = {}
for node in nodes:
    name = node["metadata"]["name"]
    labels = node["metadata"].get("labels", {})
    ips = [a["address"] for a in node["status"]["addresses"]
           if a["type"] == "InternalIP" and ":" not in a["address"]]
    if labels.get("kubernetes.io/arch") != "arm64" or len(ips) != 1:
        raise SystemExit(f"Review architecture and primary IPv4 for {name}")
    addresses[name] = ips[0]
    print(name, labels.get("node.kubernetes.io/instance-type"), ips[0])
Path("node-addresses.local.json").write_text(json.dumps(addresses, indent=2) + "\n")
PYNODES
```

The renderer confines node-stat requests to this explicit mapping and your declared node subnet ranges. An administrator must approve the generated ClusterRole and ClusterRoleBinding, which grant `get` on `nodes` and `nodes/stats` for these node names. The node-stat response can include other Pods on the approved node; the application filters its own workloads, but that namespace filtering is not enforced by the `nodes/stats` RBAC permission. Node addresses can change after node replacement; regenerate and re-review the mapping then. Do not publish this local file.

You can omit `--node-addresses` if your administrator does not permit this access, but verified VM details and some worker metrics will be unavailable in the dashboard. In that case use `kubectl` for placement evidence and report missing metrics rather than treating them as zero.

Set these values to your verified ranges:

```bash
export KUBE_API_CIDR="your-control-plane-ip/32"
export NODE_CIDR="your-node-subnet-cidr"
export POD_CIDR="your-pod-range-cidr"
export SERVICE_CIDR="your-service-range-cidr"

python tools/configure.py \
  --project "$PROJECT_ID" --registry "$REGISTRY" --tag "$TAG" \
  --kube-api-cidr "$KUBE_API_CIDR" --node-cidr "$NODE_CIDR" \
  --pod-cidr "$POD_CIDR" --service-cidr "$SERVICE_CIDR" \
  --node-addresses node-addresses.local.json \
  --gemini-model "$GEMINI_MODEL" --output config.local.json
```

Pin the three application images to the digests written by Buildx, then render the manifests. Run this from the same source directory, where `.build/*.json` contains the successful build metadata:

```bash
python - <<'PYCONFIG'
import json, os, re
from pathlib import Path
path = Path("config.local.json")
config = json.loads(path.read_text())
for name in ("worker", "studio", "model"):
    metadata = json.loads(Path(f".build/{name}.json").read_text())
    digest = metadata["containerimage.digest"]
    if not re.fullmatch(r"sha256:[0-9a-f]{64}", digest):
        raise SystemExit(f"Invalid image digest for {name}")
    config[f"{name}_image"] = f"{os.environ['REGISTRY']}/{name}@{digest}"
path.write_text(json.dumps(config, indent=2) + "\n")
PYCONFIG
python infra/render.py --config config.local.json --require-digests \
  --phase full --output generated/full.json
```

The configuration selects C4A for all three engineers, N4A for the manager, and N4A for validation. It does not restore a previous recording or inject a successful result. Review the generated JSON before applying it. Do not commit your local configuration, network addresses, or credentials to a public repository.

Each engineer Pod requests 4.25 CPUs and 8.5 GiB of memory across its worker and model containers. Its combined limits are 6.5 CPUs and 13 GiB. Kubernetes schedules using requests: the three CPU requests total 12.75, while their 19.5 total CPU limit permits bursts but does not create more than the shared node's capacity.

## What you have configured

You have selected the recorded model settings, built and pinned your own arm64 images, and generated manifests using your cluster network. Next, check those manifests against the live API before deployment.
