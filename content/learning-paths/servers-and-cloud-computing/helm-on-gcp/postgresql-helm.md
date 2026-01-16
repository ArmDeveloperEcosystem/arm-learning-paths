---
title: PostgreSQL Deployment Using Custom Helm Chart
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---


## PostgreSQL Deployment Using Custom Helm Chart
This document explains how to deploy **PostgreSQL** on Kubernetes using a **custom Helm chart** with persistent storage.

### Goal
After completing this guide, the environment will include:
- PostgreSQL running inside Kubernetes
- Persistent storage using PVC
- Secure credentials using Kubernetes Secrets
- Ability to connect using psql
- A clean, reusable Helm chart

### Prerequisites
Ensure Kubernetes and Helm are working:

```console
kubectl get nodes
helm version
```

If these commands fail, fix them first before continuing.

### CREATE WORKING DIRECTORY
Creates a dedicated folder to store all Helm charts for microservices.

```console
mkdir helm-microservices
cd helm-microservices
```

### Create Helm Chart
Generates a Helm chart skeleton that will be customized for PostgreSQL.

```console
helm create my-postgres
```

**Directory structure:**

```text
helm-microservices/
└── my-postgres/
    ├── Chart.yaml
    ├── values.yaml
    └── templates/
```

### Clean the chart
The default Helm chart contains several files that are not required for a basic PostgreSQL deployment. Removing these files prevents confusion and template errors.
Inside `my-postgres/templates/`, delete the following:

- hpa.yaml
- ingress.yaml
- serviceaccount.yaml
- tests/
- NOTES.txt
- httproute.yaml

Only PostgreSQL-specific templates will be maintained.

### Configure values.yaml (Main Configuration File)
`values.yaml` centralizes all configurable settings, including:

- Container image details
- Database credentials
- Persistent storage configuration

Replace the entire contents of `my-postgres/values.yaml` with the following:

```yaml
replicaCount: 1

image:
  repository: postgres
  tag: "15"
  pullPolicy: IfNotPresent

postgresql:
  username: admin
  password: admin123
  database: mydb

persistence:
  enabled: true
  size: 10Gi
  mountPath: /var/lib/postgresql
  dataSubPath: data
```

This matters

- Ensures consistent configuration
- Avoids Helm template evaluation errors
- Simplifies upgrades and maintenance

### Create secret.yaml (Database Credentials)
Stores PostgreSQL credentials securely using Kubernetes Secrets.
Create the following file:

`my-postgres/templates/secret.yaml`

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: {{ include "my-postgres.fullname" . }}
type: Opaque
stringData:
  POSTGRES_USER: {{ .Values.postgresql.username }}
  POSTGRES_PASSWORD: {{ .Values.postgresql.password }}
  POSTGRES_DB: {{ .Values.postgresql.database }}
```

That matters

- Prevents hard-coding credentials
- Follows Kubernetes security best practices

### Create pvc.yaml (Persistent Storage)
Requests persistent storage so PostgreSQL data remains available even if the pod restarts.
Create the following file:

`my-postgres/templates/pvc.yaml`

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: {{ include "my-postgres.fullname" . }}-pvc
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: {{ .Values.persistence.size }}
```

That matters
- Without a PVC, PostgreSQL data would be lost whenever the pod restarts.

### deployment.yaml (PostgreSQL Pod Definition)
Defines how PostgreSQL runs inside Kubernetes, including:
- Container image
- Environment variables
- Volume mounts
- Pod configuration

Replace the existing `my-postgres/templates/deployment.yaml` file completely.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ include "my-postgres.fullname" . }}

spec:
  replicas: 1
  selector:
    matchLabels:
      app: {{ include "my-postgres.name" . }}

  template:
    metadata:
      labels:
        app: {{ include "my-postgres.name" . }}

    spec:
      containers:
        - name: postgres
          image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
          imagePullPolicy: {{ .Values.image.pullPolicy }}

          ports:
            - containerPort: 5432

          envFrom:
            - secretRef:
                name: {{ include "my-postgres.fullname" . }}

          env:
            - name: PGDATA
              value: "{{ .Values.persistence.mountPath }}/{{ .Values.persistence.dataSubPath }}"

          volumeMounts:
            - name: postgres-data
              mountPath: {{ .Values.persistence.mountPath }}

      volumes:
        - name: postgres-data
          persistentVolumeClaim:
            claimName: {{ include "my-postgres.fullname" . }}-pvc
```

- PGDATA avoids the common lost+found directory issue
- Persistent storage is mounted safely
- Secrets inject credentials at runtime

### service.yaml (Internal Access)
Enables internal cluster communication so other services can connect to PostgreSQL.
Replace `my-postgres/templates/service.yaml` with:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: {{ include "my-postgres.fullname" . }}
spec:
  type: ClusterIP
  ports:
    - port: 5432
      targetPort: 5432
  selector:
    app: {{ include "my-postgres.name" . }}
```

**ClusterIP**
- PostgreSQL should remain accessible only inside the Kubernetes cluster.

### Install PostgreSQL Using Helm

```console
cd helm-microservices
helm uninstall postgres || true
helm install postgres-app ./my-postgres
```

**Check:**

```console
kubectl get pods
kubectl get pvc
```

You should see an output similar to:
```output
NAME                                        READY   STATUS    RESTARTS   AGE
postgres-app-my-postgres-6dbc8759b6-jgpxs   1/1     Running   0          40s

>kubectl get pvc
NAME                           STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   VOLUMEATTRIBUTESCLASS   AGE
postgres-app-my-postgres-pvc   Bound    pvc-5f3716df-39bb-4683-990a-c5cd3906fbce   10Gi       RWO            standard-rwo   <unset>                 33s
```

### Test PostgreSQL
Connect to PostgreSQL

```console
kubectl exec -it <postgres-pod> -- psql -U admin -d mydb
```

You should see an output similar to:
```output
psql (15.15 (Debian 15.15-1.pgdg13+1))
Type "help" for help.

mydb=#
```

**Run test queries:**

```psql
CREATE TABLE test (id INT);
INSERT INTO test VALUES (1);
SELECT * FROM test;
```

You should see an output similar to:
```output
mydb=# CREATE TABLE test (id INT);
INSERT INTO test VALUES (1);
SELECT * FROM test;
CREATE TABLE
INSERT 0 1
 id
----
  1
(1 row)
```

### Outcome
You have successfully:

- Created a custom Helm chart
- Deployed PostgreSQL on Kubernetes
- Enabled persistent storage
- Used Secrets for credentials
- Verified database functionality

