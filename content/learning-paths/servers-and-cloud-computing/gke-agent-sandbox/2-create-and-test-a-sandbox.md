---
title: Claim a sandbox and test its restrictions
description: Create a Python sandbox warm pool and verify Arm execution, non-root identity, and a denied system-directory write.
weight: 4
layout: learningpathall
---

## Define the Python environment

Continue on your local machine in `$LP_WORKDIR`. Download the files that you need to define the sandbox environment:

```bash
cd "$LP_WORKDIR"
BASE_URL=https://raw.githubusercontent.com/ArmDeveloperEcosystem/arm-learning-paths/main/content/learning-paths/servers-and-cloud-computing/gke-agent-sandbox/files
for FILE in \
  sandbox_common.py \
  sandbox.yaml \
  claim.py \
  workload.py; do
  curl -fL "$BASE_URL/$FILE" -o "$FILE" || exit 1
done
```

Inspect the template before applying it:

```bash
cat sandbox.yaml
```

The template selects the Arm gVisor node pool and uses `python:3.12.15-slim-bookworm`. The image provides Python on Debian 12 without installing Python packages on your local machine. Its principal settings are as follows:

| Setting | Effect |
| --- | --- |
| `runtimeClassName: gvisor` | Selects the sandbox runtime |
| UID and GID `1000` | Runs the workload without root identity |
| `readOnlyRootFilesystem: true` | Makes the image root filesystem read-only |
| Writable `/workspace` and `/tmp` volumes | Provides task and temporary storage |
| Dropped capabilities and no privilege escalation | Restricts process privileges |
| `automountServiceAccountToken: false` | Omits the default Kubernetes API token |
| `500m` CPU and `512Mi` memory limits | Bounds the configured compute resources of the Pod |

The container sleep command keeps it available for interactive tasks for up to 24 hours per start. These examples aren't persistent storage: the `emptyDir` workspace is tied to the lifetime of the Pod.

Apply the resources:

```bash
kubectl --context "$GKE_CONTEXT" create namespace "$NAMESPACE" --dry-run=client -o yaml \
  | kubectl --context "$GKE_CONTEXT" apply -f -
kubectl --context "$GKE_CONTEXT" apply -f sandbox.yaml
kubectl --context "$GKE_CONTEXT" -n "$NAMESPACE" get sandboxwarmpool,sandbox,pod -o wide
```

Wait for an available warm Pod to become ready before continuing.

## Claim and identify your sandbox

`claim.py` is a Python script that automates the sandbox lifecycle. The script creates a `SandboxClaim` against the warm pool and waits until a sandbox Pod is ready. It then records the exact claim, Sandbox, and Pod names in a local run directory. You'll use those recorded names in subsequent commands to target the right Pod.

Create the claim and wait for the Pod to be ready:

```bash
rm -rf "$LP_WORKDIR/runs/smoke"
python3 claim.py create \
  --context "$GKE_CONTEXT" --namespace "$NAMESPACE" \
  --pool axion-python-pool --purpose smoke --output-dir "$LP_WORKDIR/runs/smoke"
```

When `create` finishes, load the Pod name into your shell and verify the binding:

```bash
source "$LP_WORKDIR/runs/smoke/binding.env"
python3 claim.py check --record "$LP_WORKDIR/runs/smoke/run.json"
```

`binding.env` exports `POD_NAME` and related variables so that subsequent `kubectl exec` commands know which Pod to target. Each run needs a new output directory, so choose a different name if you repeat this step.

If readiness times out, inspect the claim and namespace events:

```bash
kubectl --context "$GKE_CONTEXT" -n "$NAMESPACE" get sandboxclaim,sandbox,pod -o wide
kubectl --context "$GKE_CONTEXT" -n "$NAMESPACE" get events --sort-by=.lastTimestamp
```

## Run the Python test

Review `workload.py` before running it:

```bash
cat workload.py
```

The script runs inside the sandbox and does four things:

- Reports the CPU architecture and user ID to confirm that it's running on Arm as a non-root user (UID 1000).
- Checks that the default Kubernetes service-account token is absent, as configured in the template.
- Attempts to write a file under `/etc`. This write is expected to fail because the root filesystem is read-only and the process runs without root privileges. A write to `/workspace` succeeds because the template mounts a writable volume there.
- Computes the sum of squares of integers 1 to 9 as a numeric result to confirm that the Python environment works.

Verify that the claim is still bound, then run the script and retrieve the result:

```bash
python3 claim.py check --record "$LP_WORKDIR/runs/smoke/run.json"
kubectl --context "$GKE_CONTEXT" -n "$NAMESPACE" exec -i "$POD_NAME" -c runtime -- \
  python3 - < workload.py
kubectl --context "$GKE_CONTEXT" -n "$NAMESPACE" exec "$POD_NAME" -c runtime -- \
  cat /workspace/result.json > "$LP_WORKDIR/output/result.json"
cat "$LP_WORKDIR/output/result.json"
```

The output is similar to:

```output
{
  "architecture": "aarch64",
  "uid": 1000,
  "sum_of_squares": 285,
  "service_account_token_present": false,
  "denied_write": {
    "errno": 13,
    "reason": "Permission denied"
  }
}
```
The `errno` value for the denied write can vary.

The script fails if the `/etc` write succeeds. `EACCES`, `EPERM`, or `EROFS` are all accepted denied-write results.

Record the runtime class and image ID:

```bash
kubectl --context "$GKE_CONTEXT" -n "$NAMESPACE" get pod "$POD_NAME" \
  -o jsonpath='{.spec.runtimeClassName}{"\n"}{.status.containerStatuses[0].imageID}{"\n"}' \
  > "$LP_WORKDIR/output/runtime-image.txt"
cat "$LP_WORKDIR/output/runtime-image.txt"
```

The runtime class should be `gvisor`.

## Release the claim for the test 

Delete only the verified claim and wait for its bound Sandbox and Pod to disappear:

```bash
python3 claim.py delete --record "$LP_WORKDIR/runs/smoke/run.json"
kubectl --context "$GKE_CONTEXT" -n "$NAMESPACE" get sandboxwarmpool,sandbox,pod -o wide
```

The helper confirms claim, Sandbox, and Pod deletion. The warm pool remains available and prepares a replacement Pod.

## What you've accomplished and what's next

You've run Python on Arm with a non-root user, retrieved a workspace artifact, and verified a denied system-directory write. 

Next, you'll use the same pool for a CSV analysis task with a reproducible failure and correction.
