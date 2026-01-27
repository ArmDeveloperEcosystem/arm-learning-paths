---
title: Deploy Applications using GitOps with Argo CD
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

In this section, you deploy a **production-ready NGINX application** on an **Arm64-based GKE cluster** using **GitOps with Argo CD**.

All Kubernetes resources are declared in Git and continuously reconciled by Argo CD, ensuring the cluster always matches the desired state stored in the repository.

## Prerequisite

Ensure the following prerequisites are met before proceeding:

* Arm64 GKE cluster is running
* Argo CD is installed and accessible (UI and CLI)
* `kubectl` is configured for the cluster
* A GitHub repository to store GitOps manifests (an empty repo is sufficient)

## Create GitOps Repository

Create a local Git repository that acts as the **single source of truth** for application configuration.

```console
mkdir -p argocd-arm-gitops/apps/nginx
cd argocd-arm-gitops
git init
```

What this does:

* Creates a GitOps-compliant directory structure for managing Kubernetes applications
* Initializes a local Git repository that will later be pushed to GitHub
* Establishes Git as the only place where application state is defined (no manual kubectl apply)


**Repository structure:**

```text
Copy code
argocd-arm-gitops/
└── apps/
    └── nginx/
        ├── namespace.yaml
        ├── deployment.yaml
        └── service.yaml
```

## Kubernetes Manifests
Create declarative Kubernetes manifests that define the desired state of the application.

Creates an isolated production namespace (`apps/nginx/namespace.yaml`):

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: prod
```

**Deployment Manifest (apps/nginx/deployment.yaml):**

Deploys an NGINX application with two replicas for high availability.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx
  namespace: prod
spec:
  replicas: 2
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.25
        ports:
        - containerPort: 80
```

**Service Manifest (apps/nginx/service.yaml):**

Exposes NGINX publicly using a LoadBalancer service.

```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx
  namespace: prod
spec:
  type: LoadBalancer
  selector:
    app: nginx
  ports:
  - port: 80
    targetPort: 80
```

## Commit and Push
Push the application manifests to GitHub so Argo CD can continuously track and apply changes.

```console
git add .
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
git commit -m "Initial ARM GitOps app"
git branch -M main
git remote add origin https://github.com/<YOUR_GITHUB_USERNAME>/argocd-arm-gitops.git
git push -u origin main
```

* Commits define the desired cluster state
* Any future Git change automatically triggers reconciliation
* Replace <YOUR_GITHUB_USERNAME> with your own GitHub username or organization name.

## Register Application in Argo CD
Create an Argo CD Application resource to link GitHub manifests with the GKE cluster.

Create **argo-app.yaml**:

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: nginx-prod
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/<YOUR_ORG>/argocd-arm-gitops.git
    targetRevision: main
    path: apps/nginx
  destination:
    server: https://kubernetes.default.svc
    namespace: prod
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
```


**Key settings:**

* `automated` sync keeps the cluster aligned with Git
* `prune` removes deleted resources
* `selfHeal` restores manual drift
*  Ensure the repoURL points to your own GitHub repository.

**Apply the application:**

```console
kubectl apply -f argo-app.yaml
```

## Verify GitOps Deployment
Confirm that Argo CD has successfully synchronized and deployed the application.

```console
kubectl get pods -n prod
kubectl get svc -n prod
```

The output is similar to:
```output
NAME                     READY   STATUS    RESTARTS   AGE
nginx-55d67f7b54-glhj5   1/1     Running   0          5s
nginx-55d67f7b54-sdh9h   1/1     Running   0          5s

> kubectl get svc -n prod
NAME    TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE
nginx   LoadBalancer   34.118.225.71   34.30.xx.xx   80:32019/TCP   2m11s
```

## Access the Application
Validate the deployment by accessing the application through the external load balancer.

```bash
http://<NGINX_EXTERNAL_IP>
```

Expected result:

![NGINX Welcome Page confirming successful GitOps deployment via Argo CD alt-txt#center](images/argo-cd-nginx.png "NGINX Application Output")

This confirms the application is successfully deployed via GitOps.


## Argo CD Application Status (UI)

The Argo CD UI provides real-time visibility into application health, sync status, repository source, and deployment history.

![Argo CD UI showing nginx-prod application in Healthy and Synced state alt-txt#center](images/argocd-app.png "Argo CD Application Status")


Key indicators:

* **Status:** Healthy & Synced
* **Source:** GitHub repository
* **Path:** `apps/nginx`
* **Namespace:** `prod`


## Test Self-Healing
Validate Argo CD’s self-healing capability by manually changing cluster state.

```console
kubectl scale deployment nginx -n prod --replicas=1
```

Argo CD automatically restores the deployment back to 2 replicas, matching the Git-defined desired state.

## Learning Outcome

By completing this section, you have successfully implemented a production-grade GitOps workflow on ARM infrastructure.

- ARM64-based GKE cluster
- Declarative GitOps deployment
- Argo CD automated sync and pruning
- Continuous reconciliation and self-healing
- External application exposure via LoadBalancer
