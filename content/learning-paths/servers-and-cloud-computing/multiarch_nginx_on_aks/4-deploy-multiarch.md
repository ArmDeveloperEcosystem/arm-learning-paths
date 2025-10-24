---
title: Deploy nginx multiarch service to the cluster
weight: 60

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Add multiarch service

You now have nginx running on Intel, AMD, and ARM nodes with architecture-specific services. In this section, you'll create a multiarch service that can route to any available nginx pod regardless of architecture, providing load balancing across all architectures.

### Create the multiarch service

The multiarch service targets all pods with the `app: nginx-multiarch` label (all nginx deployments share this label). It uses `sessionAffinity: None` to ensure requests are distributed across all available pods without stickiness, and can route to Intel, AMD, or ARM pods based on availability and load balancing algorithms.

1. Run the following command to download and apply the multiarch service:

```bash
curl -sO https://raw.githubusercontent.com/geremyCohen/nginxOnAKS/main/multiarch_nginx.yaml
kubectl apply -f multiarch_nginx.yaml
```

You see the following response:

```output
service/nginx-multiarch-svc created
```

2. Get the status of all services by running:

```bash
kubectl get svc -nnginx 
```

Your output should be similar to the following, showing four services:

```output
NAME                    TYPE           CLUSTER-IP     EXTERNAL-IP     PORT(S)        AGE
nginx-amd-svc           LoadBalancer   10.0.67.234    20.4.5.6        80:30081/TCP   25m
nginx-arm-svc           LoadBalancer   10.0.89.145    20.7.8.9        80:30082/TCP   20m
nginx-intel-svc         LoadBalancer   10.0.45.123    20.1.2.3        80:30080/TCP   45m
nginx-multiarch-svc     LoadBalancer   10.0.123.456   20.10.11.12     80:30083/TCP   1m
```

3. Check which pods the multiarch service can route to:

```bash
kubectl get endpoints nginx-multiarch-svc -nnginx
```

You should see all three architecture pods listed as endpoints:

```output
NAME                  ENDPOINTS                                      AGE
nginx-multiarch-svc   10.244.0.217:80,10.244.1.177:80,10.244.2.68:80   1m
```

### Test the nginx multiarch service

4. Run the following to make HTTP requests to the multiarch nginx service:

```bash
./nginx_util.sh get multiarch
```

You get back the HTTP response from one of the available pods:

```output
Using service endpoint 20.10.11.12 for get on **multiarch service**
Response: <title>Welcome to nginx!</title>
Served by: nginx-**arm**-deployment-6f8d9c2a-def56
```

5. Run the command multiple times to see load balancing across architectures:

```bash
./nginx_util.sh get multiarch
./nginx_util.sh get multiarch
./nginx_util.sh get multiarch
```

The pod logs will show requests being served by different architecture deployments (intel, amd, or arm), demonstrating that the multiarch service distributes load across all available pods.

### Compare architecture-specific vs multiarch routing

Now you can compare the behavior:

- **Architecture-specific**: `./nginx_util.sh get intel` always routes to Intel pods
- **Architecture-specific**: `./nginx_util.sh get amd` always routes to AMD pods  
- **Architecture-specific**: `./nginx_util.sh get arm` always routes to ARM pods
- **Multiarch**: `./nginx_util.sh get multiarch` routes to any available pod

This multiarch service provides high availability and load distribution across your entire multi-architecture cluster.
