---
title: Deploy OpenEBS on an Arm-based virtual machine 
description: Install K3s, deploy OpenEBS LocalPV with Helm, and configure OpenEBS as the default storage class on an Arm64 virtual machine.
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Set up OpenEBS on the virtual machine

In this section, you'll install OpenEBS LocalPV using a lightweight single-node Kubernetes cluster on the virtual machine (VM) that you created in the previous section.

You'll configure Kubernetes storage provisioning and prepare the environment for persistent workloads. 

### Update your system

Start by updating the package index and installing the latest package updates on the virtual machine.

```bash
sudo apt update && sudo apt upgrade -y
```

### Install required dependencies

Install the tools required for Kubernetes and Helm setup.

```bash
sudo apt install -y curl wget git apt-transport-https
```

### Install Kubernetes using K3s

K3s is a lightweight Kubernetes distribution optimized for edge systems, Arm64 environments, and single-node deployments.

Run the following command to install K3s:

```bash
curl -sfL https://get.k3s.io | sh -
```

Verify the installation:

```bash
sudo kubectl get nodes
```

The output is similar to:

```output
NAME            STATUS   ROLES           AGE   VERSION
openebs-arm64   Ready    control-plane   7s    v1.35.5+k3s1
```

### Configure kubectl access

Create the Kubernetes configuration directory:

```bash
mkdir -p ~/.kube
```

Copy the K3s kubeconfig file:

```bash
sudo cp /etc/rancher/k3s/k3s.yaml ~/.kube/config
```

Update ownership permissions:

```bash
sudo chown $USER:$USER ~/.kube/config
```

Set the Kubernetes configuration environment variable:

```bash
export KUBECONFIG=$HOME/.kube/config
```

Persist the configuration:

```bash
echo 'export KUBECONFIG=$HOME/.kube/config' >> ~/.bashrc
source ~/.bashrc
```

Verify access:

```bash
kubectl get nodes
```

The output is similar to:

```output
NAME            STATUS   ROLES           AGE   VERSION
openebs-arm64   Ready    control-plane   62s   v1.35.5+k3s1
```

### Install Helm

Helm is the Kubernetes package manager used to deploy OpenEBS.

Install Helm:

```bash
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
```

Verify that Helm installed successfully:

```bash
helm version
```

The output is similar to:

```output
version.BuildInfo{Version:"v3.21.0", GitCommit:"e0878d41b711792be60777fd65ad23a101e6b85f", GitTreeState:"clean", GoVersion:"go1.25.10"}
```
### Add the OpenEBS repository

Add the official OpenEBS Helm repository:

```bash
helm repo add openebs https://openebs.github.io/openebs
```

### Update Helm repositories

After adding the OpenEBS repository, update Helm repositories:

```bash
helm repo update
```

The output is similar to:

```output
...Successfully got an update from the "openebs" chart repository
Update Complete. ⎈Happy Helming!⎈
```

### Install lightweight OpenEBS

Create the `openebs` namespace that will hold all OpenEBS components.

```bash
kubectl create namespace openebs
```

Install OpenEBS LocalPV components and disable Mayastor, Loki, Alloy, and observability services, which are unnecessary for a single-node setup:

{{% notice Note %}}
The following command installs the latest available OpenEBS chart. To pin to a specific version, add `--version <version>` to the command. To find available versions, run `helm search repo openebs/openebs --versions`.
{{% /notice %}}

```bash
helm install openebs openebs/openebs \
  --namespace openebs \
  --set engines.replicated.mayastor.enabled=false \
  --set loki.enabled=false \
  --set alloy.enabled=false \
  --set obs.enabled=false
```

## Verify OpenEBS installation

OpenEBS components take a moment to start. Wait for the pods to become ready before continuing:

```bash
kubectl wait --for=condition=Ready pod -l app=openebs-localpv-provisioner -n openebs --timeout=120s
```

Then check whether all OpenEBS pods are running:

```bash
kubectl get pods -n openebs
```

The output is similar to:

```output
NAME                                              READY   STATUS    RESTARTS   AGE
openebs-localpv-provisioner-6f9447fcc9-nnbgm      1/1     Running   0          17s
openebs-lvm-localpv-controller-5996c4fbfc-d8274   5/5     Running   0          17s
openebs-lvm-localpv-node-9g49t                    2/2     Running   0          17s
openebs-zfs-localpv-controller-6b98b6cc9d-rjq76   5/5     Running   0          17s
openebs-zfs-localpv-node-p28g2                    2/2     Running   0          17s
```

### Verify storage classes

Check the available Kubernetes storage classes:

```bash
kubectl get sc
```

The output is similar to:

```output
NAME                   PROVISIONER             RECLAIMPOLICY   VOLUMEBINDINGMODE      ALLOWVOLUMEEXPANSION   AGE
local-path (default)   rancher.io/local-path   Delete          WaitForFirstConsumer   false                  2m16s
openebs-hostpath       openebs.io/local        Delete          WaitForFirstConsumer   false                  32s
```

## Configure OpenEBS as the default storage class

Remove the default flag from the K3s local-path storage class:

```bash
kubectl patch storageclass local-path \
  -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"false"}}}'
```

Set OpenEBS HostPath as the default storage class:

```bash
kubectl patch storageclass openebs-hostpath \
  -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"true"}}}'
```

Verify that the configuration commands worked:

```bash
kubectl get sc
```

The output is similar to:

```output
NAME                         PROVISIONER             RECLAIMPOLICY   VOLUMEBINDINGMODE      ALLOWVOLUMEEXPANSION   AGE
local-path                   rancher.io/local-path   Delete          WaitForFirstConsumer   false                  2m55s
openebs-hostpath (default)   openebs.io/local        Delete          WaitForFirstConsumer   false                  71s
```

Check all OpenEBS resources:

```bash
kubectl get all -n openebs
```

At this stage, OpenEBS LocalPV is successfully configured and ready to provision persistent storage volumes for Kubernetes workloads.

## What you've accomplished and what's next

You've now created a lightweight single-node Kubernetes cluster running on an Arm64 virtual machine powered by Azure Cobalt 100. You've configured OpenEBS LocalPV as the default storage class.

Next, you'll create a PersistentVolumeClaim (PVC), deploy a stateful NGINX application, and validate data persistence.
