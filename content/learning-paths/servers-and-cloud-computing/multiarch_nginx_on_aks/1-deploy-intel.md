---
title: Deploy nginx Intel to the cluster
weight: 30

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Deployment and service

In this section, you'll bootstrap the cluster with nginx on Intel, simulating an existing Kubernetes (K8s) cluster running nginx. In the next section, you'll add arm64 nodes alongside the Intel nodes for performance comparison. 

1. Use a text editor to copy the following YAML and save it to a file called `namespace.yaml`:

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: nginx
```

Applying this YAML creates a new namespace called `nginx`, which contains all subsequent K8s objects.

2. Use a text editor to copy the following YAML and save it to a file called `intel_nginx.yaml`:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-intel-deployment
  labels:
    app: nginx-multiarch
  namespace: nginx
spec:
  replicas: 1
  selector:
    matchLabels:
      arch: intel
  template:
    metadata:
      labels:
        app: nginx-multiarch
        arch: intel
    spec:
      nodeSelector:
        agentpool: intel
      containers:
      - image: nginx:latest
        name: nginx-multiarch
        ports:
        - containerPort: 80
          name: http
          protocol: TCP
---
apiVersion: v1
kind: Service
metadata:
  name: nginx-intel-svc
  namespace: nginx
spec:
  sessionAffinity: None
  ports:
  - nodePort: 30080
    port: 80
    protocol: TCP
    targetPort: 80
  selector:
    arch: intel
  type: LoadBalancer
```

When the above is applied:

* A new deployment called `nginx-intel-deployment` is created. This deployment pulls a multi-architecture [nginx image](https://hub.docker.com/_/nginx) from DockerHub. 

Of particular interest is the `nodeSelector` `agentpool`, with the value of `intel`. This ensures that the deployment only runs on Intel nodes, utilizing the amd64 version of the nginx container image. 

* A new load balancer service `nginx-intel-svc` is created, targeting all pods with the `arch: intel` label (the Intel deployment creates these pods).

A `sessionAffinity` tag is added to this service to remove sticky connections to the target pods. This removes persistent connections to the same pod on each request.

### Apply the Intel deployment and service

1. Run the following commands to apply the namespace, deployment, and service definitions:

```bash
kubectl apply -f namespace.yaml
kubectl apply -f intel_nginx.yaml
```

You see the following responses:

```output
namespace/nginx created
deployment.apps/nginx-intel-deployment created
service/nginx-intel-svc created
```

2. Optionally, set the `default Namespace` to `nginx` to simplify future commands:

```bash
kubectl config set-context --current --namespace=nginx
```

3. Get the status of nodes, pods and services by running:

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

When the pods show `Running` and the service shows a valid `External IP`, you're ready to test the nginx Intel service.

### Test the Intel service

4. Run the following to make an HTTP request to the Intel nginx service:

```bash
./nginx_util.sh get intel
```

You get back the HTTP response, as well as information about which pod served it:

```output
Using service endpoint 48.223.233.136 for get on **intel service**
Response: <title>Welcome to nginx!</title>
Served by: nginx-**intel**-deployment-dc84dc59f-7qb72
```

If you see the output `Welcome to nginx!` you have successfully bootstrapped your AKS cluster with an Intel node, running a deployment with the nginx multi-architecture container instance.

Continue to the next section to create the test utility that will be used throughout this tutorial.
