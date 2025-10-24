---
title: Deploy nginx Intel to the cluster
weight: 30

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Deployment and service

In this section, you'll add a new namespace, deployment, and service for nginx on Intel.  The end result will be a K8s cluster running nginx accessible via the Internet through a load balancer. 

To better understand the individual components, the configuration is split into two files:

1. Applying the namespace.yaml creates a new namespace called `nginx`, which contains all your K8s nginx objects. 

2. Applying the intel_nginx.yaml creates the following K8s objects:

2. 1. A K8s deployment called `nginx-intel-deployment`. This deployment pulls a multi-architecture [nginx image](https://hub.docker.com/_/nginx) from DockerHub, and launches a pod for it on the x86 node. 

2. 2. A K8s load balancer service `nginx-intel-svc`, targeting any pod with the `arch: intel` label (the Intel deployment will create this pod).


The following commands download, create, and apply the namespace and Intel nginx deployment and service configuration:

```bash
curl -o namespace.yaml https://raw.githubusercontent.com/geremyCohen/nginxOnAKS/refs/heads/main/namespace.yaml
kubectl apply -f namespace.yaml

curl -o intel_nginx.yaml https://raw.githubusercontent.com/geremyCohen/nginxOnAKS/refs/heads/main/intel_nginx.yaml
kubectl apply -f intel_nginx.yaml

```

When pasted into your terminal, you will see output similar to the following for each command:

You will see output similar to:

```output
curl -o intel_nginx.yaml https://raw.githubusercontent.com/geremyCohen/nginxOnAKS/refs/heads/main/intel_nginx.yaml
kubectl apply -f intel_nginx.yaml
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100    55  100    55    0     0   1242      0 --:--:-- --:--:-- --:--:--  1250
namespace/nginx unchanged
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   751  100   751    0     0  16192      0 --:--:-- --:--:-- --:--:-- 16326
deployment.apps/nginx-intel-deployment unchanged
service/nginx-intel-svc unchanged```
```

### Examining the deployment configuration
Taking a closer look at the `intel_nginx.yaml` deployment file, you'll see some settings that ensure the deployment runs as we expect on the Intel node:

* The `nodeSelector` `agentpool`, with the value of `intel`. This ensures that the deployment only runs on Intel nodes, utilizing the amd64 version of the nginx container image.

```yaml
    spec:
      nodeSelector:
        agentpool: intel
```

* The A `sessionAffinity` tag, which removes sticky connections to the target pods. This removes persistent connections to the same pod on each request.

```yaml
spec:
  sessionAffinity: None
```

* Since the final goal is running nginx on multiple architectures, the deployment uses the standard nginx image from DockerHub. This image supports multiple architectures, including amd64 (Intel), arm64 (ARM), and others.

```yaml
    - image: nginx:latest
    name: nginx-multiarch
```
{{% notice Note %}}
Optionally, you can set the `default Namespace` to `nginx` to simplify future commands by removing the need to specify the `-nnginx` flag each time:
```bash
kubectl config set-context --current --namespace=nginx
```
{{% /notice %}}

### Verify the deployment has completed
You've deployed the objects, so now it's time to verify everything is running as expected.

1. Confirm the nodes, pods, and services are running:

```bash
kubectl get nodes,pods,svc -nnginx 
```

Your output should be similar to the following, showing three nodes, one pod, and one service:

```output
NAME                                STATUS   ROLES    AGE   VERSION
node/aks-amd-10099357-vmss000000    Ready    <none>   10m   v1.32.7
node/aks-arm-49028967-vmss000000    Ready    <none>   12m   v1.32.7
node/aks-intel-34846084-vmss000000  Ready    <none>   15m   v1.32.7

NAME                                        READY   STATUS    RESTARTS   AGE
pod/nginx-intel-deployment-7d4c8f9b-xyz12  1/1     Running   0          2m

NAME                      TYPE           CLUSTER-IP    EXTERNAL-IP     PORT(S)        AGE
service/nginx-intel-svc   LoadBalancer   10.0.45.123   20.1.2.3        80:30080/TCP   2m
```

With the pods in a `Ready` state and the service showing a valid `External IP`, you're now ready to test the nginx Intel service.

### Test the Intel service

4. Run the following to make an HTTP request to the Intel nginx service:

```bash
./nginx_util.sh get intel
```

You get back the HTTP response, as well as information about which pod served it:

```output
Using service endpoint 20.3.71.69 for get on intel service
Response:
{
  "message": "nginx response",
  "timestamp": "2025-10-24T16:49:29+00:00",
  "server": "nginx-intel-deployment-758584d5c6-2nhnx",
  "request_uri": "/"
}
Served by: nginx-intel-deployment-758584d5c6-2nhnx
```

If you see output similar to above, you've successfully configured your AKS cluster with an Intel node, running an nginx deployment and service with the nginx multi-architecture container image.


