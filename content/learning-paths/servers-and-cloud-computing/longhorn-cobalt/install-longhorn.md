---
title: Deploy Longhorn on Azure Cobalt 100 Arm64 VM
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Deploy Longhorn on Azure Cobalt 100 Arm64 VM

In this section, you'll learn how to install Longhorn on an Azure Cobalt 100 Arm64 virtual machine using a single-node Kubernetes cluster powered by K3s.

Longhorn provides Kubernetes-native distributed block storage and enables persistent storage for stateful applications running on Arm64 infrastructure.

You'll set up the Kubernetes environment, install Longhorn, access the Longhorn dashboard, and configure it for a single-node cluster.

### Update your system

Start by updating the package index and installing the latest available package updates on the virtual machine.

```bash
sudo apt update && sudo apt upgrade -y
```

### Install required dependencies

Longhorn requires iSCSI utilities for block storage attachment, along with common tools used for downloading files, checking services, and managing the environment.

```bash
sudo apt install -y \
open-iscsi \
nfs-common \
curl \
wget \
vim \
git
```

### Enable iSCSI service

Longhorn uses iSCSI to attach block volumes to Kubernetes workloads. Enable and start the iSCSI service before installing Longhorn.

```bash
sudo systemctl enable iscsid
```

```bash
sudo systemctl start iscsid
```

Verify that the service is running:

```bash
sudo systemctl status iscsid
```

The output should show that the service is active:

```output
active (running)
```

### Install K3s Kubernetes

Install K3s, a lightweight Kubernetes distribution suitable for a single-node Azure Cobalt 100 Arm64 VM.

```bash
curl -sfL https://get.k3s.io | sh -
```

### Verify Kubernetes installation

Check that the Kubernetes node is ready.

```bash
sudo kubectl get nodes
```

The output is similar to:

```output
NAME             STATUS   ROLES                  AGE   VERSION
longhorn-Arm64   Ready    control-plane,master   1m    v1.35.5+k3s1
```

### Configure kubectl access

Create the Kubernetes configuration directory for the current user.

```bash
mkdir -p ~/.kube
```

Copy the K3s kubeconfig file to your user profile.

```bash
sudo cp /etc/rancher/k3s/k3s.yaml ~/.kube/config
```

Update ownership so that kubectl can access the configuration without sudo.

```bash
sudo chown $USER:$USER ~/.kube/config
```

Set the Kubernetes configuration environment variable.

```bash
export KUBECONFIG=$HOME/.kube/config
```

Persist the configuration for future terminal sessions.

```bash
echo 'export KUBECONFIG=$HOME/.kube/config' >> ~/.bashrc
source ~/.bashrc
```

Verify kubectl access:

```bash
kubectl get nodes
```

The output is similar to:

```output
NAME             STATUS   ROLES           AGE   VERSION
longhorn-Arm64   Ready    control-plane   5s    v1.35.5+k3s1
```

### Create Longhorn storage directory

Create a local directory that Longhorn can use for storing volume replicas on the VM.

```bash
sudo mkdir -p /longhorn
```

Set permissions for the directory:

```bash
sudo chmod 777 /longhorn
```

Verify available disk space:

```bash
df -h
```

This helps confirm that enough disk space is available before creating Longhorn volumes.

### Install Longhorn

Deploy Longhorn into the Kubernetes cluster using the official Longhorn manifest.

```bash
kubectl apply -f https://raw.githubusercontent.com/longhorn/longhorn/v1.10.0/deploy/longhorn.yaml
```

### Verify Longhorn installation

Check the Longhorn pods in the `longhorn-system` namespace.

```bash
kubectl get pods -n longhorn-system
```

Wait until the pods are running. The output is similar to:

