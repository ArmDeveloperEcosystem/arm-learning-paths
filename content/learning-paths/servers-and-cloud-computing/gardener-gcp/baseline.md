---
title: Gardener  Baseline Testing on Google Axion C4A Arm Virtual Machine
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Gardener Baseline Testing on GCP SUSE VMs
This section checks whether your Gardener Local setup is working correctly on an Arm-based GCP Axion (C4A) VM before running real workloads.

### Set Kubeconfig
This tells Kubernetes commands (**kubectl) which cluster to talk to**. Without this, kubectl won’t know where your Gardener cluster is.
``` console
export KUBECONFIG=$PWD/example/gardener-local/kind/local/kubeconfig
```

### Check Cluster Health
Before testing any workload, verify that the Gardener-local Kubernetes cluster is healthy. This ensures the control plane and node are functional.

``` console
kubectl get nodes -o wide
kubectl get pods -A
```
You should see an output similar to:

```output
NAME                           STATUS   ROLES           AGE    VERSION   INTERNAL-IP   EXTERNAL-IP   OS-IMAGE                         KERNEL-VERSION                  CONTAINER-RUNTIME
gardener-local-control-plane   Ready    control-plane   148m   v1.32.5   172.18.0.2    <none>        Debian GNU/Linux 12 (bookworm)   5.14.21-150500.55.124-default   containerd://2.1.1
extension-networking-calico-8z7jw           gardener-extension-networking-calico-94bcb44bf-kmmpj   1/1     Running   0              102m
extension-networking-calico-8z7jw           gardener-extension-networking-calico-94bcb44bf-whgtn   1/1     Running   0              135m
extension-provider-local-m7d79              gardener-extension-provider-local-fc75c4494-47szg      1/1     Running   0              137m
extension-provider-local-m7d79              gardener-extension-provider-local-fc75c4494-hkksz      1/1     Running   0              137m
garden                                      dependency-watchdog-prober-d47b5899f-ml6x9             1/1     Running   0              61m
garden                                      dependency-watchdog-prober-d47b5899f-xmzh2             1/1     Running   0              60m
garden                                      dependency-watchdog-weeder-66f8bffd8b-lgx7f            1/1     Running   0              60m
garden                                      dependency-watchdog-weeder-66f8bffd8b-vd9md            1/1     Running   0              61m
garden                                      etcd-0                                                 1/1     Running   0              141m
garden                                      etcd-druid-65d56db866-bstcm                            1/1     Running   0              139m
garden                                      etcd-druid-65d56db866-zkfjb                            1/1     Running   0              139m
garden                                      fluent-bit-8259c-s5wnv                                 1/1     Running   0              139m
garden                                      fluent-operator-5b9ff5bfb7-6ffvc                       1/1     Running   0              137m
garden                                      fluent-operator-5b9ff5bfb7-cw67l                       1/1     Running   0              137m
garden                                      gardener-admission-controller-899c585bf-2mp9g          1/1     Running   2 (141m ago)   141m
garden                                      gardener-admission-controller-899c585bf-xp2f4          1/1     Running   2 (141m ago)   141m
garden                                      gardener-apiserver-54fcdfcd97-5zkgr                    1/1     Running   0              141m
garden                                      gardener-controller-manager-77bf4b686f-zxgsh           1/1     Running   3 (140m ago)   141m
garden                                      gardener-extension-admission-local-57d674d98f-6qbcv    1/1     Running   0              136m
garden                                      gardener-extension-admission-local-57d674d98f-zlgpd    1/1     Running   0              135m
garden                                      gardener-resource-manager-cfd685fc5-n9mp7              1/1     Running   0              133m
garden                                      gardener-resource-manager-cfd685fc5-spbn7              1/1     Running   0              134m
garden                                      gardener-scheduler-6599d654c9-vw2q5                    1/1     Running   0              141m
garden                                      gardenlet-59cb4b6956-hsmdp                             1/1     Running   0              96m
garden                                      kube-state-metrics-seed-f89d48b49-94l46                1/1     Running   0              121m
garden                                      kube-state-metrics-seed-f89d48b49-q95kr                1/1     Running   0              130m
garden                                      nginx-ingress-controller-5bb9b58c44-ck2q7              1/1     Running   0              139m
garden                                      nginx-ingress-controller-5bb9b58c44-r8wwd              1/1     Running   0              139m
garden                                      nginx-ingress-k8s-backend-5547dddffd-fqsfm             1/1     Running   0              139m
garden                                      perses-operator-9f9694dcd-wvl5z                        1/1     Running   0              139m
garden                                      plutono-776964667b-225r7                               2/2     Running   0              139m
garden                                      prometheus-aggregate-0                                 2/2     Running   0              87m
garden                                      prometheus-cache-0                                     2/2     Running   0              22m
garden                                      prometheus-operator-8447dc86f9-6mb25                   1/1     Running   0              139m
garden                                      prometheus-seed-0                                      2/2     Running   0              87m
garden                                      vali-0                                                 2/2     Running   0              139m
garden                                      vpa-admission-controller-76b4c99684-lkf27              1/1     Running   0              30m
garden                                      vpa-admission-controller-76b4c99684-tkg7n              1/1     Running   0              81m
garden                                      vpa-recommender-5b668455db-fctrs                       1/1     Running   0              139m
garden                                      vpa-recommender-5b668455db-sdpv6                       1/1     Running   0              139m
garden                                      vpa-updater-7dd7dccc6d-dgg7r                           1/1     Running   0              131m
garden                                      vpa-updater-7dd7dccc6d-whlqx                           1/1     Running   0              133m
gardener-extension-provider-local-coredns   coredns-69d964db7f-mrmq9                               1/1     Running   0              139m
istio-ingress                               istio-ingressgateway-5b48596bf9-4pzsw                  1/1     Running   0              139m
istio-ingress                               istio-ingressgateway-5b48596bf9-ff4zp                  1/1     Running   0              139m
istio-system                                istiod-769565bbdb-2hnzz                                1/1     Running   0              76m
istio-system                                istiod-769565bbdb-wlbts                                1/1     Running   0              77m
kube-system                                 calico-kube-controllers-bfc8cf74c-pj9hh                1/1     Running   0              148m
kube-system                                 calico-node-88sdt                                      1/1     Running   0              148m
kube-system                                 coredns-54bf7d48d5-j6zbg                               1/1     Running   0              148m
kube-system                                 coredns-54bf7d48d5-zrqqc                               1/1     Running   0              148m
kube-system                                 etcd-gardener-local-control-plane                      1/1     Running   0              148m
kube-system                                 kube-apiserver-gardener-local-control-plane            1/1     Running   0              148m
kube-system                                 kube-controller-manager-gardener-local-control-plane   1/1     Running   0              148m
kube-system                                 kube-proxy-fxxzc                                       1/1     Running   0              148m
kube-system                                 kube-scheduler-gardener-local-control-plane            1/1     Running   0              148m
kube-system                                 metrics-server-78b7d676c8-cjwrs                        1/1     Running   0              148m
local-path-storage                          local-path-provisioner-7dc846544d-m825q                1/1     Running   0              148m
registry                                    registry-c85bbb98c-lqtcj                               1/1     Running   0              148m
registry                                    registry-europe-docker-pkg-dev-7956694cfb-hbg69        1/1     Running   0              148m
registry                                    registry-gcr-6d4b454594-b9plv                          1/1     Running   0              148m
registry                                    registry-k8s-5bf5795799-t44xd                          1/1     Running   0              148m
registry                                    registry-quay-84dbcd78b4-dw2pn                         1/1     Running   0              148m
shoot--local--local                         blackbox-exporter-58c4f64c97-l96ct                     1/1     Running   0              104m
shoot--local--local                         blackbox-exporter-58c4f64c97-nlhjj                     1/1     Running   0              105m
shoot--local--local                         cluster-autoscaler-b894888d6-qwrpp                     1/1     Running   0              116m
shoot--local--local                         etcd-events-0                                          2/2     Running   0              136m
shoot--local--local                         etcd-main-0                                            2/2     Running   0              136m
shoot--local--local                         event-logger-777b7b7c7c-77h9n                          1/1     Running   0              133m
shoot--local--local                         gardener-resource-manager-764b5d4f97-bdd8n             1/1     Running   0              118m
shoot--local--local                         gardener-resource-manager-764b5d4f97-z48b5             1/1     Running   0              129m
shoot--local--local                         kube-apiserver-6545887cc9-26h5w                        1/1     Running   0              124m
shoot--local--local                         kube-apiserver-6545887cc9-gf92k                        1/1     Running   0              98m
shoot--local--local                         kube-controller-manager-555b598dbf-45n8v               1/1     Running   0              122m
shoot--local--local                         kube-scheduler-695d49b6c5-xr7hp                        1/1     Running   0              125m
shoot--local--local                         kube-state-metrics-76cc7bb4f9-xq4g2                    1/1     Running   0              130m
shoot--local--local                         machine-controller-manager-775dc6d574-mntqt            2/2     Running   0              111m
shoot--local--local                         machine-shoot--local--local-local-68499-nhvjl          1/1     Running   0              131m
shoot--local--local                         plutono-869d676bb9-jjwcx                               2/2     Running   0              133m
shoot--local--local                         prometheus-shoot-0                                     2/2     Running   0              95m
shoot--local--local                         vali-0                                                 4/4     Running   0              133m
shoot--local--local                         vpa-admission-controller-bcc4c968c-8ndg8               1/1     Running   0              133m
shoot--local--local                         vpa-admission-controller-bcc4c968c-r6lnt               1/1     Running   0              72m
shoot--local--local                         vpa-recommender-b49f4dd7c-mk9sx                        1/1     Running   0              107m
shoot--local--local                         vpa-updater-6cc999b5bc-jcrbg                           1/1     Running   0              123m
shoot--local--local                         vpn-seed-server-7497c89db-b5p5c                         2/2     Running   0              15m
```    

