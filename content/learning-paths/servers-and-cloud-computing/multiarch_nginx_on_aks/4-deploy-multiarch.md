---
title: Deploy nginx multiarch service to the cluster
weight: 60

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Add multiarch service

You now have nginx running on Intel and ARM nodes with architecture-specific services. In this section, you'll create a multiarch service that can route to any available nginx pod regardless of architecture, providing load balancing across all architectures.

### Create the multiarch service

The multiarch service targets all pods with the `app: nginx-multiarch` label (all nginx deployments share this label). It uses `sessionAffinity: None` to ensure requests are distributed across all available pods without stickiness, and can route to Intel or ARM pods based on availability and load balancing algorithms.

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

Your output should be similar to the following, showing three services:

```output
NAME                  TYPE           CLUSTER-IP     EXTERNAL-IP     PORT(S)        AGE
nginx-arm-svc         LoadBalancer   10.0.241.154   48.192.64.197   80:30082/TCP   7m52s
nginx-intel-svc       LoadBalancer   10.0.226.250   20.80.128.191   80:30080/TCP   16m
nginx-multiarch-svc   LoadBalancer   10.0.40.169    20.99.208.140   80:30083/TCP   38s
```

3. Check which pods the multiarch service can route to:

```bash
kubectl get endpoints nginx-multiarch-svc -nnginx
```

You should see both architecture pods listed as endpoints:

```output
NAME                  ENDPOINTS                      AGE
nginx-multiarch-svc   10.244.0.21:80,10.244.1.1:80   47s
```

### Test the nginx multiarch service

4. Run the following to make HTTP requests to the multiarch nginx service:

```bash
./nginx_util.sh curl multiarch
```

You get back the HTTP response from one of the available pods:

```output
Using service endpoint 20.99.208.140 for curl on multiarch service
Response:
{
  "message": "nginx response",
  "timestamp": "2025-10-24T22:12:23+00:00",
  "server": "nginx-arm-deployment-5bf8df95db-wznff",
  "request_uri": "/"
}
Served by: nginx-arm-deployment-5bf8df95db-wznff
```

5. Run the command multiple times to see load balancing across architectures:

```bash
./nginx_util.sh curl multiarch
./nginx_util.sh curl multiarch
./nginx_util.sh curl multiarch
```

The responses will show requests being served by different architecture deployments (intel or arm), demonstrating that the multiarch service distributes load across all available pods.

### Compare architecture-specific vs multiarch routing

Now you can compare the behavior:

- **Architecture-specific**: `./nginx_util.sh curl intel` always routes to Intel pods
- **Architecture-specific**: `./nginx_util.sh curl arm` always routes to ARM pods
- **Multiarch**: `./nginx_util.sh curl multiarch` routes to any available pod

This multiarch service provides high availability and load distribution across your entire multi-architecture cluster.
