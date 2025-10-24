---
title: Deploy nginx ARM to the cluster
weight: 50

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Add ARM deployment and service

In this section, you'll add nginx on ARM nodes to your existing cluster, completing your multi-architecture Intel/AMD/ARM environment for comprehensive performance comparison.

Copy and paste the following commands into a terminal to download and apply the ARM deployment and service:

```bash
curl -o arm_nginx.yaml https://raw.githubusercontent.com/geremyCohen/nginxOnAKS/refs/heads/main/arm_nginx.yaml
kubectl apply -f arm_nginx.yaml
```

When pasted into your terminal, you will see output similar to the following for each command:

```output
curl -o arm_nginx.yaml https://raw.githubusercontent.com/geremyCohen/nginxOnAKS/refs/heads/main/arm_nginx.yaml
kubectl apply -f arm_nginx.yaml
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   739  100   739    0     0  15192      0 --:--:-- --:--:-- --:--:-- 15306
deployment.apps/nginx-arm-deployment created
service/nginx-arm-svc created
```

When the above is applied:

* A new deployment called `nginx-arm-deployment` is created. This deployment pulls the same multi-architecture nginx image from DockerHub. 

Of particular interest is the `nodeSelector` `agentpool`, with the value of `arm`. This ensures that the deployment only runs on ARM nodes, utilizing the arm64 version of the nginx container image.

* A new load balancer service `nginx-arm-svc` is created, targeting all pods with the `arch: arm` label (the ARM deployment creates these pods).

### Apply the ARM deployment and service

1. Run the following command to apply the ARM deployment and service:

```bash
kubectl apply -f arm_nginx.yaml
```

You see the following response:

```output
deployment.apps/nginx-arm-deployment created
service/nginx-arm-svc created
```

2. Get the status of nodes, pods and services by running:

```bash
kubectl get nodes,pods,svc -nnginx 
```

Your output should be similar to the following, showing three nodes, three pods, and three services:

```output
NAME                                STATUS   ROLES    AGE   VERSION
node/aks-amd-10099357-vmss000000    Ready    <none>   60m   v1.32.7
node/aks-arm-49028967-vmss000000    Ready    <none>   62m   v1.32.7
node/aks-intel-34846084-vmss000000  Ready    <none>   65m   v1.32.7

NAME                                        READY   STATUS    RESTARTS   AGE
pod/nginx-amd-deployment-7d4c8f9b-abc34    1/1     Running   0          17m
pod/nginx-arm-deployment-6f8d9c2a-def56    1/1     Running   0          2m
pod/nginx-intel-deployment-dc84dc59f-7qb72  1/1     Running   0          30m

NAME                      TYPE           CLUSTER-IP    EXTERNAL-IP     PORT(S)        AGE
service/nginx-amd-svc     LoadBalancer   10.0.67.234   20.4.5.6        80:30081/TCP   17m
service/nginx-arm-svc     LoadBalancer   10.0.89.145   20.7.8.9        80:30082/TCP   2m
service/nginx-intel-svc   LoadBalancer   10.0.45.123   20.1.2.3        80:30080/TCP   30m
```

When the pods show `Running` and the service shows a valid `External IP`, you're ready to test the nginx ARM service.

### Test the nginx web service on ARM

3. Run the following to make an HTTP request to the ARM nginx service using the script you created earlier:

```bash
./nginx_util.sh get arm
```

You get back the HTTP response, as well as the log line from the ARM pod that served it:

```output
Using service endpoint 20.7.8.9 for get on **arm service**
Response: <title>Welcome to nginx!</title>
Served by: nginx-**arm**-deployment-6f8d9c2a-def56
```

If you see the output `Welcome to nginx!` and the pod log shows `nginx-arm-deployment`, you have successfully added ARM nodes to your cluster running nginx.

### Compare all architectures

Now you can test all three architectures and compare their responses:

```bash
./nginx_util.sh get intel
./nginx_util.sh get amd  
./nginx_util.sh get arm
```

Each command will route to its respective architecture-specific service, allowing you to compare performance and verify that your multi-architecture cluster is working correctly.