### Deploy a Test Nginx Pod
This step deploys a simple web server (nginx) to confirm that workloads can run.
- Creates one nginx pod
- Confirms Kubernetes can pull images and start containers

When the pod status becomes Running, workload deployment works.

``` console
kubectl run test-nginx --image=nginx --restart=Never
kubectl get pod test-nginx -w
```
- `kubectl run test-nginx` → Creates a single nginx pod.
- `kubectl get pod test-nginx -w` → Watches pod status in real time.

You should see an output similar to:

```output
>pod/test-nginx created
> kubectl get pod test-nginx -w
NAME         READY   STATUS              RESTARTS   AGE
test-nginx   0/1     ContainerCreating   0          0s
test-nginx   0/1     ContainerCreating   0          1s
test-nginx   1/1     Running             0          4s
```

Now, press "ctrl-c" in the ssh shell to kill the currently running monitor. 

### Expose the Pod (ClusterIP Service)
Pods cannot be accessed directly by other pods reliably.
So we create a Kubernetes Service.
- The service gives nginx a stable internal IP
- It allows other pods to reach nginx using a name

This confirms Kubernetes service networking is working.

``` console
kubectl expose pod test-nginx --port=80 --name=test-nginx-svc
kubectl get svc test-nginx-svc
```
- `kubectl expose pod` → Creates a ClusterIP service on port 80.
- `kubectl get svc` → Shows the service details.

