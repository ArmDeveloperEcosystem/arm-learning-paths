---
title: Install Gardener
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install Gardener on GCP SUSE VM
This guide walks you through a clean, corrected, and fully working setup of Gardener Local on a GCP SUSE Arm64 VM, including installation of Go 1.24, the Arm64 yq binary, all required Gardener CLI tools, KinD cluster setup, shoot creation, and kubeconfig retrieval.

### Update System
This step updates the operating system packages to the latest versions to avoid bugs and compatibility issues.

``` console
sudo zypper refresh
sudo zypper update -y
```
### Enable SUSE Containers Module
This enables SUSE’s official container support, so Docker and container tools can work properly.

``` console
sudo SUSEConnect -p sle-module-containers/15.5/arm64
sudo SUSEConnect --list-extensions | grep Containers
```

You should see "Activated" as part of the output from the above commands. 

### Install Docker
Docker is required to run KinD and Kubernetes components as containers. This step installs Docker, starts it, and allows your user to run Docker without sudo.
``` console
sudo zypper refresh
sudo zypper install -y docker
sudo systemctl enable --now docker
sudo usermod -aG docker $USER
exit
```

Next, re-open a new shell into your VM and type the following:

```console
docker ps
```

You should see the following output:

```output
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```

### Install Go 1.24 (Manual)
Gardener requires a newer Go version than what SUSE provides by default. Here, Go 1.24 is downloaded and installed manually.

``` console
cd /tmp
curl -LO https://go.dev/dl/go1.24.0.linux-arm64.tar.gz
sudo rm -rf /usr/local/go
sudo tar -C /usr/local -xzf go1.24.0.linux-arm64.tar.gz
echo 'export PATH=$PATH:/usr/local/go/bin' >> ~/.consolerc
source ~/.consolerc
go version
```
You should see an output similar to:

```output
go version go1.24.0 linux/arm64
```

### Install Git, Build Tools
These tools are needed to download the Gardener source code and compile components during setup.

``` console
sudo zypper install -y git curl tar gzip make gcc
```

### Install kubectl
`kubectl` is the command-line tool for interacting with Kubernetes clusters. It lets you check nodes, pods, and cluster status.

``` console
curl -LO https://dl.k8s.io/release/v1.34.0/bin/linux/arm64/kubectl
chmod +x kubectl
sudo mv kubectl /usr/local/bin/
kubectl version --client
```

You should see an output similar to:

```output
Client Version: v1.34.0
Kustomize Version: v5.7.1
```

### Install Helm
Helm is used to install and manage Kubernetes applications. Gardener uses Helm internally to deploy its components.

``` console
curl -sSfL https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 > get_helm.sh
chmod 755 ./get_helm.sh
./get_helm.sh
helm version
```

You should see an output similar to:

```output
version.BuildInfo{Version:"v3.19.2", GitCommit:"8766e718a0119851f10ddbe4577593a45fadf544", GitTreeState:"clean", GoVersion:"go1.24.9"}
```

### Install yq
`yq` is a YAML processing tool used by Gardener scripts to read and modify configuration files.

``` console
sudo curl -L -o /usr/local/bin/yq https://github.com/mikefarah/yq/releases/download/v4.43.1/yq_linux_arm64
sudo chmod +x /usr/local/bin/yq
yq --version
```

You should see an output similar to:

```output
yq (https://github.com/mikefarah/yq/) version v4.43.1
```

### Install Kustomize
Kustomize helps customize Kubernetes YAML files without changing the original manifests.

``` console
curl -LO https://github.com/kubernetes-sigs/kustomize/releases/download/kustomize/v5.3.0/kustomize_v5.3.0_linux_arm64.tar.gz
tar -xvf kustomize_v5.3.0_linux_arm64.tar.gz
sudo mv kustomize /usr/local/bin/
kustomize version
```

You should see an output (Kustomize version) that is similar to:

```output
v5.3.0
```

### Install Kind
Kind (Kubernetes in Docker) creates a local Kubernetes cluster inside Docker. Gardener Local runs entirely on this KinD cluster.

``` console
curl -Lo kind https://kind.sigs.k8s.io/dl/v0.30.0/kind-linux-arm64
chmod +x kind
sudo mv kind /usr/local/bin/
kind version
```

You should see an output similar to:

```output
kind v0.30.0 go1.24.6 linux/arm64
```

### Add Required Loopback IPs
These special loopback IPs are needed so Gardener services and the local API endpoints work correctly.

``` console
sudo ip addr add 172.18.255.1/32 dev lo
sudo ip addr add 172.18.255.22/32 dev lo
ip addr show lo
```

