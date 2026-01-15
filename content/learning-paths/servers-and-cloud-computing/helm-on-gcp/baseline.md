---
title: Validate Helm workflows on a Google Axion C4A virtual machine
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview
This section walks you through baseline testing to confirm that Helm works correctly on an Arm64-based Kubernetes cluster by validating core workflows such as install, upgrade, and uninstall.

## Add Helm repository
Add the Bitnami Helm chart repository and update the local index:

```console
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update
```

You should see an output similar to:
```output
"bitnami" has been added to your repositories
Hang tight while we grab the latest from your chart repositories...
...Successfully got an update from the "bitnami" chart repository
Update Complete. ⎈Happy Helming!⎈
```

## Install a sample application
Install a sample NGINX application using a Helm chart:

```console
helm install nginx bitnami/nginx
```
Deploy a simple test app to validate that Helm can create releases on the cluster.

The output is similar to the following (warnings can be safely ignored as they don't affect functionality):
```output
NAME: nginx
LAST DEPLOYED: Wed Dec  3 07:34:04 2025
NAMESPACE: default
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
CHART NAME: nginx
CHART VERSION: 22.3.3
APP VERSION: 1.29.3
```


## Validate deployment
Verify that the Helm release is created:

```console
helm list
```

Confirm Helm recorded the release and that the deployment exists.

The output is similar to:
```output
NAME    NAMESPACE       REVISION        UPDATED                                 STATUS          CHART           APP VERSION
nginx   default         1               2025-12-09 21:04:15.944165326 +0000 UTC deployed        nginx-22.3.3    1.29.3 
```

Check Kubernetes resources:

```console
kubectl get pods
kubectl get svc
```
The output is similar to:
```output
NAME                     READY   STATUS    RESTARTS   AGE
nginx-7b9564dc4b-2ghkw   1/1     Running   0          3m5s

NAME         TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)                      AGE
kubernetes   ClusterIP      10.96.0.1       <none>        443/TCP                      4m28s
nginx        LoadBalancer   10.96.216.137   <pending>     80:32708/TCP,443:31052/TCP   3m6s
```
All pods should be in the **Running** state. If pods are in **Pending** state, wait 30-60 seconds for container images to download, then retry the commands above. 


## Validate Helm lifecycle
Confirm that Helm supports the full application lifecycle on Arm64.

### Upgrade the release

```console
helm upgrade nginx bitnami/nginx
```
Test Helm's ability to update an existing release to a new revision.

The output is similar to:
```output
Release "nginx" has been upgraded. Happy Helming!
```

### Uninstall the release
Ensure Helm can cleanly remove the release and associated resources.

```console
helm uninstall nginx
```

The output is similar to:
```output
release "nginx" uninstalled
```

## What you've accomplished and what's next

You've validated Helm's core functionality by:
- Installing a sample application using Helm charts
- Upgrading an existing release to a new revision
- Uninstalling releases and cleaning up resources
- Verifying that all workflows execute successfully on Arm64

Next, you'll benchmark Helm's performance by measuring concurrent operations and evaluating how well it handles parallel workloads on your Arm64 Kubernetes cluster.
