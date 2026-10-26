---
title: Preserve results and delete cloud resources
description: Preserve the generated code and execution output, release the agent claim, and remove the dedicated GKE cluster.
weight: 8
layout: learningpathall
---

## Preserve the results that you need

Your local machine retains the small-test result, CSV reports, interactive observations, and `agy` execution captures. Preserve the `agy` conversations and the final project permission state before deleting the remote environment.

Inspect your local files from your terminal:

```bash
cd "$LP_WORKDIR"
ls output
ls runs/csv
ls "$AGY_SESSION/remote-first"
```

The bridge audit can contain task commands and output. Review it before sharing. Keep account configuration and kubeconfig files private.

## Release the agent session claim

Make sure that `agy` is closed, then release the sandbox claim that you created earlier:

```bash
python3 mcp-bridge/finish_session.py --record "$AGY_RECORD"
```

The script verifies claim ownership, deletes the claim and its bound Pod, and preserves the bridge logs.

## Remove the dedicated namespace and warm pool 

Inspect the claims that remain in the Learning Path namespace:

```bash
kubectl --context "$GKE_CONTEXT" -n "$NAMESPACE" get sandboxclaim,sandboxwarmpool,sandbox,pod
```

Remove the warm pool so that it stops replenishing available sandboxes:

```bash
kubectl --context "$GKE_CONTEXT" -n "$NAMESPACE" delete sandboxwarmpool axion-python-pool --ignore-not-found
```

If you stopped an earlier task midway, inspect and delete its claim by name. 

After confirming that the namespace contains only resources associated with the Learning Path, delete the namespace:

```bash
kubectl --context "$GKE_CONTEXT" delete namespace "$NAMESPACE" --wait=true
```

Deleting the namespace removes its remaining namespaced resources. Node and control-plane charges continue until you delete the cluster.

## Delete the cluster

Confirm that the project, location, and cluster name still identify the cluster that you created. After confirming, delete the cluster:

```bash
printf 'Project: %s\nLocation: %s\nCluster: %s\n' "$PROJECT_ID" "$LOCATION" "$CLUSTER_NAME"
gcloud container clusters delete "$CLUSTER_NAME" \
  --project="$PROJECT_ID" --location="$LOCATION" --quiet
```

Deletion can take a few minutes. Wait for the deletion to complete before continuing. 

Check the project for remaining clusters, disks, and addresses:

```bash
gcloud container clusters list --project="$PROJECT_ID"
gcloud compute disks list --project="$PROJECT_ID"
gcloud compute addresses list --project="$PROJECT_ID"
```

Confirm that the cluster that you deleted is absent. Investigate any leftover resources associated with the Learning Path before removing them. Retain unrelated project resources. If you needed to create another cluster in a different zone to troubleshoot capacity issues, remove that cluster too.

After cluster deletion, remove the VPC subnet and network that you created earlier:

```bash
gcloud compute networks subnets delete "$SUBNETWORK" \
  --region="$REGION" --project="$PROJECT_ID" --quiet
gcloud compute networks delete "$NETWORK" \
  --project="$PROJECT_ID" --quiet
```

You didn't create an external load balancer, custom image registry, or persistent workload disk. Existing project logging, storage, and other services can still incur charges independently.

## What you've accomplished

You've retained results while removing the task environments and the dedicated cluster for the Learning Path.

You can extend the Learning Path workflow to run agent-generated code in an isolated environment for your own use cases.


