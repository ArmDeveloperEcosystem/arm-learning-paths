---
title: Install Gardener
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install Gardener and dependencies

This section guides you through setting up Gardener Local on a Google Cloud Arm64 (C4A) VM running SUSE Linux Enterprise Server. You'll install system dependencies, CLI tools, and Gardener components to create a fully functional local Kubernetes cluster management system.

### Update your system

Update your operating system packages to the latest versions:

```console
sudo zypper refresh
sudo zypper update -y
```

### Enable the SUSE Containers Module

Enable SUSE's official container support module for Docker and container tools:

```console
sudo SUSEConnect -p sle-module-containers/15.5/arm64
sudo SUSEConnect --list-extensions | grep Containers
```

The output shows "Activated" for the Containers module, confirming successful enablement.

### Install Docker

Install Docker to run Kubernetes in Docker (KinD) and Kubernetes components as containers:

```console
sudo zypper refresh
sudo zypper install -y docker
sudo systemctl enable --now docker
sudo usermod -aG docker $USER
exit
```

Open a new SSH session to apply the Docker group membership, then verify Docker is running:

```console
docker ps
```

The output is similar to:

```output
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```

An empty container list confirms Docker is installed and running correctly.

### Install Go 1.24

Gardener requires Go 1.24, which isn't available in the default SUSE repositories. Download and install the Arm64-compatible Go binary:

```console
cd /tmp
curl -LO https://go.dev/dl/go1.24.0.linux-arm64.tar.gz
sudo rm -rf /usr/local/go
sudo tar -C /usr/local -xzf go1.24.0.linux-arm64.tar.gz
echo 'export PATH=$PATH:/usr/local/go/bin' >> ~/.consolerc
source ~/.consolerc
go version
```

The output is similar to:

```output
go version go1.24.0 linux/arm64
```

### Install build tools

Install Git and build tools needed to download and compile Gardener components:

```console
sudo zypper install -y git curl tar gzip make gcc
```

### Install kubectl

Install kubectl, the command-line tool for interacting with Kubernetes clusters:

```console
curl -LO https://dl.k8s.io/release/v1.34.0/bin/linux/arm64/kubectl
chmod +x kubectl
sudo mv kubectl /usr/local/bin/
kubectl version --client
```

The output is similar to:

```output
Client Version: v1.34.0
Kustomize Version: v5.7.1
```

### Install Helm

Install Helm to manage Kubernetes applications. Gardener uses Helm internally to deploy components:

```console
curl -sSfL https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 > get_helm.sh
chmod 755 ./get_helm.sh
./get_helm.sh
helm version
```

The output is similar to:

```output
version.BuildInfo{Version:"v3.19.2", GitCommit:"8766e718a0119851f10ddbe4577593a45fadf544", GitTreeState:"clean", GoVersion:"go1.24.9"}
```

### Install yq

Install yq, a YAML processing tool used by Gardener scripts to modify configuration files:

```console
sudo curl -L -o /usr/local/bin/yq https://github.com/mikefarah/yq/releases/download/v4.43.1/yq_linux_arm64
sudo chmod +x /usr/local/bin/yq
yq --version
```

The output is similar to:

```output
yq (https://github.com/mikefarah/yq/) version v4.43.1
```

### Install Kustomize

Install Kustomize to customize Kubernetes YAML files without modifying the originals:

```console
curl -LO https://github.com/kubernetes-sigs/kustomize/releases/download/kustomize/v5.3.0/kustomize_v5.3.0_linux_arm64.tar.gz
tar -xvf kustomize_v5.3.0_linux_arm64.tar.gz
sudo mv kustomize /usr/local/bin/
kustomize version
```

The output is similar to:

```output
v5.3.0
```

### Install Kind

Install Kind (Kubernetes in Docker) to create a local Kubernetes cluster inside Docker containers:

```console
curl -Lo kind https://kind.sigs.k8s.io/dl/v0.30.0/kind-linux-arm64
chmod +x kind
sudo mv kind /usr/local/bin/
kind version
```

The output is similar to:

```output
kind v0.30.0 go1.24.6 linux/arm64
```

### Configure network settings

Add required loopback IP addresses for Gardener services and local API endpoints:

```console
sudo ip addr add 172.18.255.1/32 dev lo
sudo ip addr add 172.18.255.22/32 dev lo
ip addr show lo
```

Add a hosts entry to map the Gardener domain name to localhost:

```console
echo "127.0.0.1 garden.local.gardener.cloud" | sudo tee -a /etc/hosts
```

The output is similar to:

```output
127.0.0.1 garden.local.gardener.cloud
```

### Clone the Gardener repository

Download the Gardener source code and check out a stable release version:

