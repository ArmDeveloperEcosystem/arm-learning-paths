---
title: Validate Persistent Storage with OpenEBS on Azure Cobalt 100
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Create and validate persistent storage

In this section, you'll create a Persistent Volume Claim (PVC), deploy a stateful NGINX application, and validate persistent storage behavior using OpenEBS LocalPV.

You'll verify that data persists even after the application pod is deleted and recreated.

## Create a Persistent Volume Claim

Create a Persistent Volume Claim (PVC) manifest:

```bash
cat > pvc.yaml <<EOF
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: openebs-pvc
spec:
  storageClassName: openebs-hostpath
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 5Gi
EOF
```

Apply the PVC:

```bash
kubectl apply -f pvc.yaml
```

Verify:

```bash
kubectl get pvc
```

The output is similar to:

```output
NAME          STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS       VOLUMEATTRIBUTESCLASS   AGE
openebs-pvc   Bound    pvc-4784909a-837e-457d-90aa-0aa6867f26de   5Gi        RWO            openebs-hostpath   <unset>                 134m
```

The PVC is dynamically provisioned by OpenEBS LocalPV.

## Deploy a stateful NGINX application

Create the deployment manifest:

```bash
cat > nginx-openebs.yaml <<EOF
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-openebs
spec:
  replicas: 1
  selector:
    matchLabels:
      app: nginx-openebs
  template:
    metadata:
      labels:
        app: nginx-openebs
    spec:
      containers:
      - name: nginx
        image: nginx
        ports:
        - containerPort: 80
        volumeMounts:
        - name: openebs-storage
          mountPath: /usr/share/nginx/html
      volumes:
      - name: openebs-storage
        persistentVolumeClaim:
          claimName: openebs-pvc
EOF
```

Deploy the application:

```bash
kubectl apply -f nginx-openebs.yaml
```

## Verify Kubernetes resources

Check the pod status:

```bash
kubectl get pods
```

The output is similar to:

```output
NAME                             READY   STATUS    RESTARTS   AGE
nginx-openebs-84d6bfddd4-6rf5v   1/1     Running   0          133m
```

Check the PVC:

```bash
kubectl get pvc
```

The output is similar to:

```output
NAME          STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS       VOLUMEATTRIBUTESCLASS   AGE
openebs-pvc   Bound    pvc-4784909a-837e-457d-90aa-0aa6867f26de   5Gi        RWO            openebs-hostpath   <unset>                 136m
```

Check the Persistent Volume (PV):

```bash
kubectl get pv
```

The output is similar to:

```output
NAME                                       CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM                 STORAGECLASS       VOLUMEATTRIBUTESCLASS   REASON   AGE
pvc-4784909a-837e-457d-90aa-0aa6867f26de   5Gi        RWO            Delete           Bound    default/openebs-pvc   openebs-hostpath   <unset>                          134m
```

The output confirms that the Persistent Volume has been dynamically created and attached.

## Write persistent data

Get the pod name:

```bash
POD=$(kubectl get pod -l app=nginx-openebs -o jsonpath='{.items[0].metadata.name}')
```

Write test data into the mounted volume:

```bash
kubectl exec -it $POD -- sh -c 'echo "OpenEBS on Azure Cobalt D4ps Arm64" > /usr/share/nginx/html/index.html'
```

Verify the data:

```bash
kubectl exec -it $POD -- cat /usr/share/nginx/html/index.html
```

The output is similar to:

```output
OpenEBS on Azure Cobalt D4ps Arm64
```

## Validate persistence after pod recreation

Delete the NGINX pod:

```bash
kubectl delete pod -l app=nginx-openebs
```

Wait for Kubernetes to recreate the pod:

```bash
kubectl get pods -w
```

Press `Ctrl + C` after the new pod reaches the Running state.

Get the new pod name:

```bash
NEW_POD=$(kubectl get pod -l app=nginx-openebs -o jsonpath='{.items[0].metadata.name}')
```

Verify the data again:

```bash
kubectl exec -it $NEW_POD -- cat /usr/share/nginx/html/index.html
```

The output is similar to:

```output
OpenEBS on Azure Cobalt D4ps Arm64
```

This confirms that the Persistent Volume retains data even after the pod is deleted and recreated.

## Expose the application

Create a NodePort service:

```bash
kubectl expose deployment nginx-openebs \
  --type NodePort \
  --port 80
```

Verify the service:

```bash
kubectl get svc
```

The output is similar to:

```output
NAME            TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)        AGE
kubernetes      ClusterIP   10.x.x.x      <none>        443/TCP        143m
nginx-openebs   NodePort    10.x.x.x  <none>        80:31635/TCP   7s
```

## Access the application

Open the following URL in your browser:

```text
http://<VM_PUBLIC_IP>:31635
```

You should see:

```output
OpenEBS on Azure Cobalt D4ps Arm64
```

![NGINX application running on Kubernetes with persistent storage provisioned by OpenEBS LocalPV on Azure Cobalt 100 Arm64.#center](images/openebs-browser.png "NGINX application using OpenEBS persistent storage")

## Cleanup resources

Delete the deployment:

```bash
kubectl delete -f nginx-openebs.yaml
```

Delete the PVC:

```bash
kubectl delete -f pvc.yaml
```

## What you've learned

You successfully created dynamically provisioned Persistent Volumes using OpenEBS LocalPV on a single-node Kubernetes cluster running on Azure Cobalt 100 Arm64.

You validated persistent storage functionality by recreating application pods while preserving data across restarts.