### Add Hosts Entry
This step maps a Gardener domain name to the local machine so services can be accessed by name.

``` console
echo "127.0.0.1 garden.local.gardener.cloud" | sudo tee -a /etc/hosts
```

You should see an output similar to:

```output
127.0.0.1 garden.local.gardener.cloud
```

### Clone Gardener Repo
Here you download the Gardener’s source code and switch to a known, stable release version.

``` console
cd ~
git clone https://github.com/gardener/gardener.git
cd gardener
git fetch --all --tags
git checkout v1.122.0
```

### Clean Old KinD Network
This removes any leftover KinD network from previous runs to avoid IP or port conflicts.

``` console
docker network rm kind
```

You should get the following output which is correct:

```output
Error response from daemon: network kind not found
exit status 1
```

You can confirm this by typing:

```console
docker network ls
```

Your output should look something like this (note the absence of the "kind" name...its not present in the network config):

```output
NETWORK ID     NAME      DRIVER    SCOPE
bb9f7955c11b   bridge    bridge    local
aec64365a860   host      host      local
d60c34b45e0a   none      null      local
```

### Create Gardener KinD Cluster
This step creates the Kubernetes cluster using KinD and prepares it to run Gardener.

``` console
make kind-up
```

You should see an output similar to:

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

### If the above "make" command fails...

If the above make command fails, please reset the loopback interfaces as follows and re-try the make command:

``` console
sudo ip addr del 172.18.255.1/32 dev lo
sudo ip addr del 172.18.255.22/32 dev lo
sudo ip addr add 172.18.255.1/32 dev lo
sudo ip addr add 172.18.255.22/32 dev lo
ip addr show lo
make kind-up
```


### Export kubeconfig
This config file allows `kubectl` to connect to the newly created Gardener local cluster.

``` console
export KUBECONFIG=$PWD/example/gardener-local/kind/local/kubeconfig
kubectl get nodes
```
You should see an output similar to:

```output
NAME                           STATUS   ROLES           AGE   VERSION
gardener-local-control-plane   Ready    control-plane   41s   v1.32.5
```

### Deploy Gardener Components
This installs all Gardener control-plane services, including the API server, controller, scheduler, and monitoring tools.

``` console
make gardener-up
kubectl get pods -n garden
```

You should see an output similar to:

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

### Verify Seed
This checks whether the “seed” cluster (the infrastructure cluster managed by Gardener) is healthy and ready.

``` console
./hack/usage/wait-for.sh seed local GardenletReady SeedSystemComponentsHealthy ExtensionsReady
kubectl get seeds
```

You should see an output similar to:

```output
⏳ Checking last operation state and conditions for seed/local with a timeout of 600 seconds...
✅ Last operation state is 'Succeeded' and all conditions passed for seed/local.
gcpuser@lpprojectsusearm64:~/gardener> kubectl get seeds
NAME    STATUS   LAST OPERATION               PROVIDER   REGION   AGE     VERSION    K8S VERSION
local   Ready    Reconcile Succeeded (100%)   local      local    2m48s   v1.122.0   v1.32.5
```

### Create Shoot Cluster
A Shoot cluster is a user Kubernetes cluster managed by Gardener. This step creates a sample Shoot running locally.

``` console
kubectl apply -f example/provider-local/shoot.yaml
kubectl -n garden-local get shoots
```

You should see an output similar to:

```output
shoot.core.gardener.cloud/local created
> kubectl -n garden-local get shoots
NAME    CLOUDPROFILE   PROVIDER   REGION   K8S VERSION   HIBERNATION   LAST OPERATION            STATUS    AGE
local   local          local      local    1.33.0        Awake         Create Succeeded (100%)   healthy   3h45m
```

### Add shoot DNS
These DNS entries allow your system to resolve the Shoot cluster’s API endpoint correctly.

``` console
cat <<EOF | sudo tee -a /etc/hosts
# Shoot cluster DNS
172.18.255.1 api.local.local.external.local.gardener.cloud
172.18.255.1 api.local.local.internal.local.gardener.cloud
EOF
```

### Get Shoot Admin Kubeconfig

{{% notice Note %}}
You may need to wait a 4-5 minutes before running the next commands... otherwise, they may fail. 
If they fail, please wait a bit and retry again. 
{{% /notice %}}

This generates an admin kubeconfig so you can access and manage the Shoot Kubernetes cluster.

``` console
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

You now have **Gardener Local running on SUSE Arm64** with Go 1.24, Helm, kubectl, yq, Kustomize, Kind, and a working Shoot cluster.
