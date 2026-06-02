---
title: Validate Persistent Storage and Benchmark Longhorn
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Validate Persistent Storage and Benchmark Longhorn

In this section, you'll create Kubernetes Persistent Volumes using Longhorn, deploy workloads, validate persistent storage functionality, and benchmark storage performance using fio.

You'll create a Persistent Volume Claim (PVC), attach it to a Kubernetes workload, verify that data survives pod recreation, and run storage benchmarking tests on the Longhorn-backed volume.

### Create Persistent Volume Claim

Create a Kubernetes Persistent Volume Claim (PVC) using the Longhorn StorageClass.

```bash
cat > pvc.yaml <<EOF
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: longhorn-pvc
spec:
  accessModes:
    - ReadWriteOnce
  storageClassName: longhorn
  resources:
    requests:
      storage: 5Gi
EOF
```

Apply the PVC configuration:

```bash
kubectl apply -f pvc.yaml
```

The PVC requests a 5 GB Longhorn-backed volume that can be mounted by a single Kubernetes node in read-write mode.

### Verify Persistent Volume Claim

Check that the PVC is successfully provisioned.

```bash
kubectl get pvc
```

The output is similar to:

```output
NAME           STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   VOLUMEATTRIBUTESCLASS   AGE
longhorn-pvc   Bound    pvc-14ab1c22-be1c-4706-b9bc-f5b228007814   5Gi        RWO            longhorn       <unset>                 7s
```

The `Bound` status confirms that Longhorn successfully created and attached the Persistent Volume.

### Deploy test application

Create an NGINX pod that mounts the Longhorn-backed Persistent Volume Claim.

```bash
cat > nginx-longhorn.yaml <<EOF
apiVersion: v1
kind: Pod
metadata:
  name: nginx-longhorn
spec:
  containers:
  - name: nginx
    image: nginx
    volumeMounts:
    - mountPath: "/usr/share/nginx/html"
      name: longhorn-storage
  volumes:
  - name: longhorn-storage
    persistentVolumeClaim:
      claimName: longhorn-pvc
EOF
```

Deploy the pod:

```bash
kubectl apply -f nginx-longhorn.yaml
```

This mounts the Longhorn volume inside the NGINX container and allows Kubernetes workloads to store persistent application data.

### Verify application pod

Check that the NGINX pod is running successfully.

```bash
kubectl get pods
```

The output is similar to:

```output
NAME             READY   STATUS    RESTARTS   AGE
nginx-longhorn   1/1     Running   0          31s
```

### Write data to the Persistent Volume

Open a shell inside the running NGINX container.

```bash
kubectl exec -it nginx-longhorn -- bash
```

Write sample data to the mounted Longhorn volume.

```bash
echo "Longhorn Storage Working on Arm64" > /usr/share/nginx/html/index.html
```

Exit the container:

```bash
exit
```

This creates a file directly on the Longhorn-backed Persistent Volume.

### Validate persistent storage

Delete the running pod.

```bash
kubectl delete pod nginx-longhorn
```

Recreate the pod:

```bash
kubectl apply -f nginx-longhorn.yaml
```

Verify that the data still exists after the pod recreation.

```bash
kubectl exec -it nginx-longhorn -- cat /usr/share/nginx/html/index.html
```

The output is similar to:

```output
Longhorn Storage Working on Arm64
```

This confirms that the data persists independently of the Kubernetes pod lifecycle.

### Create fio benchmark pod

Create a benchmarking pod that mounts the Longhorn volume and installs fio for storage testing.

```bash
cat > fio-pod.yaml <<EOF
apiVersion: v1
kind: Pod
metadata:
  name: fio-test
spec:
  containers:
  - name: fio
    image: ubuntu
    command: ["/bin/bash", "-c"]
    args:
      - apt update && apt install -y fio && sleep infinity
    volumeMounts:
    - mountPath: /data
      name: longhorn-storage
  volumes:
  - name: longhorn-storage
    persistentVolumeClaim:
      claimName: longhorn-pvc
EOF
```

Deploy the benchmarking pod:

```bash
kubectl apply -f fio-pod.yaml
```

Wait until the pod becomes ready:

```bash
kubectl wait --for=condition=Ready pod/fio-test --timeout=300s
```

The fio pod will install the benchmarking utility and keep the container running for interactive testing.

### Open fio container shell

Open a shell inside the fio container.

```bash
kubectl exec -it fio-test -- bash
```

Verify that fio is installed correctly.

```bash
which fio
```

If fio is not installed, install it manually:

```bash
apt update
apt install -y fio
```

### Run fio storage benchmark

Run a random write workload against the Longhorn-backed Persistent Volume.

```bash
fio --name=benchmark \
--directory=/data \
--rw=randwrite \
--bs=4k \
--size=1G \
--numjobs=2 \
--time_based \
--runtime=60 \
--group_reporting
```

This benchmark performs random write operations with 4 KB block sizes for 60 seconds and measures storage throughput, latency, and IOPS.

The output is similar to:

```output
benchmark: Laying out IO file (1 file / 1024MiB)
benchmark: Laying out IO file (1 file / 1024MiB)
Jobs: 2 (f=2): [w(2)][100.0%][eta 00m:00s]
benchmark: (groupid=0, jobs=2): err= 0: pid=3344: Tue May 26 04:06:33 2026
  write: IOPS=40.5k, BW=158MiB/s (166MB/s)(10.0GiB/64649msec)
```

The benchmark validates storage performance and confirms that Longhorn volumes are functioning correctly on the Azure Cobalt 100 Arm64 virtual machine.

You should observe:

- PVC successfully provisioned
- Longhorn storage mounted correctly
- Data persists after pod recreation
- fio benchmark completes successfully
- Stable storage performance on Arm64 Kubernetes

## What you've learned

You now have a working Longhorn-backed Persistent Volume running on Kubernetes with validated storage persistence and benchmarking results.

You created a Persistent Volume Claim, mounted it into a Kubernetes workload, verified data persistence across pod recreation, and benchmarked the storage layer using fio.
