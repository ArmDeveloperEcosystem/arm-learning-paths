---
title: Deploy nginx AMD to the cluster
weight: 40

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Add AMD deployment and service

In this section, you'll add nginx on AMD nodes to your existing cluster, creating a hybrid Intel/AMD environment for performance comparison.

1. Use a text editor to copy the following YAML and save it to a file called `amd_nginx.yaml`:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-amd-deployment
  labels:
    app: nginx-multiarch
  namespace: nginx
spec:
  replicas: 1
  selector:
    matchLabels:
      arch: amd
  template:
    metadata:
      labels:
        app: nginx-multiarch
        arch: amd
    spec:
      nodeSelector:
        agentpool: amd
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
  name: nginx-amd-svc
  namespace: nginx
spec:
  sessionAffinity: None
  ports:
  - nodePort: 30081
    port: 80
    protocol: TCP
    targetPort: 80
  selector:
    arch: amd
  type: LoadBalancer
```

When the above is applied:

* A new deployment called `nginx-amd-deployment` is created. This deployment pulls the same multi-architecture nginx image from DockerHub. 

Of particular interest is the `nodeSelector` `agentpool`, with the value of `amd`. This ensures that the deployment only runs on AMD nodes, utilizing the amd64 version of the nginx container image.

* A new load balancer service `nginx-amd-svc` is created, targeting all pods with the `arch: amd` label (the AMD deployment creates these pods).

### Apply the AMD deployment and service

1. Run the following command to apply the AMD deployment and service:

```bash
kubectl apply -f amd_nginx.yaml
```

You see the following response:

```output
deployment.apps/nginx-amd-deployment created
service/nginx-amd-svc created
```

2. Get the status of nodes, pods and services by running:

```bash
kubectl get nodes,pods,svc -nnginx 
```

Your output should be similar to the following, showing three nodes, two pods, and two services:

```output
NAME                                STATUS   ROLES    AGE   VERSION
node/aks-amd-10099357-vmss000000    Ready    <none>   45m   v1.32.7
node/aks-arm-49028967-vmss000000    Ready    <none>   47m   v1.32.7
node/aks-intel-34846084-vmss000000  Ready    <none>   50m   v1.32.7

NAME                                        READY   STATUS    RESTARTS   AGE
pod/nginx-amd-deployment-7d4c8f9b-abc34    1/1     Running   0          2m
pod/nginx-intel-deployment-dc84dc59f-7qb72  1/1     Running   0          15m

NAME                      TYPE           CLUSTER-IP    EXTERNAL-IP     PORT(S)        AGE
service/nginx-amd-svc     LoadBalancer   10.0.67.234   20.4.5.6        80:30081/TCP   2m
service/nginx-intel-svc   LoadBalancer   10.0.45.123   20.1.2.3        80:30080/TCP   15m
```

When the pods show `Running` and the service shows a valid `External IP`, you're ready to test the nginx AMD service.

### Test the nginx web service on AMD

3. Run the following to make an HTTP request to the AMD nginx service using the script you created earlier:

```bash
./nginx_util.sh get amd
```

You get back the HTTP response, as well as the log line from the AMD pod that served it:

```output
Using service endpoint 20.4.5.6 for get on **amd service**
Response: <title>Welcome to nginx!</title>
Served by: nginx-**amd**-deployment-7d4c8f9b-abc34
```

If you see the output `Welcome to nginx!` and the pod log shows `nginx-amd-deployment`, you have successfully added AMD nodes to your cluster running nginx.
