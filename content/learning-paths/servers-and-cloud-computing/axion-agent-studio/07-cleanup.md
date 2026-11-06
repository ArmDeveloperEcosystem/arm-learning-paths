---
title: Save evidence and clean up
description: Export the review results and remove only the resources created for this Learning Path.
weight: 8
layout: learningpathall
---

## Preserve what you need for review

Export the run, artifacts, and metrics using the commands in [Inspect the run evidence](../05-run/#inspect-the-run-evidence) before deleting workloads. Record any manual checkout checks alongside them. Review evidence for project identifiers, endpoint addresses, account names, and private code before sharing it publicly.

The manager stores run data in an `emptyDir` volume. The validator keeps accepted candidates in process memory. The model init container copies weights into another temporary volume. A Pod replacement can lose this state; an old dashboard record does not guarantee its candidate quote service is still available. Rerun the workflow if the validated candidate has disappeared.

## Remove the tutorial workloads

Return to the terminal holding the port-forward and press **Ctrl+C**. In the deployment terminal, confirm the context and review the namespace contents:

```bash
cd "$LP_WORKDIR"
kubectl config current-context
kubectl -n "$NAMESPACE" get pods,services,sandboxes.agents.x-k8s.io
```

For the dedicated installation created by this tutorial, have the same authorized operator or administrator remove the manifest set, including its cluster-scoped node observer role and binding:

```bash
kubectl delete -f generated/full.json
```

This manifest includes the namespace, so deletion removes everything inside it. Use this command only for the dedicated tutorial installation you checked earlier. If another team has added resources there, coordinate cleanup before deleting the namespace.

Deleting Pods or a namespace does **not** stop charges for a fixed-size GKE node pool. Have the cluster owner scale down or remove dedicated tutorial pools according to your organization's procedure. Do not stop individual managed VMs in Compute Engine as a substitute for changing their GKE node pool.

The cluster, shared VPC, registry, and node pools were prerequisites and are not deleted by the application manifests. Remove only tutorial-specific image versions if you no longer need them. If the manager's IAM grant was created solely for this exercise, have its administrator remove that specific principal binding. Keep shared registry, node, and IAM configuration intact.

## Review the outcome

You deployed a bounded coding-agent workflow, used local Gemma inference on C4A for three roles, validated generated behavior on N4A, and served the accepted shop through an N4A manager. You also separated VM capacity from Pod quotas and measured usage.

Keep your run evidence with the configuration and image digests you used. Record any failed or skipped checks so another developer can understand what your run verified.