```console
cd ~
git clone https://github.com/gardener/gardener.git
cd gardener
git fetch --all --tags
git checkout v1.122.0
```

### Remove the Kind network

Remove any existing Kind network from previous installations to avoid conflicts:

```console
docker network rm kind
```

The expected output indicates the network doesn't exist yet:

```output
Error response from daemon: network kind not found
exit status 1
```

Verify the Kind network is absent:

```console
docker network ls
```

The output is similar to:

```output
NETWORK ID     NAME      DRIVER    SCOPE
bb9f7955c11b   bridge    bridge    local
aec64365a860   host      host      local
d60c34b45e0a   none      null      local
```

The Kind network isn't listed, confirming a clean state for installation.

### Create the KinD cluster

Create the Kubernetes cluster using Kind:

```console
make kind-up
```

The output is similar to:

```output
clusterrolebinding.rbac.authorization.k8s.io/system:metrics-server serverside-applied
service/metrics-server serverside-applied
deployment.apps/metrics-server serverside-applied
apiservice.apiregistration.k8s.io/v1beta1.metrics.k8s.io serverside-applied
[gardener-local-control-plane] Setting up containerd registry mirror for host gcr.io.
[gardener-local-control-plane] Setting up containerd registry mirror for host registry.k8s.io.
[gardener-local-control-plane] Setting up containerd registry mirror for host quay.io.
[gardener-local-control-plane] Setting up containerd registry mirror for host europe-docker.pkg.dev.
[gardener-local-control-plane] Setting up containerd registry mirror for host garden.local.gardener.cloud:5001.
Waiting for FelixConfiguration to be created...
FelixConfiguration 'default' successfully updated.
Approving Kubelet Serving Certificate Signing Requests...
certificatesigningrequest.certificates.k8s.io/csr-nbmbj approved
certificatesigningrequest.certificates.k8s.io/csr-rnvdk approved
Kubelet Serving Certificate Signing Requests approved.
```

The cluster creation takes two to three minutes.

{{% notice Note %}}
If the `make kind-up` command fails, reset the loopback interfaces and retry:
```console
sudo ip addr del 172.18.255.1/32 dev lo
sudo ip addr del 172.18.255.22/32 dev lo
sudo ip addr add 172.18.255.1/32 dev lo
sudo ip addr add 172.18.255.22/32 dev lo
ip addr show lo
make kind-up
```
{{% /notice %}}

### Configure kubectl access

Set the kubeconfig environment variable to connect kubectl to your new cluster:

```console
export KUBECONFIG=$PWD/example/gardener-local/kind/local/kubeconfig
kubectl get nodes
```

The output is similar to:

```output
NAME                           STATUS   ROLES           AGE   VERSION
gardener-local-control-plane   Ready    control-plane   41s   v1.32.5
```

A node in "Ready" status confirms the cluster is operational.

### Deploy Gardener components

Install all Gardener control plane services, including the API server, controller, scheduler, and monitoring tools:

```console
make gardener-up
kubectl get pods -n garden
```

The output is similar to:

```output
NAME                                                  READY   STATUS    RESTARTS        AGE
dependency-watchdog-prober-d47b5899f-9dltz            1/1     Running   0               118s
dependency-watchdog-prober-d47b5899f-gn7fh            1/1     Running   0               118s
dependency-watchdog-weeder-66f8bffd8b-skb64           1/1     Running   0               118s
dependency-watchdog-weeder-66f8bffd8b-th59c           1/1     Running   0               118s
etcd-0                                                1/1     Running   0               3m56s
etcd-druid-65d56db866-bstcm                           1/1     Running   0               118s
etcd-druid-65d56db866-zkfjb                           1/1     Running   0               117s
fluent-bit-8259c-s5wnv                                1/1     Running   0               98s
fluent-operator-5b9ff5bfb7-6tz2w                      1/1     Running   0               118s
fluent-operator-5b9ff5bfb7-6xqfx                      1/1     Running   0               118s
gardener-admission-controller-899c585bf-2mp9g         1/1     Running   2 (3m41s ago)   3m44s
gardener-admission-controller-899c585bf-xp2f4         1/1     Running   2 (3m41s ago)   3m44s
gardener-apiserver-54fcdfcd97-5zkgr                   1/1     Running   0               3m44s
gardener-controller-manager-77bf4b686f-zxgsh          1/1     Running   3 (3m20s ago)   3m44s
gardener-extension-admission-local-57d674d98f-fswsz   1/1     Running   0               25s
gardener-extension-admission-local-57d674d98f-fwg49   1/1     Running   0               25s
gardener-resource-manager-cfd685fc5-jdv8v             1/1     Running   0               2m34s
gardener-resource-manager-cfd685fc5-spmrr             1/1     Running   0               2m34s
gardener-scheduler-6599d654c9-vw2q5                   1/1     Running   0               3m44s
gardenlet-59cb4b6956-9htmc                            1/1     Running   0               2m45s
kube-state-metrics-seed-f89d48b49-hbddp               1/1     Running   0               118s
kube-state-metrics-seed-f89d48b49-sc66l               1/1     Running   0               118s
nginx-ingress-controller-5bb9b58c44-ck2q7             1/1     Running   0               118s
nginx-ingress-controller-5bb9b58c44-r8wwd             1/1     Running   0               117s
nginx-ingress-k8s-backend-5547dddffd-fqsfm            1/1     Running   0               117s
perses-operator-9f9694dcd-wvl5z                       1/1     Running   0               119s
plutono-776964667b-225r7                              2/2     Running   0               117s
prometheus-aggregate-0                                2/2     Running   0               113s
prometheus-cache-0                                    2/2     Running   0               113s
prometheus-operator-8447dc86f9-6mb25                  1/1     Running   0               119s
prometheus-seed-0                                     2/2     Running   0               112s
vali-0                                                2/2     Running   0               118s
vpa-admission-controller-76b4c99684-4m6pb             1/1     Running   0               115s
vpa-admission-controller-76b4c99684-qf8c6             1/1     Running   0               115s
vpa-recommender-5b668455db-fctrs                      1/1     Running   0               116s
vpa-recommender-5b668455db-sdpv6                      1/1     Running   0               116s
vpa-updater-7dd7dccc6d-bcgv8                          1/1     Running   0               116s
vpa-updater-7dd7dccc6d-jdxrg                          1/1     Running   0               116s
```

