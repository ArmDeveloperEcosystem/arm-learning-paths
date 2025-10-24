---
title: Deploy nginx Intel to the cluster
weight: 30

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Deployment and service

In this section, you'll add a new namespace, deployment, and service for nginx on Intel. The end result will be a K8s cluster running nginx accessible via the Internet through a load balancer. 

To better understand the individual components, the configuration is split into two files:

1. **namespace.yaml** - Creates a new namespace called `nginx`, which contains all your K8s nginx objects

2. **intel_nginx.yaml** - Creates the following K8s objects:
   - **ConfigMap** (`nginx-intel-config`) - Contains performance-optimized nginx configuration
   - **Deployment** (`nginx-intel-deployment`) - Pulls a multi-architecture [nginx image](https://hub.docker.com/_/nginx) from DockerHub, launches a pod on the Intel node, and mounts the ConfigMap as `/etc/nginx/nginx.conf`
   - **Service** (`nginx-intel-svc`) - Load balancer targeting pods with both `app: nginx-multiarch` and `arch: intel` labels


The following commands download, create, and apply the namespace and Intel nginx deployment and service configuration:

```bash
curl -o namespace.yaml https://raw.githubusercontent.com/geremyCohen/nginxOnAKS/refs/heads/main/namespace.yaml
kubectl apply -f namespace.yaml

curl -o intel_nginx.yaml https://raw.githubusercontent.com/geremyCohen/nginxOnAKS/refs/heads/main/intel_nginx.yaml
kubectl apply -f intel_nginx.yaml

```

You will see output similar to:

```output
namespace/nginx created
configmap/nginx-intel-config created
deployment.apps/nginx-intel-deployment created
service/nginx-intel-svc created
```

### Examining the deployment configuration
Taking a closer look at the `intel_nginx.yaml` deployment file, you'll see some settings that ensure the deployment runs as we expect on the Intel node:

* The `nodeSelector` `kubernetes.io/arch: amd64`. This ensures that the deployment only runs on x86_64 nodes, utilizing the amd64 version of the nginx container image.

```yaml
    spec:
      nodeSelector:
        kubernetes.io/arch: amd64
```

{{% notice Note %}}
The `amd64` architecture label represents x86_64 nodes, which can be either AMD or Intel processors. In this tutorial, we're using Intel x64 nodes.
{{% /notice %}}

* The A `sessionAffinity` tag, which removes sticky connections to the target pods. This removes persistent connections to the same pod on each request.

```yaml
spec:
  sessionAffinity: None
```

* The service selector uses both `app: nginx-multiarch` and `arch: intel` labels to target only Intel pods. This dual-label approach allows for both architecture-specific and multi-architecture service routing.

```yaml
  selector:
    app: nginx-multiarch
    arch: intel
```

* Since the final goal is running nginx on multiple architectures, the deployment uses the standard nginx image from DockerHub. This image supports multiple architectures, including amd64 (Intel), arm64 (ARM), and others.

```yaml
      containers:
      - image: nginx:latest
        name: nginx
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

Your output should be similar to the following, showing two nodes, one pod, and one service:

```output
NAME                                 STATUS   ROLES    AGE   VERSION
node/aks-arm-56500727-vmss000000     Ready    <none>   50m   v1.32.7
node/aks-intel-31372303-vmss000000   Ready    <none>   55m   v1.32.7

NAME                                          READY   STATUS    RESTARTS   AGE
pod/nginx-intel-deployment-78bb8885fd-mw24f   1/1     Running   0          38s

NAME                      TYPE           CLUSTER-IP     EXTERNAL-IP     PORT(S)        AGE
service/nginx-intel-svc   LoadBalancer   10.0.226.250   20.80.128.191   80:30080/TCP   39s
```

You can also verify the ConfigMap was created:

```bash
kubectl get configmap -nnginx
```

```output
NAME                 DATA   AGE
nginx-intel-config   1      51s
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


