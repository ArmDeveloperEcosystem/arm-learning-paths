---
title: Helm Baseline Testing on Google Axion C4A Arm Virtual Machine
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Helm Baseline Testing on GCP SUSE VMs
This guide walks you through baseline testing to confirm that Helm works correctly on an Arm64-based Kubernetes cluster by validating core workflows such as install, upgrade, and uninstall.

### Add Helm Repository
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

### Install a Sample Application
Install a sample NGINX application using a Helm chart:

```console
helm install nginx bitnami/nginx
```
Deploy a simple test app to validate that Helm can create releases on the cluster.

You should see an output that contains text similar to this (please ignore any WARNINGS you receive):
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


### Validate Deployment
Verify that the Helm release is created:

```console
helm list
```

Confirm Helm recorded the release and that the deployment exists.

You should see an output similar to:
```output
NAME    NAMESPACE       REVISION        UPDATED                                 STATUS          CHART           APP VERSION
nginx   default         1               2025-12-09 21:04:15.944165326 +0000 UTC deployed        nginx-22.3.3    1.29.3 
```

Check Kubernetes resources:

```console
kubectl get pods
kubectl get svc
```
You should see an output similar to:
```output
NAME                     READY   STATUS    RESTARTS   AGE
nginx-7b9564dc4b-2ghkw   1/1     Running   0          3m5s

NAME         TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)                      AGE
kubernetes   ClusterIP      10.96.0.1       <none>        443/TCP                      4m28s
nginx        LoadBalancer   10.96.216.137   <pending>     80:32708/TCP,443:31052/TCP   3m6s
```
All pods should be in the **Running** state. If the pods are in **Pending** state, please wait a bit and retry the commands above. 


### Validate Helm Lifecycle
This step confirms that Helm supports the full application lifecycle on Arm64.

#### Upgrade the Release

```console
helm upgrade nginx bitnami/nginx
```
Test Helm's ability to update an existing release to a new revision.

You should see an output similar (towards the top of the output...) to:
```output
Release "nginx" has been upgraded. Happy Helming!
```

#### Uninstall the Release
Ensure Helm can cleanly remove the release and associated resources.

```console
helm uninstall nginx
```

You should see an output similar to:
```output
release "nginx" uninstalled
```
This confirms the successful execution of **install**, **upgrade**, and **delete** workflows using Helm on Arm64.
Helm is fully functional on the Arm64 Kubernetes cluster and ready for further experimentation or benchmarking.
