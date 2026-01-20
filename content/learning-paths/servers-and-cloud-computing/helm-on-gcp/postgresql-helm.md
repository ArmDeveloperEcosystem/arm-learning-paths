---
title: PostgreSQL Deployment Using Custom Helm Chart
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---


## Deploy PostgreSQL using a custom Helm chart

This section explains how to deploy PostgreSQL on Kubernetes using a custom Helm chart with persistent storage. After completing this section, you'll have PostgreSQL running inside Kubernetes with persistent storage using PVC, secure credentials using Kubernetes Secrets, the ability to connect using psql, and a clean, reusable Helm chart.

### Prerequisites
Ensure Kubernetes and Helm are working:

```console
kubectl get nodes
helm version
```

If these commands fail, fix them first before continuing.

### Create a working directory

Create a dedicated folder to store all Helm charts for microservices:

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

The default Helm chart contains several files that aren't required for a basic PostgreSQL deployment. Remove the following files from `my-postgres/templates/` to prevent confusion and template errors: hpa.yaml, ingress.yaml, serviceaccount.yaml, tests/, NOTES.txt, and httproute.yaml.

```console
cd ./my-postgres/templates
rm -rf hpa.yaml ingress.yaml serviceaccount.yaml tests/ NOTES.txt httproute.yaml
cd $HOME/helm-microservices
```

Only PostgreSQL-specific templates will be maintained.

### Configure values.yaml

Replace the entire contents of `my-postgres/values.yaml` with the following to centralize all configurable settings including container image details, database credentials, and persistent storage configuration:

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

This configuration ensures consistent settings, avoids Helm template evaluation errors, and simplifies upgrades and maintenance.

### Create secret.yaml

Create `my-postgres/templates/secret.yaml` with the following content to store PostgreSQL credentials securely using Kubernetes Secrets:

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

This approach prevents hard-coding credentials and follows Kubernetes security best practices.

### Create pvc.yaml

Create `my-postgres/templates/pvc.yaml` with the following content to request persistent storage so PostgreSQL data remains available even if the pod restarts:

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

Without a PVC, PostgreSQL data would be lost whenever the pod restarts.

### Deployment definition (deployment.yaml)

Replace the entire contents of the existing `my-postgres/templates/deployment.yaml` file with the following to define how PostgreSQL runs inside Kubernetes, including the container image, environment variables, volume mounts, and pod configuration.

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

This configuration ensures PGDATA avoids the common lost+found directory issue, persistent storage is mounted safely, and secrets inject credentials at runtime.

### Service definition (service.yaml)

Replace the entire contents of `my-postgres/templates/service.yaml` with the following to enable internal cluster communication so other services can connect to PostgreSQL:

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

PostgreSQL should remain accessible only inside the Kubernetes cluster.

### Install PostgreSQL Using Helm

```console
cd $HOME
cd helm-microservices
helm uninstall postgres-app || true
helm install postgres-app ./my-postgres
```

The output is similar to:
```output
NAME: postgres-app
LAST DEPLOYED: Mon Jan 19 16:28:29 2026
NAMESPACE: default
STATUS: deployed
REVISION: 1
TEST SUITE: None
```

### Taint the nodes

Taint the nodes to ensure proper scheduling. First, list the nodes:

```console
kubectl get nodes
```

The output is similar to:

```output
NAME                                                STATUS   ROLES    AGE   VERSION
gke-helm-arm64-cluster-default-pool-7400f0d3-dq80   Ready    <none>   10m   v1.33.5-gke.2072000
gke-helm-arm64-cluster-default-pool-7400f0d3-v3c9   Ready    <none>   10m   v1.33.5-gke.2072000
```

For each node starting with **gke**, run the taint command. For example: 

```console
kubectl taint nodes gke-helm-arm64-cluster-default-pool-7400f0d3-dq80 kubernetes.io/arch=arm64:NoSchedule-
kubectl taint nodes gke-helm-arm64-cluster-default-pool-7400f0d3-v3c9 kubernetes.io/arch=arm64:NoSchedule-
```

Replace the node names with your actual node names from the previous command output. 

### Check the runtime status

Check the pod and PVC status:

```console
kubectl get pods
kubectl get pvc
```

Check the **STATUS** of the pod first. If it's not **Running**, wait 30 seconds and retry. 

You should see an output similar to:

```output
NAME                                        READY   STATUS    RESTARTS   AGE
postgres-app-my-postgres-6dbc8759b6-jgpxs   1/1     Running   0          40s

>kubectl get pvc
NAME                           STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   VOLUMEATTRIBUTESCLASS   AGE
postgres-app-my-postgres-pvc   Bound    pvc-5f3716df-39bb-4683-990a-c5cd3906fbce   10Gi       RWO            standard-rwo   <unset>                 33s
```

### Test PostgreSQL

Connect to PostgreSQL:

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

## What you've accomplished and what's next

You've successfully created a custom Helm chart and deployed PostgreSQL on Kubernetes with persistent storage, secure credentials using Secrets, and verified database functionality.

Next, you'll deploy Redis on your GKE cluster using another custom Helm chart for internal communication within your Kubernetes environment.
