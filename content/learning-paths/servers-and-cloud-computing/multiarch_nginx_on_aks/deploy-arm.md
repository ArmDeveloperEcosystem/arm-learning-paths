---
title: Deploy nginx on Arm 
weight: 50

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Add the Arm deployment and service

In this section, you'll add nginx on Arm to your existing cluster, completing your multi-architecture Intel/Arm environment for comprehensive performance comparison.

When applied, the **arm_nginx.yaml** file creates the following K8s objects:
   - **Deployment** (`nginx-arm-deployment`) - Pulls the multi-architecture nginx image from DockerHub, launches a pod on the Arm node, and mounts the shared ConfigMap as `/etc/nginx/nginx.conf`
   - **Service** (`nginx-arm-svc`) - Load balancer targeting pods with both `app: nginx-multiarch` and `arch: arm` labels

Copy and paste the following commands into a terminal to download and apply the Arm deployment and service:

```bash
curl -o arm_nginx.yaml https://raw.githubusercontent.com/geremyCohen/nginxOnAKS/refs/heads/main/arm_nginx.yaml
kubectl apply -f arm_nginx.yaml
```

You will see output similar to:

```output
deployment.apps/nginx-arm-deployment created
service/nginx-arm-svc created
```

### Examining the deployment configuration

Taking a closer look at the `arm_nginx.yaml` deployment file, you'll see settings optimized for the Arm architecture:

The `nodeSelector` value of `kubernetes.io/arch: arm64` ensures that the deployment only runs on Arm nodes, utilizing the `arm64` version of the nginx container image.

```yaml
    spec:
      nodeSelector:
        kubernetes.io/arch: arm64
```

The service selector uses both `app: nginx-multiarch` and `arch: arm` labels to target only Arm pods. This dual-label approach allows for both architecture-specific and multi-architecture service routing.

```yaml
  selector:
    app: nginx-multiarch
    arch: arm
```

### Verify the deployment

Get the status of nodes, pods and services by running:

```bash
kubectl get nodes,pods,svc -nnginx 
```

Your output should be similar to the following, showing two nodes, two pods, and two services:

```output
NAME                                 STATUS   ROLES    AGE   VERSION
node/aks-arm-56500727-vmss000000     Ready    <none>   59m   v1.32.7
node/aks-intel-31372303-vmss000000   Ready    <none>   63m   v1.32.7

NAME                                          READY   STATUS    RESTARTS   AGE
pod/nginx-arm-deployment-5bf8df95db-wznff     1/1     Running   0          36s
pod/nginx-intel-deployment-78bb8885fd-mw24f   1/1     Running   0          9m21s

NAME                      TYPE           CLUSTER-IP     EXTERNAL-IP     PORT(S)        AGE
service/nginx-arm-svc     LoadBalancer   10.0.241.154   48.192.64.197   80:30082/TCP   36s
service/nginx-intel-svc   LoadBalancer   10.0.226.250   20.80.128.191   80:30080/TCP   9m22s
```

You can also verify the shared ConfigMap is available:

```bash
kubectl get configmap -nnginx
```

The output is similar to:

```output
NAME               DATA   AGE
nginx-config       1      10m
```

When the pods show `Running` and the service shows a valid `External IP`, you're ready to test the nginx Arm service.

### Test the nginx web service on Arm

Run the following command to make an HTTP request to the Arm nginx service using the script you created earlier:

```bash
./nginx_util.sh curl arm
```

You get back the HTTP response, as well as information about which pod served it:

```output
Using service endpoint 48.192.64.197 for curl on arm service
Response:
{
  "message": "nginx response",
  "timestamp": "2025-10-24T22:04:59+00:00",
  "server": "nginx-arm-deployment-5bf8df95db-wznff",
  "request_uri": "/"
}
Served by: nginx-arm-deployment-5bf8df95db-wznff
```

If you see similar output, you have successfully added Arm nodes to your cluster running nginx.

### Compare both architectures

Now you can test both architectures and compare their responses:

```bash
./nginx_util.sh curl intel
./nginx_util.sh curl arm
```

Each command will route to its respective architecture-specific service, allowing you to compare performance and verify that your multi-architecture cluster is working correctly.
