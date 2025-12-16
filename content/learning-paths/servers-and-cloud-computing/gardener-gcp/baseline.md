---
title: Verify Gardener cluster health and functionality
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Verify your Gardener cluster is working

This section confirms that your Gardener Local setup is functioning correctly on an Arm-based Google Cloud C4A VM before running production workloads. You'll check cluster health, deploy test workloads, and validate networking.

## Set the kubeconfig environment variable

Configure kubectl to communicate with your Gardener cluster by setting the `KUBECONFIG` variable:

```console
export KUBECONFIG=$PWD/example/gardener-local/kind/local/kubeconfig
```

This tells kubectl where to find your cluster's authentication credentials.

## Check cluster health

Verify that your Gardener Local Kubernetes cluster is healthy by checking node and pod status:

```console
kubectl get nodes -o wide
kubectl get pods -A
```

The output is similar to:

```outputNAME                           STATUS   ROLES           AGE    VERSION   INTERNAL-IP   EXTERNAL-IP   OS-IMAGE
gardener-local-control-plane   Ready    control-plane   148m   v1.32.5   172.18.0.2    <none>        Debian GNU/Linux 12 (bookworm)
```

A `Ready` status indicates the control plane is healthy. You should also see numerous pods running across the `garden`, `kube-system`, `istio-system`, and `shoot--local--local` namespaces, confirming that all Gardener components are operational.

## Deploy a test nginx pod

Deploy a simple nginx pod to verify that workload deployment works correctly:

```console
kubectl run test-nginx --image=nginx --restart=Never
kubectl get pod test-nginx -w
```
- `kubectl run test-nginx` → Creates a single nginx pod.
- `kubectl get pod test-nginx -w` → Watches pod status in real time.

The output is similar to:

```output
>pod/test-nginx created
> kubectl get pod test-nginx -w
NAME         READY   STATUS              RESTARTS   AGE
test-nginx   0/1     ContainerCreating   0          0s
test-nginx   0/1     ContainerCreating   0          1s
test-nginx   1/1     Running             0          4s
```

When the pod reaches `Running` status, workload deployment is functioning. Press **Ctrl + C** to stop watching the pod.

## Create a service for the pod

Kubernetes services provide stable network endpoints for pods. Create a ClusterIP service to expose your nginx pod:

```console
kubectl expose pod test-nginx --port=80 --name=test-nginx-svc
kubectl get svc test-nginx-svc
```
- `kubectl expose pod` → Creates a ClusterIP service on port 80.
- `kubectl get svc` → Shows the service details.

The output is similar to:

```output
>service/test-nginx-svc exposed
> kubectl get svc test-nginx-svc
NAME             TYPE        CLUSTER-IP    EXTERNAL-IP   PORT(S)   AGE
test-nginx-svc   ClusterIP   10.2.194.17   <none>        80/TCP    9s
```

The assigned ClusterIP (such as `10.2.194.17`) confirms that Kubernetes service networking is functioning correctly.

## Test pod-to-service connectivity

Verify that one pod can communicate with another pod through a service by running curl inside a temporary pod:

```console
kubectl run curl --image=curlimages/curl -i --tty -- sh
```

Inside the pod shell, send an HTTP request to the nginx service:

```console
curl http://test-nginx-svc
```
Exit shell:

``` console
exit
```

The output is similar to:

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

Successful curl output confirms that pod-to-service networking is working correctly.

## Verify DNS resolution

Test DNS service discovery by running `nslookup` inside the curl pod:

If DNS resolves correctly, service discovery is healthy.

``` console
kubectl exec curl -- nslookup test-nginx-svc.default.svc.cluster.local
```

The output is similar to:

```output
Server:         10.2.0.10
Address:        10.2.0.10:53

Name:   test-nginx-svc.default.svc.cluster.local
Address: 10.2.194.17
```

Successful DNS resolution confirms that CoreDNS is functioning and service discovery is healthy.

## Check pod logs and command execution

Verify that you can access pod logs and execute commands inside containers:

```console
kubectl logs test-nginx | head
kubectl exec test-nginx -- nginx -v
```
- `kubectl logs` → Shows nginx pod logs.
- `kubectl exec` → Runs nginx -v inside the pod.

The output is similar to:

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

Pod logs and command execution working confirms that you can debug and troubleshoot workloads effectively.

## Clean up test resources

Remove the test pods and service to keep your cluster clean:

```console
kubectl delete pod test-nginx curl
kubectl delete svc test-nginx-svc
```

The output is similar to:

```output
pod "test-nginx" deleted from default namespace
pod "curl" deleted from default namespace
> kubectl delete svc test-nginx-svc
service "test-nginx-svc" deleted from default namespace
```
## Summary and what's next

After completing these steps, you have confirmed that the Kubernetes cluster and Gardener setup are healthy, core components are functioning correctly, pods start successfully, networking and services operate as expected, DNS resolution works, and the cluster is ready to run real workloads.
