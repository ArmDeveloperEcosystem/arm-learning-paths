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

You should see an output similar to:
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
NAME            NAMESPACE       REVISION        UPDATED                                 STATUS          CHART           APP VERSION
nginx           default         1               2025-12-03 08:02:21.533232677 +0000 UTC deployed        nginx-22.3.3    1.29.3
nginx-1         default         1               2025-12-03 05:20:12.871824822 +0000 UTC deployed          nginx-22.3.3    1.29.3
nginx-2         default         1               2025-12-03 05:20:12.844759384 +0000 UTC deployed          nginx-22.3.3    1.29.3
nginx-3         default         1               2025-12-03 05:20:13.154627899 +0000 UTC deployed          nginx-22.3.3    1.29.3
nginx-4         default         1               2025-12-03 05:20:12.874546176 +0000 UTC deployed          nginx-22.3.3    1.29.3
nginx-5         default         1               2025-12-03 05:20:12.875725062 +0000 UTC deployed          nginx-22.3.3    1.29.3
nginx-bench     default         1               2025-12-02 08:45:50.190893813 +0000 UTC deployed          nginx-22.3.3    1.29.3
```

Check Kubernetes resources:

```console
kubectl get pods
kubectl get svc
```
You should see an output similar to:
```output
NAME                          READY   STATUS    RESTARTS        AGE
nginx-1-c89c47fc6-vqww4       1/1     Running   0               163m
nginx-2-54f57f5bb9-wf4r7      1/1     Running   0               163m
nginx-3-bfd4cf4f8-q57qq       1/1     Running   0               163m
nginx-4-6c5d9989c5-ld9mk      1/1     Running   0               163m
nginx-5-74b7ccf97b-cfgr7      1/1     Running   0               163m
nginx-7b9564dc4b-92rnd        1/1     Running   0               75s
nginx-bench-c4f66c79c-bhlgl   1/1     Running   1 (3h37m ago)   23h
```
All pods should be in the **Running** state.


### Validate Helm Lifecycle
This step confirms that Helm supports the full application lifecycle on Arm64.

#### Upgrade the Release

```console
helm upgrade nginx bitnami/nginx
```
Test Helm's ability to update an existing release to a new revision.

You should see an output similar to:
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
