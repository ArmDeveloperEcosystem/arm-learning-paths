---
title: Deploy the assistant on N4A
description: Add the assistant component to the storefront and keep the application on the N4A node pool.
weight: 7
layout: "learningpathall"
---

## Create the N4A overlay

If you opened a new terminal, return to the source tree and restore the required variables:

```bash
cd "${HOME}/n4a-c4a/microservices-demo"

export PROJECT_ID="$(gcloud config get-value project)"
export ARTIFACT_REGION="us-central1"
export ARTIFACT_REPO="axion-workshop"
export ASSISTANT_IMAGE_REPO="${ARTIFACT_REGION}-docker.pkg.dev/${PROJECT_ID}/${ARTIFACT_REPO}/shoppingassistantservice"
export ASSISTANT_IMAGE_TAG="lab-v1"
export N4A_NODE_POOL_NAME="arm64-pool-n4a2"
export FRONTEND_IP="$(kubectl get service frontend-external \
  -o jsonpath='{.status.loadBalancer.ingress[0].ip}')"
export APP_URL="http://${FRONTEND_IP}"
```

Create a Kustomize overlay that adds the assistant component and keeps the full storefront, including the assistant, on the N4A node pool:

```bash
mkdir -p kustomize/overlays/assistant-n4a

cat <<EOF > kustomize/overlays/assistant-n4a/kustomization.yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
- ../../base
components:
- ../../components/shopping-assistant
images:
- name: shoppingassistantservice
  newName: ${ASSISTANT_IMAGE_REPO}
  newTag: ${ASSISTANT_IMAGE_TAG}
patches:
- path: node-selector.yaml
  target:
    kind: Deployment
EOF

cat <<EOF > kustomize/overlays/assistant-n4a/node-selector.yaml
- op: add
  path: /spec/template/spec/nodeSelector
  value:
    cloud.google.com/gke-nodepool: ${N4A_NODE_POOL_NAME}
- op: add
  path: /spec/template/spec/tolerations
  value:
  - key: kubernetes.io/arch
    operator: Equal
    value: arm64
    effect: NoSchedule
EOF
```

## Render the overlay

Review the overlay files and render the manifest:

```bash
sed -n '1,120p' kustomize/overlays/assistant-n4a/kustomization.yaml
sed -n '1,120p' kustomize/overlays/assistant-n4a/node-selector.yaml
kubectl kustomize kustomize/overlays/assistant-n4a | sed -n '1,240p'
```

Do not apply the overlay if the rendered manifest has an empty image name, image tag, or node-pool value.

## Apply the overlay

Apply the overlay and wait for the frontend and assistant deployments:

```bash
kubectl apply -k kustomize/overlays/assistant-n4a
kubectl rollout status deployment/frontend --timeout=600s
kubectl rollout status deployment/shoppingassistantservice --timeout=1200s
```

{{% notice Note %}}
`kubectl apply -k` reapplies the full rendered application state. It is normal to see existing deployments reported as `configured`. The `shopping-assistant` component patches `frontend`, so a frontend rollout is expected.
{{% /notice %}}

## Confirm pod placement

Check where the frontend and assistant pods landed:

```bash
kubectl get pods -o wide | grep -E 'frontend|shoppingassistantservice'

ASSISTANT_POD="$(kubectl get pod -l app=shoppingassistantservice \
  -o jsonpath='{.items[0].metadata.name}' 2>/dev/null || true)"

echo "${ASSISTANT_POD}"
if [ -n "${ASSISTANT_POD}" ]; then
  kubectl describe pod "${ASSISTANT_POD}" | \
    grep -E 'Node:|Image:|Pulling|Pulled|Ready:' || true
fi
```

The `frontend` and `shoppingassistantservice` pods should both be on the N4A node pool.

## Check the assistant logs

Inspect both containers in the assistant pod:

```bash
kubectl logs deployment/shoppingassistantservice -c server --tail=20
kubectl logs deployment/shoppingassistantservice -c ollama --tail=20
```

The `server` container serves the assistant API. The `ollama` container prepares the local model runtime.

{{% notice Tip %}}
The first rollout can take a few minutes because the Ollama sidecar pulls the model when the pod starts. Early `/readyz` checks can return `503` until the model is available.
{{% /notice %}}

## Validate the assistant through the storefront

Create a session with cookies and send one assistant request through the storefront:

```bash
curl --max-time 30 -s -c /tmp/assistant.cookies "${APP_URL}/assistant" >/dev/null

for i in {1..12}; do
  if curl --max-time 120 -s \
    -b /tmp/assistant.cookies \
    -c /tmp/assistant.cookies \
    -H 'Content-Type: application/json' \
    -d '{"message":"Find a mug for a minimalist desk setup."}' \
    "${APP_URL}/bot" | tee /tmp/assistant-response.json | jq .; then
    break
  fi
  sleep 10
done
```

The JSON response should include a non-empty assistant message. The exact product names can vary, but the response should be grounded in the live product catalog.

## Try the browser flow

Open the storefront URL in your browser. Refresh the page if it was already open before the assistant-enabled frontend rolled out.

Try these prompts in the assistant panel:

```text
Find one desk accessory that looks clean and minimalist for a home office.
Add that item to my cart.
yes
What is in my cart now?
```

The assistant should recommend a catalog item, ask for confirmation before changing the cart, and then show the cart contents.

## What you've accomplished

You've deployed the assistant on N4A and validated it through the same storefront path that a shopper uses.

Next, you'll observe the assistant as a live workload and capture the N4A benchmark baseline.
