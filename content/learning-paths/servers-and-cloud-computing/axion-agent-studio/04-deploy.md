---
title: Deploy and inspect the workers
description: Validate the manifests against the installed API, deploy the workflow, and verify its actual placement and readiness.
weight: 5
layout: learningpathall
---

## Validate the manifests before applying them

Continue in the same terminal and source directory. Verify that the installed Agent Sandbox controller is running, and record its configured image and the image IDs of its Pods. The following names match Google's manifest-based installation; use the actual controller namespace and Deployment name supplied by your administrator if they differ:

```bash
export SANDBOX_CONTROLLER_NAMESPACE="agent-sandbox-system"
export SANDBOX_CONTROLLER_DEPLOYMENT="agent-sandbox-controller"
kubectl -n "$SANDBOX_CONTROLLER_NAMESPACE" rollout status \
  "deployment/$SANDBOX_CONTROLLER_DEPLOYMENT" --timeout=300s
kubectl -n "$SANDBOX_CONTROLLER_NAMESPACE" get deployment \
  "$SANDBOX_CONTROLLER_DEPLOYMENT" \
  -o jsonpath='{range .spec.template.spec.containers[*]}{.name}{" "}{.image}{"\n"}{end}'
kubectl -n "$SANDBOX_CONTROLLER_NAMESPACE" get pods \
  -o custom-columns='POD:.metadata.name,OWNER:.metadata.ownerReferences[*].name,IMAGE_IDS:.status.containerStatuses[*].imageID'
```

Keep the controller version and image IDs with your run evidence. An installed CRD alone does not prove that a controller is running or that it can create the worker Pods.

Check that the namespace is unused before a new installation. If it already contains another deployment, use another existing compatible learning cluster or coordinate with its owner; do not overwrite it.

```bash
cd "$LP_WORKDIR"
kubectl get namespace "$NAMESPACE"
```

For a fresh environment, the namespace lookup must report `NotFound`. Create this dedicated namespace before dry-running namespaced resources; a dry-run namespace creation alone does not make the namespace available to subsequent objects:

```bash
kubectl create namespace "$NAMESPACE"
kubectl apply --dry-run=server -f generated/full.json
```

If server-side dry-run rejects the Sandbox schema, stop. Resolve API compatibility before applying the workloads. A successful render proves JSON construction, while server-side dry-run checks admission against the actual cluster. The controller creates the underlying Sandbox Pods only after you apply the resources, so their scheduling and readiness still need separate checks.

After dry-run succeeds, have an identity authorized for the namespaced resources and the narrowly scoped node observer role apply the workload set:

```bash
kubectl apply -f generated/full.json
kubectl -n "$NAMESPACE" get sandboxes.agents.x-k8s.io
kubectl -n "$NAMESPACE" get pods -o wide
kubectl -n "$NAMESPACE" rollout status deployment/studio-manager --timeout=300s
```

Model images are large. Follow the Pod events while the init container copies model weights into its temporary volume. Allow time for image pulls and model loading; do not interpret an initializing worker as an inference failure.

```bash
kubectl -n "$NAMESPACE" get events --sort-by=.metadata.creationTimestamp
kubectl -n "$NAMESPACE" wait --for=condition=Ready \
  sandboxes.agents.x-k8s.io/worker-backend \
  sandboxes.agents.x-k8s.io/worker-frontend \
  sandboxes.agents.x-k8s.io/worker-qa \
  sandboxes.agents.x-k8s.io/validator --timeout=900s
kubectl -n "$NAMESPACE" wait --for=condition=Ready pod \
  -l app=axion-agent-studio --timeout=300s
kubectl -n "$NAMESPACE" get pods \
  -o custom-columns='POD:.metadata.name,UID:.metadata.uid,NODE:.spec.nodeName,RUNTIME:.spec.runtimeClassName,READY:.status.containerStatuses[*].ready,IMAGE_IDS:.status.containerStatuses[*].imageID'
kubectl get nodes \
  -L kubernetes.io/arch,node.kubernetes.io/instance-type,studio.axion.dev/pool
```

Confirm three Ready worker Sandboxes and a separate Ready validator Sandbox. Each execution Pod must use `gvisor` and run on a node whose architecture is `arm64`. Match the actual node names and machine types: backend, frontend, and QA share the single eligible C4A node in this setup; the manager and validator use their respective N4A nodes. If a wait times out, inspect the Sandbox conditions, Pod events, and logs before proceeding.

Save the workload identities, placement, configured images, resolved image IDs, and init-container results before starting a run:

```bash
mkdir -p review-evidence
kubectl -n "$NAMESPACE" get sandboxes.agents.x-k8s.io -o json \
  > review-evidence/sandboxes.json
kubectl -n "$NAMESPACE" get pods -o json > review-evidence/pods.json
kubectl get nodes \
  -l 'studio.axion.dev/pool in (n4a-regular,c4a-sandbox,n4a-sandbox)' \
  -o json > review-evidence/nodes.json
```

Review these files for private infrastructure details before sharing them. Node labels and resolved image IDs provide placement and artifact evidence independently of the application's health response.

Inspect an actual worker rather than relying only on diagram labels:

```bash
export BACKEND_POD="$(kubectl -n "$NAMESPACE" get pod -l component=worker,role=backend -o jsonpath='{.items[0].metadata.name}')"
kubectl -n "$NAMESPACE" get pod "$BACKEND_POD" \
  -o jsonpath='{.spec.containers[?(@.name=="llama")].args}{"\n"}'
kubectl -n "$NAMESPACE" logs "$BACKEND_POD" -c llama --tail=50
```

Check the model name, four inference threads, context size, and zero GPU layers. Do not paste access tokens or private endpoint details into public logs.

## Open the dashboard through the manager

Keep your deployment terminal open so its environment variables remain available. Open a second terminal solely for port-forwarding, set the same namespace there, and forward the regular-pool manager service. The service is internal; the tutorial does not create a public load balancer or ingress.

```bash
export NAMESPACE="axion-agent-studio"
kubectl -n "$NAMESPACE" port-forward service/studio-manager 8090:8080 --address 127.0.0.1
```

Leave the port-forward running. In a browser, open [Axion Agent Studio](http://127.0.0.1:8090/?view=booth). Return to your original deployment terminal for the remaining commands and inspect the live configuration:

```bash
curl --fail --silent --show-error http://127.0.0.1:8090/api/config | python3 -m json.tool
```

The response must contain `live_available: true` before you submit work. This preflight check confirms service health and the presence of hosted-model configuration. It does not make a Gemini request or prove that credentials and model access work; the planning stage of your first live run checks that access. The separate `/health` endpoint only confirms that the manager process is responding.

Resolve missing workers, missing hosted-model configuration, or an unreachable validator before continuing.

## Troubleshoot deployment issues

| Symptom | Check |
| --- | --- |
| Sandbox admission fails | Installed API version and fields, controller availability, server-side dry-run details |
| Pod remains Pending | Arm labels, gVisor runtime and taints, allocatable CPU/memory, ResourceQuota |
| Image pull fails | Registry path, architecture, node identity's repository access |
| Worker never becomes ready | Init-container events, model checksum and size, llama container logs |
| Hosted planning returns 403 | Manager's Workload Identity principal, model permission, project and location |
| CPU metrics are unavailable | Metrics API and observer permissions; absence of a sample is not zero CPU |
| Browser connection is refused | Port-forward process, local port, manager Pod and Service endpoints |

Once readiness passes, you have connected the dashboard to the live services. Next, submit a request and inspect the result.
