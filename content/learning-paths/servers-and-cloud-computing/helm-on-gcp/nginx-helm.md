---
title: Deploy NGINX with public access
weight: 9

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Create a custom NGINX Helm chart

In this section you'll deploy NGINX as a frontend service on Kubernetes using a custom Helm chart. After deployment, NGINX will have public access through a LoadBalancer service with an external IP for browser access.

### Create a Helm chart skeleton

Create a Helm chart skeleton that will be customized for NGINX:

```console
helm create my-nginx
```

### Resulting structure

```text
my-nginx/
├── Chart.yaml
├── values.yaml
└── templates/
```

### Configure values.yaml

Replace the contents of `my-nginx/values.yaml`:

```yaml
image:
  repository: nginx
  tag: latest

service:
  type: LoadBalancer
  port: 80
```

This configuration centralizes settings, allows service exposure without editing templates, and simplifies future changes.

### Deployment definition (deployment.yaml)

Replace the entire contents of `my-nginx/templates/deployment.yaml`:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ include "my-nginx.fullname" . }}

spec:
  replicas: 1
  selector:
    matchLabels:
      app: {{ include "my-nginx.name" . }}

  template:
    metadata:
      labels:
        app: {{ include "my-nginx.name" . }}

    spec:
      containers:
        - name: nginx
          image: nginx
          ports:
            - containerPort: 80
```

### Service definition (service.yaml)

Replace the entire contents of `my-nginx/templates/service.yaml` to expose NGINX to external traffic:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: {{ include "my-nginx.fullname" . }}
spec:
  type: LoadBalancer
  ports:
    - port: 80
  selector:
    app: {{ include "my-nginx.name" . }}
```

A LoadBalancer provides a public IP required for browser access and is a common pattern for frontend services.

### Install and access

```console
helm install nginx ./my-nginx
```

```output
NAME: nginx
LAST DEPLOYED: Tue Jan  6 07:55:52 2026
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
     NOTE: It may take a few minutes for the LoadBalancer IP to be available.
           You can watch its status by running 'kubectl get --namespace default svc -w nginx-my-nginx'
  export SERVICE_IP=$(kubectl get svc --namespace default nginx-my-nginx --template "{{ range (index .status.loadBalancer.ingress 0) }}{{.}}{{ end }}")
  echo http://$SERVICE_IP:80
```

### Access NGINX from a browser

Get the external IP by running the following command:

```console
kubectl get svc
```

Wait until **EXTERNAL-IP** is assigned.

```output
NAME                       TYPE           CLUSTER-IP       EXTERNAL-IP     PORT(S)        AGE
kubernetes                 ClusterIP      34.118.224.1     <none>          443/TCP        3h22m
nginx-my-nginx             LoadBalancer   34.118.239.19    34.63.103.125   80:31501/TCP   52s
postgres-app-my-postgres   ClusterIP      34.118.225.2     <none>          5432/TCP       13m
redis-my-redis             ClusterIP      34.118.234.155   <none>          6379/TCP       6m53s
```

Open the external IP in your browser:

```bash
http://<EXTERNAL-IP>
```

You should see the default NGINX welcome page:

![NGINX default welcome page displayed in a web browser showing the welcome message and basic NGINX information#center](images/nginx-browser.png "NGINX welcome page")

## What you've accomplished and what's next

You've successfully deployed NGINX as a frontend service using a custom Helm chart. The deployment includes public access through a LoadBalancer with an external IP, and the infrastructure is ready to route traffic to backend services.

This completes the helm-on-gcp Learning Path. You've learned how to install and configure Helm on Google Cloud C4A Arm-based virtual machines, create and manage GKE clusters, deploy applications using both official and custom Helm charts, and validate Helm workflows on Arm64-based Kubernetes infrastructure.