### Verify seed cluster
This checks whether the seed cluster (the infrastructure cluster managed by Gardener) is healthy and ready.

``` console
./hack/usage/wait-for.sh seed local GardenletReady SeedSystemComponentsHealthy ExtensionsReady
kubectl get seeds
```

The output is similar to:

```output
⏳ Checking last operation state and conditions for seed/local with a timeout of 600 seconds...
✅ Last operation state is 'Succeeded' and all conditions passed for seed/local.
NAME    STATUS   LAST OPERATION               PROVIDER   REGION   AGE     VERSION    K8S VERSION
local   Ready    Reconcile Succeeded (100%)   local      local    2m48s   v1.122.0   v1.32.5
```

A "Ready" status with "Succeeded" operation confirms the Seed cluster is fully operational.

### Create a Shoot cluster

A Shoot cluster is a user-managed Kubernetes cluster created and managed by Gardener. Create a sample Shoot cluster:

```console
kubectl apply -f example/provider-local/shoot.yaml
kubectl -n garden-local get shoots
```

The output is similar to:

```output
shoot.core.gardener.cloud/local created
> kubectl -n garden-local get shoots
NAME    CLOUDPROFILE   PROVIDER   REGION   K8S VERSION   HIBERNATION   LAST OPERATION            STATUS    AGE
local   local          local      local    1.33.0        Awake         Create Succeeded (100%)   healthy   3h45m
```

The Shoot cluster creation takes four to five minutes. Wait for the "STATUS" column to show "healthy" before proceeding.

### Add Shoot cluster DNS entries

Add DNS entries to resolve your Shoot cluster's API endpoint:

```console
cat <<EOF | sudo tee -a /etc/hosts
# Shoot cluster DNS
172.18.255.1 api.local.local.external.local.gardener.cloud
172.18.255.1 api.local.local.internal.local.gardener.cloud
EOF
```

### Generate Shoot cluster kubeconfig

Generate an admin kubeconfig to access and manage your Shoot cluster:

{{% notice Note %}}
Wait four to five minutes after creating the Shoot cluster before running these commands. If they fail, wait another minute and retry.
{{% /notice %}}

```console
./hack/usage/generate-admin-kubeconf.sh > admin-kubeconf.yaml
KUBECONFIG=admin-kubeconf.yaml kubectl get nodes
```

{{% notice Note %}}
If you get the following result from the "kubectl get nodes" command above:
```output
No resources found
```
Please wait a bit and retry again. Your nodes are still being generated! 
{{% /notice %}}


You should see an output similar to:

```output
NAME                                            STATUS   ROLES    AGE   VERSION
machine-shoot--local--local-local-68499-nhvjl   Ready    worker   12m   v1.33.0
```

{{% notice Note %}}
If you see "No resources found", your worker nodes are still being created. Wait one to two minutes and retry the command.
{{% /notice %}}

## Summary and what's next

You have successfully installed Gardener Local on your Arm64 SUSE VM with all required dependencies and tools. Your Garden, Seed, and Shoot clusters are running and ready for workload deployment. You're now ready to verify cluster health and test deployments!
