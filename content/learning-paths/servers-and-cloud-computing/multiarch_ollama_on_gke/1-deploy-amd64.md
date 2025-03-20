---
title: Deploy ollama amd64 to the cluster
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

Any easy way to experiment with Arm64 nodes in your K8s cluster is to deploy Arm64 nodes and pods alongside your existing amd64 node and pods. In this section of the tutorial, you'll bootstrap the cluster with ollama on amd64, to simulate an "existing" K8s cluster running ollama.

### Deployment and Service


1. Copy the following YAML, and save it to a file called *namespace.yaml*:

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: ollama
```

When the above is applied, a new K8s namespace named *ollama* will be created.  This is where all the K8s object created under this tutorial will live.

2. Copy the following YAML, and save it to a file called *amd64_ollama.yaml*:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ollama-amd64-deployment
  labels:
    app: ollama-multiarch
  namespace: ollama
spec:
  replicas: 1
  selector:
    matchLabels:
      arch: amd64
  template:
    metadata:
      labels:
        app: ollama-multiarch
        arch: amd64
    spec:
      nodeSelector:
        kubernetes.io/arch: amd64
      containers:
      - image: ollama/ollama:0.6.1
        name: ollama-multiarch
        ports:
        - containerPort: 11434
          name: http
          protocol: TCP
        volumeMounts:
        - mountPath: /root/.ollama
          name: ollama-data
      volumes:
      - emptyDir: {}
        name: ollama-data
---
apiVersion: v1
kind: Service
metadata:
  name: ollama-amd64-svc
  namespace: ollama
spec:
  sessionAffinity: None
  ports:
  - nodePort: 30668
    port: 80
    protocol: TCP
    targetPort: 11434
  selector:
    arch: amd64
  type: LoadBalancer
```

When the above is applied:

* A new Deployment called *ollama-amd64-deployment* is created.  This deployment pulls a multi-architectural (both amd64 and arm64) image [ollama image from Dockerhub](https://hub.docker.com/layers/ollama/ollama/0.6.1/images/sha256-28b909914d4e77c96b1c57dea199c60ec12c5050d08ed764d9c234ba2944be63).

Of particular interest is the *nodeSelector* *kubernetes.io/arch*, with the value of *amd64*.  This will ensure that this deployment only runs on amd64-based nodes, utilizing the amd64 version of the ollama container image. 

* A new load balancer Service *ollama-amd64-svc* is created, which targets all pods with the *arch: amd64* label (our amd64 deployment creates these pods.)

A *sessionAffinity* tag was added to this Service to remove sticky connections to the target pods; this removes persistent connections to the same pod on each request.

### Apply the amd64 Deployment and Service

1. Run the following command to apply the namespace, deployment, and service definitions:

```bash
kubectl apply -f namespace.yaml
kubectl apply -f amd64_ollama.yaml
```

You should get the following responses back:

```bash
namespace/ollama created
deployment.apps/ollama-amd64-deployment created
service/ollama-amd64-svc created
```
2. Optionally, set the *default Namespace* to *ollama* to help make those command lines quicker to type by entering the following:

```bash
config set-context --current --namespace=ollama
```

3. Get the status of the pods, and the services, by running the following:

```commandline
kubectl get pods,svc -nollama 
```

Your output should be similar to the following, showing three total services, and two total pods:

```commandline
$ kubectl get pods,svc -nollama

NAME                                           READY   STATUS    RESTARTS   AGE
pod/ollama-amd64-deployment-cbfc4b865-rf4p9    1/1     Running   0          86m

NAME                           TYPE           CLUSTER-IP       EXTERNAL-IP      PORT(S)        AGE
service/ollama-amd64-svc       LoadBalancer   1.2.3.4          104.154.81.229   80:30668/TCP   86m
```

When the pods show *Running* and the service shows a valid *External IP*, we're ready to test the ollama amd64 service!

### Test the ollama on amd64 web service 

4. Copy the following YAML, and save it to a file called *model_util.sh*:

```bash
TODO
```

5. Make it executable with the following command:

```bash
chmod 755 model_util.sh
```

This shell script conveniently bundles many test and logging commands into a single place, making it easy to test, troubleshoot, and view the services we expose in this tutorial. 

6. Run the following to make an HTTP request to the amd64 ollama service on port 80:

```commandline
./model_util.sh amd64 hello
```

You should get back the HTTP response, as well as the logline from the pod that served it:

```commandline
$ ./model_util.sh amd64 hello

Server response:
Ollama is running

Pod log output:
[pod/ollama-amd64-deployment-cbfc4b865-rf4p9/ollama-multiarch] 03:27:46
```

Congrats, you've successfully bootstrapped your GKE cluster with an amd64 node, running a Deployment with the ollama multi-architecture container instance!

Next, we'll do the same thing, but with an Arm node. 
