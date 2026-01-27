---
title: Containerize and deploy Django on Axion GKE
weight: 9

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Containerize and deploy Django on Axion GKE

This guide converts your Django REST API into a production-grade Arm64 container and deploys it on Axion-powered GKE.

### Create Docker image
This step packages your Django API and all its dependencies into a portable container image that can run on any Axion Arm64 node.

Create a file called `requirements.txt` and insert the following:

```text
django
djangorestframework
psycopg2-binary
django-redis
gunicorn
```

Create a file called `Dockerfile` and insert the following:

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["gunicorn","django_api.wsgi:application","--bind","0.0.0.0:8000","--workers","3"]
```

This Dockerfile defines how to build your Django container for production deployment.

### Build and push the image

Build the image on an Arm machine and push it to Artifact Registry, ensuring Kubernetes pulls an Arm-native image.

Replace PROJECT_ID with your current project.

Build the docker image:

```bash
docker build -t us-central1-docker.pkg.dev/PROJECT_ID/django-arm/api:1.0 .
```

Push the built image:

```bash
docker push us-central1-docker.pkg.dev/PROJECT_ID/django-arm/api:1.0
```

The image is now stored in Artifact Registry and ready for deployment.

### Deploy to GKE

Kubernetes Deployments define how many containers run and where. The nodeSelector forces pods onto Axion ARM64 nodes.

First, make a directory:

```bash
mkdir ./k8s
```

Next, create `k8s/deployment.yaml` file with the following contents (replace PROJECT_ID with your current project):

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: django-api
spec:
  replicas: 2
  selector:
    matchLabels:
      app: django-api
  template:
    metadata:
      labels:
        app: django-api
    spec:
      nodeSelector:
        kubernetes.io/arch: arm64
      containers:
      - name: django
        image: us-central1-docker.pkg.dev/PROJECT_ID/django-arm/api:1.0
        ports:
        - containerPort: 8000
        env:
        - name: DJANGO_SETTINGS_MODULE
          value: django_api.settings
```

Apply the deployment:

```bash
kubectl apply -f k8s/deployment.yaml
```

Verify pods are running on Axion Arm nodes:

```bash
kubectl get pods -o wide
```

The output is similar to:
```output
NAME                          READY   STATUS    RESTARTS   AGE     IP         NODE                                                NOMINATED NODE   READINESS GATES
django-api-XXXXXX   1/1     Running   0          3h52m   10.0.2.9   gke-django-axion-cluster-axion-pool-xxxxxxx   <none>           <none>
django-api-XXXXXX   1/1     Running   0          3h52m   10.0.1.9   gke-django-axion-cluster-axion-pool-xxxxxxx   <none>           <none>
```

The Django API is running as replicated containers on Axion Arm64 nodes.

### Create a Kubernetes service (LoadBalancer)
A Service exposes your pods to the internet using **Google Cloud’s managed load balancer**.

Create `k8s/service.yaml`:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: django-api
spec:
  type: LoadBalancer
  selector:
    app: django-api
  ports:
  - port: 80
    targetPort: 8000
```

Apply the service configuration:

```bash
kubectl apply -f k8s/service.yaml
```

### Validate public access

```bash
kubectl get svc django-api
```

```output
NAME         TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)        AGE
django-api   LoadBalancer   34.118.226.245   34.45.23.92   80:31700/TCP   3h57m
```

Wait until the `EXTERNAL-IP` field is populated before proceeding.

### Validate public access

Open the following URL in browser:

```bash
http://<EXTERNAL-IP>/healthz/
```

The output is similar to:

![Screenshot showing Django health check endpoint returning a JSON response with status ok, indicating successful deployment and validation of the Django application running on GKE alt-txt#center](images/django_framework.png "Django health check validation")

The Arm-based Django API is now accessible over the internet.

## What you've accomplished and what's next

In this section, you:
- Containerized your Django REST API for Arm64
- Pushed the image to Artifact Registry
- Deployed the application to GKE running on Axion nodes
- Exposed the service through a Kubernetes LoadBalancer
- Validated public access to your Django API

Next, you'll benchmark your Django application to measure performance on Arm infrastructure.