```output
NAME                                                READY   STATUS    RESTARTS   AGE
csi-attacher-65c5dd9586-dplk2                       1/1     Running   0          19s
csi-attacher-65c5dd9586-krglp                       1/1     Running   0          19s
csi-attacher-65c5dd9586-lnt7n                       1/1     Running   0          19s
csi-provisioner-c4f7f9c79-6mgtd                     1/1     Running   0          19s
csi-provisioner-c4f7f9c79-jcfnq                     1/1     Running   0          19s
csi-provisioner-c4f7f9c79-rbnlz                     1/1     Running   0          19s
csi-resizer-d4b7d97c7-d26xx                         1/1     Running   0          19s
csi-resizer-d4b7d97c7-mw44r                         1/1     Running   0          19s
csi-resizer-d4b7d97c7-nvgnf                         1/1     Running   0          19s
csi-snapshotter-5c96f555f9-7cmdb                    1/1     Running   0          19s
csi-snapshotter-5c96f555f9-l8dzk                    1/1     Running   0          19s
csi-snapshotter-5c96f555f9-wkt2g                    1/1     Running   0          19s
engine-image-ei-26bab25d-9w2r2                      1/1     Running   0          72s
instance-manager-949b7e7f84f3ef321c4078941b7dac4e   1/1     Running   0          42s
longhorn-driver-deployer-5889c569cf-88hwk           1/1     Running   0          94s
longhorn-manager-ptwb5                              2/2     Running   0          94s
longhorn-ui-77cdc466b5-8vlrl                        1/1     Running   0          94s
longhorn-ui-77cdc466b5-dbsx5                        1/1     Running   0          94s
```

### Access the Longhorn UI

Expose the Longhorn frontend service using port forwarding.

```bash
kubectl -n longhorn-system port-forward --address 0.0.0.0 service/longhorn-frontend 8080:80
```

Open the Longhorn Web UI in your browser. Replace `<PUBLIC_IP>` with the public IP address of your Azure VM.

```text
http://<PUBLIC_IP>:8080
```

![Longhorn UI Dashboard showing the cluster summary, storage schedulable capacity, volume health, and node status on the Azure Cobalt 100 Arm64 virtual machine. Verify that the Kubernetes node is schedulable, Longhorn storage is available, and the dashboard is accessible before proceeding to persistent volume configuration.#center](images/longhorn-ui.png "Longhorn UI Dashboard with storage and node summary")

In the Longhorn dashboard, you can view the number of volumes, available schedulable storage, node status, and overall storage health.

### Configure Longhorn for a single-node cluster

By default, Longhorn expects multiple nodes and uses a higher replica count. Since this learning path uses a single Azure Cobalt 100 VM, configure the replica count as `1`.

Inside the Longhorn UI, go to:

```text
Settings
```

Find the following setting:

```text
Default Replica Count
```

Update the values:

```text
V1 Data Engine: 1
V2 Data Engine: 1
```

Click:

```text
Save
```

![Longhorn Settings page showing the Default Replica Count configuration for single-node Kubernetes deployment on Azure Cobalt 100 Arm64 virtual machine. Ensure both V1 and V2 Data Engine replica counts are configured to 1 before creating Persistent Volumes in the single-node Longhorn environment.#center](images/longhorn-replica.png "Longhorn Replica Configuration for Single-Node Kubernetes Cluster")

This configuration allows Longhorn volumes to be scheduled successfully on a single-node Kubernetes cluster.

### Verify StorageClass

Check the Kubernetes storage classes created by K3s and Longhorn.

```bash
kubectl get storageclass
```

The output is similar to:

```output
NAME                   PROVISIONER             RECLAIMPOLICY   VOLUMEBINDINGMODE      ALLOWVOLUMEEXPANSION   AGE
local-path (default)   rancher.io/local-path   Delete          WaitForFirstConsumer   false                  8m48s
longhorn (default)     driver.longhorn.io      Delete          Immediate              true                   6m29s
longhorn-static        driver.longhorn.io      Delete          Immediate              true                   6m26s
```

The `longhorn` StorageClass confirms that Longhorn is available for dynamic Persistent Volume provisioning.

## What you've learned and what's next

You now have Longhorn running on an Azure Cobalt 100 Arm64 virtual machine with K3s Kubernetes. You installed the required dependencies, enabled iSCSI, deployed Longhorn, accessed the Longhorn Web UI, and configured the replica count for a single-node Kubernetes environment.

Next, you'll create Persistent Volume Claims, deploy an application using Longhorn storage, validate data persistence, and benchmark storage performance using fio.
