---
title: Deploy nginx multiarch service on AKS
weight: 8

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Add a multi-architecture service to your cluster

You now have nginx running on Intel and Arm nodes with architecture-specific services. In this section, you'll create a multi-architecture service that can route to any available nginx pod regardless of architecture, providing load balancing across both architectures.

## Create the multiarch service

The multiarch service targets all pods with the `app: nginx-multiarch` label (all nginx deployments share this label). It uses `sessionAffinity: None` to ensure requests are distributed across all available pods without stickiness, and can route to Intel or Arm pods based on availability and load balancing algorithms.

Run the following commands to download and apply the multiarch service:

```bash
curl -sO https://raw.githubusercontent.com/geremyCohen/nginxOnAKS/main/multiarch_nginx.yaml
kubectl apply -f multiarch_nginx.yaml
```

You see the following response:

```output
service/nginx-multiarch-svc created
```

Next, get the status of all services by running:

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

Check which pods the multiarch service can route to:

```bash
kubectl get endpoints nginx-multiarch-svc -nnginx
```

You should see both architecture pods listed as endpoints:

```output
NAME                  ENDPOINTS                      AGE
nginx-multiarch-svc   10.244.0.21:80,10.244.1.1:80   47s
```

You are ready to test the multiarch service. 

## Test the nginx multiarch service

Run the following to make HTTP requests to the multiarch nginx service:

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

Run the command multiple times to see load balancing across architectures:

```bash
./nginx_util.sh curl multiarch
./nginx_util.sh curl multiarch
./nginx_util.sh curl multiarch
```

The responses will show requests being served by different architecture deployments (Intel or Arm), demonstrating that the multiarch service distributes the load across the available pods.

## Compare architecture-specific and multiarch routing

Now you can compare the behavior:

- The architecture-specific services provide predictable routing patterns. When you run `./nginx_util.sh curl intel`, your requests consistently reach Intel-based pods. Similarly, `./nginx_util.sh curl arm` ensures your traffic goes to Arm-based pods. 

- In contrast, the multiarch service distributes requests across all available pods regardless of architecture. This means `./nginx_util.sh curl multiarch` might connect you to either an Intel or Arm pod depending on current load and availability.


## What you've accomplished and what's next

Excellent work! You've successfully created a multi-architecture service that intelligently distributes traffic across both Arm and Intel pods. This unified service approach provides high availability and load distribution across your entire multi-architecture cluster, giving you the flexibility to leverage the strengths of different CPU architectures within a single Kubernetes environment.

You now have a complete multi-architecture deployment with three different service routing patterns: architecture-specific services for targeted testing, and a multiarch service for production-grade load balancing. You're ready to move on to performance monitoring and comparison.