You should see an output similar to:

```output
>service/test-nginx-svc exposed
> kubectl get svc test-nginx-svc
NAME             TYPE        CLUSTER-IP    EXTERNAL-IP   PORT(S)   AGE
test-nginx-svc   ClusterIP   10.2.194.17   <none>        80/TCP    9s
```
A ClusterIP is assigned (example: 10.2.194.17). This confirms that Kubernetes services are functioning.

### Test Service-to-Pod Connectivity
Now we verify that one pod can talk to another pod through a service.

- Start a temporary curl pod
- Send an HTTP request to the nginx service

**Start a curl pod:** Create a temporary curl pod.

``` console
kubectl run curl --image=curlimages/curl -i --tty -- sh
```

Inside pod shell:

``` console
curl http://test-nginx-svc
```
Exit shell:

``` console
exit
```

You should see an output similar to:

```output
All commands and output from this session will be recorded in container logs, including credentials and sensitive information passed through the command prompt.
If you don't see a command prompt, try pressing enter.
~ $ curl http://test-nginx-svc
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
html { color-scheme: light dark; }
body { width: 35em; margin: 0 auto;
font-family: Tahoma, Verdana, Arial, sans-serif; }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
~ $ exit
Session ended, resume using 'kubectl attach curl -c curl -i -t' command when the pod is running
```
This confirms pod-to-service networking.

- Creates a curl container with an interactive shell.
- Uses curl to send an HTTP request to the nginx service.

### Test DNS Resolution
Ensures CoreDNS is functioning and services resolve properly. Run `nslookup` inside the curl pod to check DNS service discovery.

- `nslookup test-nginx-svc` checks if DNS can resolve the service name
- `CoreDNS` is responsible for this

If DNS resolves correctly, service discovery is healthy.

``` console
kubectl exec curl -- nslookup test-nginx-svc.default.svc.cluster.local
```

You should see an output similar to:

```output
Server:         10.2.0.10
Address:        10.2.0.10:53

Name:   test-nginx-svc.default.svc.cluster.local
Address: 10.2.194.17
```
If DNS fails, networking or CoreDNS is broken.

### Test Logs and Exec
This confirms two important Kubernetes features:
- Logs – you can debug applications
- Exec – you can run commands inside containers

If logs show nginx startup and exec returns version info, pod access works.

``` console
kubectl logs test-nginx | head
kubectl exec test-nginx -- nginx -v
```
- `kubectl logs` → Shows nginx pod logs.
- `kubectl exec` → Runs nginx -v inside the pod.

You should see an output similar to:

```output
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
/docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
2025/11/25 07:50:33 [notice] 1#1: using the "epoll" event method

> kubectl exec test-nginx -- nginx -v
nginx version: nginx/1.29.3
```
- Logs show nginx starting.
- Exec shows nginx version (e.g., `nginx version: nginx/1.25.3`).

### Delete Test Resources
Once testing is complete, temporary resources should be removed.
- Deletes nginx and curl pods
- Deletes the service
 
``` console
kubectl delete pod test-nginx curl
kubectl delete svc test-nginx-svc
```
Confirms cleanup works and keeps the cluster clean.

You should see an output similar to:

```output
pod "test-nginx" deleted from default namespace
pod "curl" deleted from default namespace
> kubectl delete svc test-nginx-svc
service "test-nginx-svc" deleted from default namespace
```
After completing these steps, you have confirmed that the Kubernetes cluster and Gardener setup are healthy, core components are functioning correctly, pods start successfully, networking and services operate as expected, DNS resolution works, and the cluster is ready to run real workloads.
