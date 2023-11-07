---
title: Build and deploy a multi-arch application on Amazon EKS
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Multi-architecture Amazon EKS cluster with x86 and Arm-based (Graviton) nodes

A multi-architecture Kubernetes cluster runs workloads on multiple hardware architectures, typically arm64 and amd64. To learn more about multi-architecture Kubernetes, you can create a hybrid cluster in Amazon EKS and gain some practical experience with arm64 and amd64 nodes. This will also help you understand multi-architecture container images.

## Before you begin

You will need an [AWS account](https://aws.amazon.com/). Create an account if needed. 

Three tools are required on your local machine. Follow the links to install the required tools.

* [Kubectl](/install-guides/kubectl/)
* [Amazon eksctl CLI](/install-guides/eksctl)
* [Docker](/install-guides/docker)

## Create a multi-architecture Amazon EKS Cluster

Use `eksctl` to create a multi-architecture Amazon EKS cluster. Create a file named `cluster.yaml` with the contents below using a file editor of your choice.

```yaml
apiVersion: eksctl.io/v1alpha5
kind: ClusterConfig

metadata:
  name: multi-arch-cluster
  region: us-east-1

nodeGroups:
  - name: x86-node-group
    instanceType: m5.large
    desiredCapacity: 2
    volumeSize: 80
  - name: arm64-node-group
    instanceType: m6g.large
    desiredCapacity: 2
    volumeSize: 80
```

Run the `eksctl` command to create the EKS cluster:

```console
eksctl create cluster -f cluster.yaml
```
This command will create a cluster that has 2 x86/amd64 nodes and 2 arm64 nodes. When the cluster is ready, use the following command to check the nodes:

```console
kubectl get nodes
```
The output should look similar to:

```output
NAME                                          STATUS   ROLES    AGE     VERSION
ip-172-31-10-206.eu-west-1.compute.internal   Ready    <none>   9m56s   v1.28.1-eks-43840fb
ip-172-31-16-133.eu-west-1.compute.internal   Ready    <none>   9m59s   v1.28.1-eks-43840fb
ip-172-31-19-140.eu-west-1.compute.internal   Ready    <none>   8m32s   v1.28.1-eks-43840fb
ip-172-31-40-45.eu-west-1.compute.internal    Ready    <none>   8m32s   v1.28.1-eks-43840fb
```
To check the architecture of the nodes, execute the following command:

```console
kubectl get node -o jsonpath='{.items[*].status.nodeInfo.architecture}'
```
The output should show two architectures for four nodes:

```output
arm64 amd64 amd64 arm64
```

## Multi-architecture containers

Multi-architecture container images are the easiest way to deploy applications and hide the underlying hardware architecture. Building multi-architecture images is slightly more complex compared to building single-architecture images. 
Docker provides two ways to create multi-architecture images:
  * docker buildx - builds both architectures at the same time.
  * docker manifest - builds each architecture separately and joins them together into a multi-architecture image.

Shown below is a simple `Go` application you can use to learn about multi-architecture Kubernetes clusters. Create a file named `hello.go` with the contents below:

```console
package main

import (
    "fmt"
    "log"
    "net/http"
    "os"
    "runtime"
)

func handler(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintf(w, "Hello from image NODE:%s, POD:%s, CPU PLATFORM:%s/%s",
        os.Getenv("NODE_NAME"), os.Getenv("POD_NAME"), runtime.GOOS, runtime.GOARCH)
}

func main() {
    http.HandleFunc("/", handler)
    log.Fatal(http.ListenAndServe(":8080", nil))
}
```
Create another file named `go.mod` with the following content:

```console
module example.com/arm
go 1.21
```

Create a Dockerfile with the following content:

```console
ARG T

#
# Build: 1st stage
#
FROM golang:1.21-alpine as builder 
ARG TARCH
WORKDIR /app
COPY go.mod .
COPY hello.go .
RUN GOARCH=${TARCH} go build -o /hello && \
    apk add --update --no-cache file && \
    file /hello   

#
# Release: 2nd stage
#
FROM ${T}alpine
WORKDIR /
COPY --from=builder /hello /hello
RUN apk add --update --no-cache file
CMD [ "/hello" ]
```

## Build multi-architecture docker images with docker buildx

With these files you can build your docker image. Log in to Amazon ECR and create a repository named `multi-arch-app`.

Run the following command to build and push the docker image to the repository:

```console
docker buildx create --name multiarch --use --bootstrap
docker buildx build -t <your-docker-repo-path>/multi-arch:latest --platform linux/amd64,linux/arm64 --push .
```
Replace `<your-docker-repo-path>` in the command above to the location of your repository.

You should now see the docker image in your repository.

## Build multi-architecture docker images with docker manifest

You can also use docker manifest to create a multi-architecture image from two single-architecture images. 
Create another repository in Amazon ECR with the name `multi-arch-demo`. Use the following command to build an amd64 image:

```console
docker build build -t <your-docker-repo-path>/multi-arch-demo:amd64 --build-arg TARCH=amd64 --build-arg T=amd64/ .
docker push <your-docker-repo-path>/multi-arch-demo:amd64
```
Replace `<your-docker-repo-path>` in the command above to the location of your repository.

Build an arm64 image by executing the following commands on an arm64 machine:
```console
docker build build -t <your-docker-repo-path>/multi-arch-demo:arm64 --build-arg TARCH=amd64 --build-arg T=amd64v8/ .
docker push <your-docker-repo-path>/multi-arch-demo:arm64
```
Again, replace `<your-docker-repo-path>` in the commands above to the location of your repository.

After building individual containers for each architecture, merge them into a single image by running the commands below on either architecture:

```console
docker manifest create <your-docker-repo-path>/multi-arch-demo:latest \
--amend <your-docker-repo-path>/multi-arch-demo:arm64 \
--amend <your-docker-repo-path>/multi-arch-demo:amd64
docker manifest push --purge <your-docker-repo-path>/multi-arch-demo:latest
```

You should see three images in the ECR repository - one for each architecture (amd64 and arm64) and a combined multi-architecture image.

## Deploy Kubernetes service in EKS cluster

You can now create a service to deploy the application. Create a file named `hello-service.yaml` with the following contents:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: hello-service
  labels:
    app: hello
    tier: web
spec:
  type: LoadBalancer
  ports:
    - port: 80
      targetPort: 8080
  selector:
    app: hello
    tier: web
```

Deploy the service and run the following command:

```console
kubectl apply -f hello-service.yaml
```

## Deploy amd64 application

Create a text file named `amd64-deployment.yaml` with the contents below. The amd64 image will only run on amd64 nodes. The nodeSelector is used to make sure the container is only scheduled on amd64 nodes. 

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: amd-deployment
  labels:
    app: hello
spec:
  replicas: 1
  selector:
    matchLabels:
      app: hello
      tier: web
  template:
    metadata:
      labels:
        app: hello
        tier: web
    spec:
      containers:
      - name: hello
        image: <your-docker-repo-path>/multi-arch-demo:amd64
        imagePullPolicy: Always
        ports:
          - containerPort: 8080
        env:
          - name: NODE_NAME
            valueFrom:
              fieldRef:
                fieldPath: spec.nodeName
          - name: POD_NAME
            valueFrom:
              fieldRef:
                fieldPath: metadata.name
        resources:
          requests:
            cpu: 300m
      nodeSelector:
        kubernetes.io/arch: amd64

```

Use the following command to deploy the application:

```console
kubectl apply -f amd64-deployment.yaml
```
The output should show a single pod running.

Get the external IP assigned to the service you deployed earlier, by executing the following command:

```console
kubectl get svc
```
Use the `external-ip` from the command output and execute the following command (this IP belongs to the Load Balancer provisioned in your cluster):

```console
curl -w '\n' http://<external_ip>
```
You should now see an output similar to what's shown below:

```output
Hello from image NODE:ip-192-168-32-244.ec2.internal, POD:amd-deployment-7d4d44889d-vzhpd, CPU PLATFORM:linux/amd64
```

## Deploy arm64 application

Create a text file named `arm64-deployment.yaml` with the contents below. Note that the value of `nodeSelector` is now arm64.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: arm-deployment
  labels:
    app: hello
spec:
  replicas: 1
  selector:
    matchLabels:
      app: hello
      tier: web
  template:
    metadata:
      labels:
        app: hello
        tier: web
    spec:
      containers:
      - name: hello
        image: <your-docker-repo-path>/multi-arch-demo:arm64
        imagePullPolicy: Always
        ports:
          - containerPort: 8080
        env:
          - name: NODE_NAME
            valueFrom:
              fieldRef:
                fieldPath: spec.nodeName
          - name: POD_NAME
            valueFrom:
              fieldRef:
                fieldPath: metadata.name
        resources:
          requests:
            cpu: 300m
      nodeSelector:
        kubernetes.io/arch: arm64
```

Deploy the arm64 application by using the command below:

```console
kubectl apply -f arm64-deployment.yaml
```

Execute the following command to check the running pods:

```console
kubectl get pods
```
You should now see two pods running in the cluster, one for amd64 and another one for arm64.

Execute the curl command a few times to see output from both the pods; you should see responses from both the arm64 and amd64 pods.

```console
curl -w '\n' http://<external_ip>
```

## Deploy multi-architecture application in EKS cluster

You can now deploy the multi-architecture version of the application in EKS cluster. Create a text file named `multi-arch-deployment.yaml` with the contents below. The image is the multi-architecture image created with docker buildx and 6 replicas are specified.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: multi-arch-deployment
  labels:
    app: hello
spec:
  replicas: 6
  selector:
    matchLabels:
      app: hello
      tier: web
  template:
    metadata:
      labels:
        app: hello
        tier: web
    spec:
      containers:
      - name: hello
        image: <your-docker-repo-path>/multi-arch:latest
        imagePullPolicy: Always
        ports:
          - containerPort: 8080
        env:
          - name: NODE_NAME
            valueFrom:
              fieldRef:
                fieldPath: spec.nodeName
          - name: POD_NAME
            valueFrom:
              fieldRef:
                fieldPath: metadata.name
        resources:
          requests:
            cpu: 300m
```
Deploy the multi-architecture application by using the command below:

```console
kubectl apply -f multi-arch-deployment.yaml
```
Execute the following command to check the running pods:

```console
kubectl get pods
```
The output should show all the pods from three deployments. To test the application, run the following command to check messages from all three versions of the application:

```console
for i in $(seq 1 10); do curl -w '\n' http://<external_ip>; done
```
The output will show a variety of arm64 and amd64 messages.

You have now deployed an x86/amd64, arm64 and multi-architecture version of the same application in a single Amazon EKS cluster. Leverage these techniques to incrementally migrate your existing x86/amd64 based applications to arm64 in AWS.
