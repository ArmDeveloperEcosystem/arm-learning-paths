---
title: Deploy Redis on GKE
weight: 8

### FIXED, DO NOT MODIFY
layout: learningpathall
---


## Deploy Redis using a custom Helm chart

In this section you'll deploy Redis on Kubernetes using a custom Helm chart. After deployment, Redis will be running with internal access using a ClusterIP Service and basic connectivity validated using redis-cli.

### Create a Helm chart

Create a Helm chart skeleton:

```console
helm create my-redis
```

### Resulting structure

```text
my-redis/
├── Chart.yaml
├── values.yaml
└── templates/
```

### Clean templates

Remove unnecessary default files from `my-redis/templates/`:

```console
cd ./my-redis/templates
rm -rf hpa.yaml ingress.yaml serviceaccount.yaml tests/ NOTES.txt
cd $HOME/helm-microservices
```

Only Redis-specific templates will be maintained.

### Configure values.yaml

Replace the entire contents of `my-redis/values.yaml`:

```yaml
replicaCount: 1

image:
  repository: redis
  tag: "7"
  pullPolicy: IfNotPresent

service:
  type: ClusterIP
  port: 6379
```

This configuration centralizes settings, simplifies future updates, and prevents Helm template evaluation issues.

### Deployment definition (deployment.yaml)

Replace the entire contents of `my-redis/templates/deployment.yaml`:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ include "my-redis.fullname" . }}

spec:
  replicas: 1
  selector:
    matchLabels:
      app: {{ include "my-redis.name" . }}

  template:
    metadata:
      labels:
        app: {{ include "my-redis.name" . }}

    spec:
      containers:
        - name: redis
          image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
          ports:
            - containerPort: 6379
```

Redis runs as a single pod with no persistence configured, which is suitable for learning and caching use cases.

### Service definition (service.yaml)

Replace the entire contents of `my-redis/templates/service.yaml` to create an internal service:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: {{ include "my-redis.fullname" . }}
spec:
  type: ClusterIP
  ports:
    - port: 6379
  selector:
    app: {{ include "my-redis.name" . }}
```

### Install Redis using Helm

Install Redis and validate that it's running:

```console
helm install redis ./my-redis
kubectl get pods
kubectl get svc
```

Get the Redis pod name from the output, then test connectivity:

```console
kubectl exec -it <redis-pod-name> -- redis-cli ping
```

Replace `<redis-pod-name>` with the actual pod name (for example, `redis-my-redis-75c88646fb-6lz8v`).

You should see an output similar to:
```output
NAME                                        READY   STATUS    RESTARTS   AGE
postgres-app-my-postgres-6dbc8759b6-jgpxs   1/1     Running   0          6m38s
redis-my-redis-75c88646fb-6lz8v             1/1     Running   0          13s

NAME                       TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
redis-my-redis             ClusterIP   34.118.234.155   <none>        6379/TCP   6m14s

> kubectl exec -it redis-my-redis-75c88646fb-6lz8v -- redis-cli ping
PONG
```

The Redis pod should be in **Running** state and the service should be **ClusterIP** type.

## What you've accomplished and what's next

You've successfully deployed Redis using a custom Helm chart with internal access via a Kubernetes Service. You've validated connectivity and created a clean, reusable Helm structure that's accessible via the service name redis.

Next, you'll deploy NGINX as a frontend service with public access to complete your microservices deployment.
