---
title: Move the assistant to C4A and compare results
description: Move only the assistant deployment to C4A, rerun the fixed benchmark, and compare it with the N4A baseline.
weight: 9
layout: "learningpathall"
---

## Create the mixed-placement overlay

If you opened a new terminal, return to the source tree and restore the required variables:

```bash
source "${HOME}/.storefront-axion-env"
cd "${REPO}"

export FRONTEND_IP="$(kubectl get service frontend-external \
  -o jsonpath='{.status.loadBalancer.ingress[0].ip}')"
export APP_URL="http://${FRONTEND_IP}"
```

Create a second overlay that keeps the storefront on N4A and moves only `shoppingassistantservice` to C4A:

```bash
mkdir -p kustomize/overlays/assistant-c4a

cat <<EOF > kustomize/overlays/assistant-c4a/kustomization.yaml
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
- path: keep-storefront-on-n4a.yaml
  target:
    kind: Deployment
- path: shoppingassistant-c4a.yaml
  target:
    kind: Deployment
    name: shoppingassistantservice
EOF

cat <<EOF > kustomize/overlays/assistant-c4a/keep-storefront-on-n4a.yaml
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

cat <<EOF > kustomize/overlays/assistant-c4a/shoppingassistant-c4a.yaml
- op: replace
  path: /spec/template/spec/nodeSelector
  value:
    cloud.google.com/gke-nodepool: ${C4A_NODE_POOL_NAME}
- op: replace
  path: /spec/template/spec/tolerations
  value:
  - key: kubernetes.io/arch
    operator: Equal
    value: arm64
    effect: NoSchedule
EOF
```

## Render the mixed-placement overlay

Review and render the overlay before you apply it:

```bash
sed -n '1,140p' kustomize/overlays/assistant-c4a/kustomization.yaml
sed -n '1,140p' kustomize/overlays/assistant-c4a/keep-storefront-on-n4a.yaml
sed -n '1,140p' kustomize/overlays/assistant-c4a/shoppingassistant-c4a.yaml
kubectl kustomize kustomize/overlays/assistant-c4a | sed -n '1,240p'
```

Do not continue if `newName`, `newTag`, or either node-pool value is blank.

{{% notice Note %}}
The first patch keeps the storefront on N4A by default. The second patch overrides only `shoppingassistantservice` and moves that deployment to C4A.
{{% /notice %}}

## Apply the mixed-placement overlay

Apply the overlay and wait for the rollout:

```bash
kubectl apply -k kustomize/overlays/assistant-c4a
kubectl rollout status deployment/frontend --timeout=600s
kubectl rollout status deployment/shoppingassistantservice --timeout=1200s
```

Confirm the final placement:

```bash
kubectl get pods -o wide | grep -E 'frontend|shoppingassistantservice'
kubectl get nodes -L cloud.google.com/gke-nodepool,node.kubernetes.io/instance-type,kubernetes.io/arch
```

The frontend should remain on N4A, and `shoppingassistantservice` should now run on C4A.

## Warm the assistant on C4A

Open the assistant endpoint to refresh the HTTP session cookie, then send one request through the storefront after the move. The cookie file preserves the same browser-like session across both calls:

```bash
curl --max-time 30 -s -c /tmp/assistant.cookies "${APP_URL}/assistant" >/dev/null

for i in {1..12}; do
  if curl --max-time 120 -s \
    -b /tmp/assistant.cookies \
    -c /tmp/assistant.cookies \
    -H 'Content-Type: application/json' \
    -d '{"message":"Show me one desk item that looks minimal and practical."}' \
    "${APP_URL}/bot" | tee /tmp/assistant-response.json | jq .; then
    break
  fi
  sleep 10
done
```

The response should contain a non-empty message.

## Run the fixed C4A benchmark

Run the same fixed batch with the expected pool set to C4A:

```bash
python3 workshop/fixed_batch_trial.py \
  --base-url "${APP_URL}" \
  --expected-pool "${C4A_NODE_POOL_NAME}" \
  --concurrency 2 \
  --prompts-per-worker 8 \
  --delay-seconds 0.2 \
  --request-timeout-seconds 120 \
  --telemetry-interval-seconds 0.5 \
  --idle-threshold-cores 1.0 \
  --idle-stable-samples 3 \
  --idle-timeout-seconds 180 \
  --request-output-file workshop/request-fixed-c4a.jsonl \
  --telemetry-output-file workshop/telemetry-fixed-c4a.jsonl | \
  tee workshop/fixed-c4a-summary.log
```

Print the C4A summary line:

```bash
grep 'SUMMARY_JSON' workshop/fixed-c4a-summary.log
```

The summary should show successful requests and the assistant running on the C4A node pool. Do not compare the runs if the summary line is missing or reports a different node pool.

## Compare the two runs

Compare the N4A and C4A summaries:

```bash
python3 workshop/compare_summaries.py \
  workshop/fixed-n4a-summary.log \
  workshop/fixed-c4a-summary.log | \
  sed '/^Interpretation$/,$d'
```

This displays the measured comparison table without adding a predetermined placement conclusion. Lower batch duration and request latency indicate the faster run for those measurements.

Focus on these signals:

- Successful request count
- Total benchmark duration
- Average request latency
- Maximum request latency
- Average assistant CPU cores during the measured batch

Your numbers can vary by prompt mix, model warmup state, node pressure, and cluster conditions. Treat the comparison as evidence for this assistant workflow, and repeat the same pattern with your own traffic before choosing a placement.

{{% notice Note %}}
Assistant CPU values come from sampled Kubernetes telemetry. Short bursts can be underrepresented, especially on faster runs. Treat request success, benchmark duration, and latency as the primary comparison signals.
{{% /notice %}}

## Explain the result

You changed one architectural variable: the placement of the assistant. The storefront tier, prompts, model, traffic shape, and benchmark script stayed the same.

The application now has three states:

- Storefront only on N4A
- Storefront plus assistant on N4A
- Storefront on N4A with only the assistant on C4A

That sequence is the core architectural point. A modern application can contain a steady application tier and a bursty AI reasoning tier. N4A supports the steady storefront and core services, while C4A gives you a placement to evaluate for concentrated, latency-sensitive assistant work.

Both Axion machine series run `arm64`, so the same assistant image moves between the Neoverse N3-based N4A pool and the Neoverse V2-based C4A pool. You can evaluate placement without maintaining a second image or build pipeline.

For this application, the useful pattern is not replacing one machine series with another. It is placing each workload tier where its behavior fits best.

If your N4A and C4A results are close, or if N4A looks better for a particular run, that is still useful information. The decision should come from the workload behavior you observe, not from assuming one Axion-based machine series is always the right answer.

## What you've accomplished

You've built, observed, and compared a mixed-placement storefront application on Axion. You kept the storefront on N4A, moved only the assistant tier to C4A, and used the same benchmark to compare both placements.

You are now ready to use the same overlay and benchmark pattern to evaluate which Axion-based machine series matches each tier's workload behavior.
