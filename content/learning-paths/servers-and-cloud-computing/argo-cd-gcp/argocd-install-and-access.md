---
title: Install and Access Argo CD on Arm64 GKE
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

In this section, you install Argo CD on an Arm64-based Google Kubernetes Engine (GKE) cluster and make it accessible through both a web browser and the Argo CD CLI.

By the end of this guide, you will have:

* Argo CD installed using official upstream manifests
* External browser access to the Argo CD UI
* Admin credentials retrieved securely
* The Argo CD CLI is installed and authenticated

## Install Argo CD
This step installs all Argo CD components into a dedicated Kubernetes namespace using the official manifests maintained by the Argo project.

**Create namespace:**

```bash
kubectl create namespace argocd
```

**What this does:**

* Creates an isolated Kubernetes namespace named `argocd`
* Keeps Argo CD components logically separated from application workloads
* Aligns with production-recommended deployment patterns
**Install Argo CD using official manifests:**

```console
kubectl apply -n argocd \
  -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```
**What this does:**

* Downloads the latest *stable* Argo CD installation manifest
* Deploys all required Argo CD components into the `argocd` namespace
* Creates Deployments, StatefulSets, Services, ConfigMaps, Secrets, and RBAC objects

**Key components installed:**

* `argocd-server` – Web UI and API server
* `argocd-repo-server` – Handles Git repository interactions
* `argocd-application-controller` – Continuously reconciles desired vs live state
* `argocd-dex-server` – Identity and authentication service
* `argocd-redis` – Internal cache and state store

All images used support **linux/arm64**, making them compatible with Arm-based GKE nodes.

### Wait for Argo CD Pods to Become Ready

```console
kubectl get pods -n argocd -w
```

**What this does:**

* Lists all pods in the `argocd` namespace
* `-w` (watch) continuously updates output as pod states change
* Allows you to confirm when all components reach `Running` state

The output is similar to:
```output
NAME                                               READY   STATUS    RESTARTS   AGE
argocd-application-controller-0                    1/1     Running   0          3h20m
argocd-applicationset-controller-944684d77-p8vcv   1/1     Running   0          3h20m
argocd-dex-server-6944b95798-hzp2j                 1/1     Running   0          3h20m
argocd-notifications-controller-7f5b87f55b-8v4zh   1/1     Running   0          3h20m
argocd-redis-c98d5794d-ckczm                       1/1     Running   0          3h20m
argocd-repo-server-7f86545bc4-gcqcv                1/1     Running   0          3h20m
argocd-server-685f5fb66f-24w8m                     1/1     Running   0          3h20m
```

Once all pods are running, Argo CD is successfully installed.

## Expose Argo CD (External Browser Access)
By default, Argo CD is only accessible inside the cluster. This step exposes the Argo CD server externally using a Kubernetes **LoadBalancer** service, which is suitable for cloud environments like GKE.

### Patch the Argo CD Server Service

```console
kubectl patch svc argocd-server -n argocd \
  -p '{"spec": {"type": "LoadBalancer"}}'
```

**What this does:**

* Modifies the existing `argocd-server` Service
* Changes the Service type from `ClusterIP` to `LoadBalancer`
* Instructs GKE to provision a cloud load balancer with a public IP

### Retrieve the External IP Address

```console
kubectl get svc argocd-server -n argocd -w
```

* Displays service details for `argocd-server`
* Waits until GKE assigns an external IP address

The output is similar to:
```output
NAME            TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)                      AGE
argocd-server   LoadBalancer   34.118.228.71   34.xx.xx.xx   80:30166/TCP,443:30920/TCP   3h22m
```
The value under `EXTERNAL-IP` will be used to access the UI and CLI.

## Get Admin Password
Argo CD generates an initial admin password and stores it securely as a Kubernetes Secret.

```console
kubectl -n argocd get secret argocd-initial-admin-secret \
  -o jsonpath="{.data.password}" | base64 -d && echo
```
**What this does:**

* Fetches the `argocd-initial-admin-secret` Secret
* Extracts the base64-encoded password field
* Decodes it into human-readable form

Save this password — it is required for both UI and CLI login.

## Access Argo CD UI
Access the Argo CD web UI using the external IP to manage and monitor GitOps applications.

Open your browser and navigate to:

```bash
https://<ARGOCD_EXTERNAL_IP>
```

**Login:**

- Username: admin
- Password: from the previous step

You will see a TLS warning because Argo CD uses a self-signed certificate by default. This is expected for lab and learning environments.

![Argo CD web UI alt-txt#center](images/argo-cd.png "Argo CD UI")

## Install Argo CD CLI (Arm64)
The Argo CD CLI allows you to manage applications, sync states, and automate GitOps workflows from the terminal.

```console
curl -LO https://github.com/argoproj/argo-cd/releases/latest/download/argocd-linux-arm64
chmod +x argocd-linux-arm64
sudo mv argocd-linux-arm64 /usr/local/bin/argocd
```

**What this does:**

* Downloads the latest Argo CD CLI binary for `linux/arm64`
* Makes the binary executable
* Moves it into `/usr/local/bin` so it is available system-wide
  
### Verify CLI Installation

```console
argocd version
```

The output is similar to:
```output
argocd: v3.2.5+c56f440
  BuildDate: 2026-01-14T16:38:17Z
  GitCommit: c56f4400f22c7e9fe9c5c12b85576b74369fb6b8
  GitTreeState: clean
  GoVersion: go1.25.5
  Compiler: gc
  Platform: linux/arm64
argocd-server: v3.2.5+c56f440
  BuildDate: 2026-01-14T16:13:04Z
  GitCommit: c56f4400f22c7e9fe9c5c12b85576b74369fb6b8
  GitTreeState: clean
  GoVersion: go1.25.5
  Compiler: gc
  Platform: linux/arm64
  Kustomize Version: v5.7.0 2025-06-28T07:00:07Z
  Helm Version: v3.18.4+gd80839c
  Kubectl Version: v0.34.0
  Jsonnet Version: v0.21.0
```
This confirms version compatibility between the CLI and server.

## Login via CLI
Authenticate the CLI with the Argo CD server using the external IP.

```console
argocd login <ARGOCD_EXTERNAL_IP> \
  --username admin \
  --password <PASTE_PASSWORD> \
  --insecure
```
**What this does:**

* Connects the CLI to the Argo CD API server
* Authenticates using admin credentials
* `--insecure` bypasses TLS verification for the self-signed certificate

The output is similar to:
```output
'admin:login' logged in successfully
Context '35.232.56.107' updated
```

### Verify CLI Connectivity

```console
argocd app list
```

**What this does:**

* Queries Argo CD for registered applications
* Confirms CLI authentication and API connectivity

**Expected output (no apps yet):**


The output is similar to:
```output
NAME  CLUSTER  NAMESPACE  PROJECT  STATUS  HEALTH  SYNCPOLICY  CONDITIONS  REPO  PATH  TARGET
```

## What You’ve Accomplished

You have successfully:

* Installed Argo CD on an Arm64 GKE cluster
* Exposed the Argo CD server securely via a LoadBalancer
* Accessed the Argo CD web UI
* Installed and authenticated the Argo CD CLI

Your environment is now fully prepared for GitOps-based application deployment and continuous delivery using Argo CD.
