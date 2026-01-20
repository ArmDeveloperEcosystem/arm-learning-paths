---
title: Redis Deployment Using Custom Helm Chart
weight: 8

### FIXED, DO NOT MODIFY
layout: learningpathall
---


## Deploy Redis using a custom Helm chart

This section explains how to deploy Redis on Kubernetes using a custom Helm chart. After completing this section, you'll have Redis running on Kubernetes with deployment managed using Helm, internal access using a ClusterIP Service, and basic connectivity validation using redis-cli.

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

### Clean templates

The default Helm chart includes several files that aren't required for a basic Redis deployment. Remove the following files from `my-redis/templates/` to avoid unnecessary complexity and template errors: ingress.yaml, hpa.yaml, serviceaccount.yaml, tests/, and NOTES.txt.

```console
cd ./my-redis/templates
rm -rf hpa.yaml ingress.yaml serviceaccount.yaml tests/ NOTES.txt
cd $HOME/helm-microservices
```

Only Redis-specific templates will be maintained.

### Configure values.yaml

Replace the entire contents of `my-redis/values.yaml` with the following to store all configurable parameters including Redis image version, service type and port, and replica count:

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

Replace the entire contents of the existing `my-redis/templates/deployment.yaml` with the following to define how the Redis container runs inside Kubernetes, including the container image, port configuration, and pod labels and selectors.

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

Replace the entire contents of `my-redis/templates/service.yaml` with the following to create an internal Kubernetes service that allows other pods to connect to Redis:

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

ClusterIP is used because Redis is intended for internal communication only within the cluster.

### Install Redis using Helm

Install Redis and validate that it's running and responding correctly:

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

The Redis pod should be in **Running** state and the service should be **ClusterIP** type.

## What you've accomplished and what's next

You've successfully deployed Redis using a custom Helm chart with internal access via a Kubernetes Service. You've validated connectivity and created a clean, reusable Helm structure that's accessible via the service name redis.

Next, you'll deploy NGINX as a frontend service with public access to complete your microservices deployment.
