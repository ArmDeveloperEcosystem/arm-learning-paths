---
title: NGINX Deployment Using Custom Helm Chart
weight: 9

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## NGINX Deployment Using Custom Helm Chart
This document explains how to deploy NGINX as a frontend service on Kubernetes using a custom Helm chart.

## Goal
After completing this guide, the environment will include:

- NGINX deployed using Helm
- Public access using a LoadBalancer service
- External IP available for browser access
- Foundation for connecting backend services (Redis, PostgreSQL)

### Create Helm Chart
Generates a Helm chart skeleton that will be customized for NGINX.

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
Defines configurable parameters such as:

- NGINX image
- Service type
- Public port

Replace the contents of `my-nginx/values.yaml` with:
```yaml
image:
  repository: nginx
  tag: latest

service:
  type: LoadBalancer
  port: 80
```

That matters

- Centralizes configuration
- Allows service exposure without editing templates
- Simplifies future changes

### Deployment Definition (deployment.yaml)
Defines how the NGINX container runs inside Kubernetes, including:

- Container image
- Pod labels
- Port exposure

Replace `my-nginx/templates/deployment.yaml` completely:

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

### Service Definition (service.yaml)
Exposes NGINX to external traffic using a Kubernetes LoadBalancer.

Replace `my-nginx/templates/service.yaml` with:

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

Why LoadBalancer:

- Provides a public IP
- Required for browser access
- Common pattern for frontend services

### Install & Access

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

### Access NGINX from Browser
Get External IP

```console
kubectl get svc
```

Wait until EXTERNAL-IP is assigned.

```output
NAME                       TYPE           CLUSTER-IP       EXTERNAL-IP     PORT(S)        AGE
kubernetes                 ClusterIP      34.118.224.1     <none>          443/TCP        3h22m
nginx-my-nginx             LoadBalancer   34.118.239.19    34.63.103.125   80:31501/TCP   52s
postgres-app-my-postgres   ClusterIP      34.118.225.2     <none>          5432/TCP       13m
redis-my-redis             ClusterIP      34.118.234.155   <none>          6379/TCP       6m53s
```

**Open in browser:**

```bash
http://<EXTERNAL-IP>    
```

You should see the default NGINX welcome page as shown below:

![NGINX default welcome page in a web browser on an GCP VM alt-text#center](images/nginx-browser.png)

### Outcome
This deployment achieves the following:

- NGINX deployed using a custom Helm chart
- Public access enabled via LoadBalancer
- External IP available for frontend access
- Ready to route traffic to backend services

