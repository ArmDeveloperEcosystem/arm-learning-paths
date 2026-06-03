---
title: Install and run Longhorn on a single-node Kubernetes cluster
description: Install K3s and Longhorn on an Azure Cobalt 100 Arm64 virtual machine, verify the Longhorn pods, access the web UI, and configure a single-node replica count.
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Set up the Kubernetes environment for Longhorn

Before you can deploy Longhorn, you need to set up a Kubernetes environment on the virtual machine (VM) that you created earlier. For steps to install kubectl, see the [kubectl install guide](/install-guides/kubectl/).

### Update your system

Start by updating the package index and installing the latest available package updates on the VM:

```bash
sudo apt update && sudo apt upgrade -y
```

### Install required dependencies

Longhorn requires iSCSI utilities for block storage attachment, along with common tools used for downloading files, checking services, and managing the environment.

Install the iSCSI utilities and required tools:

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

Longhorn uses iSCSI to attach block volumes to Kubernetes workloads. Enable the iSCSI service before installing Longhorn:

```bash
sudo systemctl enable iscsid
```
After enabling the iSCSI service, start it:

```bash
sudo systemctl start iscsid
```

Verify that the service is running:

```bash
sudo systemctl status iscsid
```

The output is similar to:

```output
Loaded: loaded (/usr/lib/systemd/system/iscsid.service; enabled; preset: enabled)
Active: active (running) 
```

### Install K3s 

K3s is a lightweight Kubernetes distribution suitable for a single-node Azure Cobalt 100 Arm64 VM.

Install K3s:

```bash
curl -sfL https://get.k3s.io | sh -
```

### Verify Kubernetes installation

Wait a few seconds for K3s to fully initialize, then check that the Kubernetes node is ready:

```bash
sudo kubectl get nodes
```

The output is similar to:

```output
NAME             STATUS   ROLES                  AGE   VERSION
longhorn-Arm64   Ready    control-plane,master   1m    v1.35.5+k3s1
```

{{% notice Note %}}
If the ROLES column shows `<none>` immediately after installation, wait 30 to 60 seconds and run the command again. Role labels are applied after the node completes initialization.
{{% /notice %}}

### Configure kubectl access

Create the Kubernetes configuration directory for the current user:

```bash
mkdir -p ~/.kube
```

Copy the K3s kubeconfig file to your user profile:

```bash
sudo cp /etc/rancher/k3s/k3s.yaml ~/.kube/config
```

Update ownership so that kubectl can access the configuration without sudo:

```bash
sudo chown $USER:$USER ~/.kube/config
```

Set the Kubernetes configuration environment variable:

```bash
export KUBECONFIG=$HOME/.kube/config
```

Persist the configuration for future terminal sessions:

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

### Check available disk space

Verify that enough disk space is available on the virtual machine before creating Longhorn volumes. Longhorn stores volume replicas in `/var/lib/longhorn` by default.

```bash
df -h
```

## Install Longhorn on Kubernetes

After setting up the Kubernetes environment, install Longhorn on the Kubernetes cluster using the official Longhorn manifest:

{{% notice Note %}}
The following command uses Longhorn version 1.10.0. The same approach works with other versions. Replace the version in the URL with your version of choice that's compatible with your K3s version. To find the latest version, see [Longhorn releases on GitHub](https://github.com/longhorn/longhorn/releases).
{{% /notice %}}

```bash
kubectl apply -f https://raw.githubusercontent.com/longhorn/longhorn/v1.10.0/deploy/longhorn.yaml
```

### Verify Longhorn installation

Longhorn deploys several components including the manager, driver, UI, and CSI controllers. These components can take several minutes to fully start. Monitor the pod rollout in the `longhorn-system` namespace:

```bash
kubectl rollout status deployment/longhorn-driver-deployer -n longhorn-system
```

After the deployment is ready, check that all Longhorn pods are running:

```bash
kubectl get pods -n longhorn-system
```

The output is similar to:

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

## Access the Longhorn UI 

After installation completes, you need to expose the Longhorn frontend service using port forwarding. Run the following command in a dedicated terminal session, as it must remain active while you use the dashboard:

```bash
kubectl -n longhorn-system port-forward --address 0.0.0.0 service/longhorn-frontend 8080:80
```

{{% notice Note %}}
The port-forward connection closes when the terminal session ends. If you lose access to the dashboard, run the command again in a new terminal.
{{% /notice %}}

Open the Longhorn web UI in your browser. Replace `<PUBLIC_IP>` with the public IP address of your Azure VM.

```text
http://<PUBLIC_IP>:8080
```

![Longhorn UI Dashboard showing the cluster summary, storage schedulable capacity, volume health, and node status on the Azure Cobalt 100 Arm64 virtual machine. Verify that the Kubernetes node is schedulable, Longhorn storage is available, and the dashboard is accessible before proceeding to persistent volume configuration.#center](images/longhorn-ui.png "Longhorn UI Dashboard with storage and node summary")

In the Longhorn dashboard, you can view the number of volumes, available schedulable storage, node status, and overall storage health.

## Configure Longhorn for a single-node cluster

By default, Longhorn expects multiple nodes and uses a higher replica count. Because you're using a single Azure Cobalt 100 VM in this Learning Path, configure the replica count to `1` so that volumes can be scheduled on a single node.

To configure the replica count, follow these steps:

1. In the Longhorn UI, select **Settings**. 
2. Find the **Default Replica Count** setting and set both **V1 Data Engine** and **V2 Data Engine** to `1`. 
3. Select **Save**.

![Longhorn Settings page showing the Default Replica Count configuration for single-node Kubernetes deployment on Azure Cobalt 100 Arm64 virtual machine. Ensure both V1 and V2 Data Engine replica counts are configured to 1 before creating Persistent Volumes in the single-node Longhorn environment.#center](images/longhorn-replica.png "Longhorn Replica Configuration for Single-Node Kubernetes Cluster")

This configuration allows Longhorn volumes to be scheduled successfully on a single-node Kubernetes cluster.

### Verify that Longhorn is available for persistent volume provisioning

Check the Kubernetes storage classes created by K3s and Longhorn:

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

The `longhorn` StorageClass confirms that Longhorn is available for dynamic persistent volume provisioning.

## What you've accomplished and what's next

You now have Longhorn installed on an Azure Cobalt 100 Arm64 virtual machine with K3s. You've installed the required dependencies, enabled iSCSI, installed Longhorn, accessed the Longhorn Web UI, and configured the replica count for a single-node Kubernetes environment.

Next, you'll create persistent volume claims, deploy an application using Longhorn storage, validate data persistence, and benchmark storage performance using fio.
