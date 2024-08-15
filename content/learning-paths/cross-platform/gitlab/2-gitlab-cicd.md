---
title: Automate the build and deployment of a multi-arch application with GitLab CI/CD
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is a multi-architecture application?
A multi-architecture application is designed to run on multiple architectures, typically arm64 and amd64. The two common ways to build a containerized multi-architecture application is using `docker buildx` and `docker manifest`. 
 - `docker buildx` builds a multi-architecture application at the same time using emulation.
 - `docker manifest` joins two different architecture images into a single multi-architecture image.

In this learning path you will use the `docker manifest` way to build a multi-architecture image.

## Create a Docker repository in Google Artifact Registry
You can create a Docker repository in the Google Artifact Registry from the Google Cloud UI or with the following command:

```console
gcloud artifacts repositories create quickstart-docker-repo --repository-format=docker \
    --location=us-central1 --description="Docker repository" \
    --project=<your-project-id>
```
Replace `<your-project-id>` in the command above with your project id in Google Cloud where you want the create the repository.

Configure the cli to authenticate the docker repository in the Artifact Registry:

```console
gcloud auth configure-docker us-central1-docker.pkg.dev
```

## Create project variables

Create the following variables in your GitLab repository by navigating to `CI/CD->Variables`. Expand the section and click on `Add Variable`.

- `GCP_PROJECT` - Your Google Cloud project ID that also hosts the Google Artifact registry
- `GKE_ZONE` - Zone for your GKE cluster - e.g. - us-central1-c
- `GKE_CLUSTER` - Name of your GKE cluster

## Create files in GitLab repository

In your GitLab repository, create the following files:

1. `hello.go` - A simple `Go` application that prints the architecture of the VM it runs on
2. `go.mod` - Defines the `Go` module to use for the application
3. `Dockerfile` - A multi-stage Dockerfile for the application that accepts CPU ARCH as arguments
4. `deployment.yaml` - The kubernetes deployment file that creates a deployment with multiple replicas of the application
5. `hello-service.yaml` - Kubernetes yaml file that creates a Service of type LoadBalancer for accessing the application

Create `hello.go` with the contents below:
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
Create `go.mod` with the following content:

```console
module example.com/arm
go 1.21
```

The `Dockerfile` with the following content:

```dockerfile
ARG T

#
# Build: 1st stage
#
FROM golang:1.21-alpine AS builder 
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

The `deployment.yaml` file references the multi-architecture docker image from the registry. Create the file using the contents below.
```yml
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
        image: us-central1-docker.pkg.dev/$GCP_PROJECT/multi-arch-demo/demo-image:latest
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
Create a Kubernetes Service of type `LoadBalancer` with the following `hello-service.yaml` contents:

```yml
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

## Automate the GitLab CI/CD build process 

In this section, the individual Docker images for each architecture - `amd64` and `arm64`- are built natively on their respective runner. For example, the `arm64` build is run on Google Axion runner and vice versa. Each runner is differentiated with `tags` in the pipeline. To build a CI/CD pipeline in GitLab, you'll need to create a `.gitlab-ci.yml` file in your repository. Use the following contents to populate the file:

```yml
workflow:
  rules:
    - if: '$CI_PIPELINE_SOURCE == "web"'
      when: always
    - when: never

stages:
  - build
  - manifest
  - deploy

arm64-build:
  stage: build
  tags:
    - arm64
  script:
    - echo "Building Arm64 Docker image"
    - gcloud auth configure-docker us-central1-docker.pkg.dev
    - docker build -t us-central1-docker.pkg.dev/$GCP_PROJECT/multi-arch-demo/demo-image:arm64 --build-arg TARCH=arm64 --build-arg T=arm64v8/ .
    - docker push us-central1-docker.pkg.dev/$GCP_PROJECT/multi-arch-demo/demo-image:arm64

amd64-build:
  stage: build
  tags:
    - amd64
  script:
    - echo "Building x86/amd64 Docker image"
    - gcloud auth configure-docker us-central1-docker.pkg.dev
    - docker build -t us-central1-docker.pkg.dev/$GCP_PROJECT/multi-arch-demo/demo-image:amd64 --build-arg TARCH=amd64 --build-arg T=amd64/ .
    - docker push us-central1-docker.pkg.dev/$GCP_PROJECT/multi-arch-demo/demo-image:amd64

manifest:
  stage: manifest
  tags:
    - arm64
  script:
    - echo "Creating single multi-architecture image"
    - docker manifest create us-central1-docker.pkg.dev/$GCP_PROJECT/multi-arch-demo/demo-image:latest \
      --amend us-central1-docker.pkg.dev/$GCP_PROJECT/multi-arch-demo/demo-image:arm64 \
      --amend us-central1-docker.pkg.dev/$GCP_PROJECT/multi-arch-demo/demo-image:amd64
    - docker manifest push --purge us-central1-docker.pkg.dev/$GCP_PROJECT/multi-arch-demo/demo-image:latest

deploy:
  stage: deploy
  tags:
    - arm64
  script:
    - echo "Deploying multi-architecture application to GKE"
    - gcloud container clusters get-credentials $GKE_CLUSTER --zone $GKE_ZONE --project $GCP_PROJECT
    - kubectl apply -f hello-service.yaml
    - kubectl apply -f deployment.yaml

```
This file has three `stages`. A `stage` is a set of commands that are executed in a sequence to achieve the desired result. In the `build` stage of the file there are two jobs that run in parallel. The `arm64-build` job gets executed on the Google Axion based C4A runner and the `amd64-build` job gets executed on an AMD64 based E2 runner. Both of these jobs push a Docker image to the registry. 

In the `manifest` stage, using `docker manifest` command both of these images are joined to create a single multi-architecture image and pushed to the registry. 

In the `deploy` stage, this multi-architecture image is deployed on a hybrid GKE cluster - with both `arm64` and `amd64` nodes. 

## Execute the GitLab CI/CD multi-architecture pipeline

To execute the pipeline in GitLab, navigate to `Build->Pipelines` and click on `Run pipeline`. Once the pipeline completes, you should see an arm64, amd64 and a multi-architecture image in Google Artifacts Registry. 

Note:
If you see the following error after executing the pipeline - 
```output
gitlab job error: job failed: prepare environment: exit status 1. check https://docs.gitlab.com/runner/shells/index.html#shell-profile-loading for more information
```
SSH to the runner VM and execute the following command

```console
sudo vi /home/gitlab-runner/.bash_logout
```
Comment all the lines in that file, save and exit. Re-run the pipeline again.
