---
title: Preserve results and delete cloud resources
description: Preserve the generated code and execution output, release the agent claim, and remove the dedicated GKE cluster.
weight: 8
layout: learningpathall
---

## Preserve the results you need

Your local machine retains the small-test result, CSV reports, interactive observations, and `agy` execution captures. Preserve the `agy` conversations and the final Project permission state before deleting the remote environment.

Inspect your local files from your terminal:

```bash
cd "$LP_WORKDIR"
ls output
ls runs/csv
ls "$AGY_SESSION/remote-first"
```

The bridge audit can contain task commands and output. Review it before sharing. Keep account configuration and kubeconfig files private.

## Release the agent session claim

Make sure `agy` is closed, then release the sandbox claim created on the previous page:

```bash
python3 mcp-bridge/finish_session.py --record "$AGY_RECORD"
```

This verifies claim ownership, deletes the claim and its bound Pod, and preserves the bridge logs.

## Remove the dedicated namespace and warm pool

The small-test and interactive pages release their own claims, and the CSV runner cleans up its claim. Inspect what remains in the tutorial namespace:

```bash
kubectl --context "$GKE_CONTEXT" -n "$NAMESPACE" get sandboxclaim,sandboxwarmpool,sandbox,pod
```

Remove the warm pool so it stops replenishing available sandboxes:

```bash
kubectl --context "$GKE_CONTEXT" -n "$NAMESPACE" delete sandboxwarmpool axion-python-pool --ignore-not-found
```

If you stopped an earlier task midway, inspect and delete its recorded tutorial claim by name. After confirming that this dedicated namespace contains only tutorial resources, delete it:

```bash
kubectl --context "$GKE_CONTEXT" delete namespace "$NAMESPACE" --wait=true
```

Deleting the namespace removes its remaining namespaced resources. Node and control-plane charges continue until you delete the cluster.

## Delete the tutorial cluster

Confirm that the project, location, and cluster name still identify the dedicated cluster you created. Then delete it:

```bash
printf 'Project: %s\nLocation: %s\nCluster: %s\n' "$PROJECT_ID" "$LOCATION" "$CLUSTER_NAME"
gcloud container clusters delete "$CLUSTER_NAME" \
  --project="$PROJECT_ID" --location="$LOCATION" --quiet
```

Wait for the deletion to complete before continuing — it can take a few minutes. Check the project for remaining clusters, disks, and addresses:

```bash
gcloud container clusters list --project="$PROJECT_ID"
gcloud compute disks list --project="$PROJECT_ID"
gcloud compute addresses list --project="$PROJECT_ID"
```

Confirm that the tutorial cluster is absent. Investigate any leftover tutorial-owned resources before removing them; retain unrelated project resources. If capacity troubleshooting created another tutorial cluster in a different zone, remove that cluster too.

Once the cluster is deleted, remove the VPC subnet and network created on page 1:

```bash
gcloud compute networks subnets delete "$SUBNETWORK" \
  --region="$REGION" --project="$PROJECT_ID" --quiet
gcloud compute networks delete "$NETWORK" \
  --project="$PROJECT_ID" --quiet
```

You didn't create an external load balancer, custom image registry, or persistent workload disk in this walkthrough. Existing project logging, storage, and other services can still incur charges independently.

## What you've accomplished

You've created an Arm sandbox pool, tested its access restrictions, run a CSV task, inspected a sandbox interactively, and used the Antigravity CLI to run agent-generated Python in the remote sandbox. You retained results while removing the task environments and the dedicated cluster.
