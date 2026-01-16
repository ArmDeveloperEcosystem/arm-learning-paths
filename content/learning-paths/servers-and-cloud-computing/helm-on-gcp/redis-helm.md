---
title: Redis Deployment Using Custom Helm Chart
weight: 8

### FIXED, DO NOT MODIFY
layout: learningpathall
---


## Redis Deployment Using Custom Helm Chart
This document explains how to deploy Redis on Kubernetes using a custom Helm chart.

## Goal
After completing this guide, the environment will include:

- Redis running on Kubernetes
- Deployment managed using Helm
- Internal access using a ClusterIP Service
- Basic connectivity validation using redis-cli

### Create Helm Chart
Generates a Helm chart skeleton that will be customized for Redis.

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

### Clean Templates
The default Helm chart includes several files that are not required for a basic Redis deployment. Removing them avoids unnecessary complexity and template errors.
Inside `my-redis/templates/`, delete the following:

- ingress.yaml
- hpa.yaml
- serviceaccount.yaml
- tests/
- NOTES.txt

Only Redis-specific templates will be maintained.

### Configure values.yaml
`values.yaml` stores all configurable parameters, including:

- Redis image version
- Service type and port
- Replica count

Replace the entire contents of `my-redis/values.yaml` with:

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

That matters

- Centralizes configuration
- Simplifies future updates
- Prevents Helm template evaluation issues

### Deployment Definition (deployment.yaml)
Defines how the Redis container runs inside Kubernetes, including:

- Container image
- Port configuration
- Pod labels and selectors

Replace the existing `my-redis/templates/deployment.yaml` completely.

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

- Redis runs as a single pod
- No persistence is configured (suitable for learning and caching use cases)

### Service Definition (service.yaml)
Creates an internal Kubernetes service to allow other pods to connect to Redis.
Replace `my-redis/templates/service.yaml` with:

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

**ClusterIP**

- Redis is intended for internal communication only within the cluster.

### Install Redis Using Helm
Validates that Redis is running and responding correctly.

```console
helm install redis ./my-redis
kubectl get svc
kubectl exec -it <redis-pod> -- redis-cli ping
```

You should see an output similar to:
```output
NAME                                        READY   STATUS    RESTARTS   AGE
postgres-app-my-postgres-6dbc8759b6-jgpxs   1/1     Running   0          6m38s
redis-my-redis-75c88646fb-6lz8v             1/1     Running   0          13s

>kubectl get svc
redis-my-redis             ClusterIP      34.118.234.155   <none>        6379/TCP       6m14s

> kubectl exec -it redis-my-redis-75c88646fb-6lz8v -- redis-cli ping
PONG
```

- Redis pod → Running
- Redis service → ClusterIP

### Outcome
This deployment achieves the following:

- Redis deployed using a custom Helm chart
- Internal access via Kubernetes Service
- Successful connectivity validation
- Clean and reusable Helm structure Accessible via service name redis
