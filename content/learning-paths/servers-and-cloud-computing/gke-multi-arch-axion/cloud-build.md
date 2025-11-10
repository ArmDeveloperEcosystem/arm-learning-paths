---
title: Automate builds and rollout with Cloud Build and Skaffold
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

Google [**Cloud Build**](https://cloud.google.com/build/docs/set-up) is a managed CI/CD service that runs your containerized build and deploy steps in isolated runners. 

In this section, you'll automate the flow you performed manually: build multi-arch images, deploy to GKE on amd64, then migrate to arm64, and print the app's external IP.

## What does this pipeline do?

The pipeline performs the following steps:

- Authenticates Docker to your Artifact Registry
- Builds and pushes amd64 and arm64 images with Docker Buildx, with QEMU enabled in the runner
- Connects to your GKE cluster
- Applies the amd64 Kustomize overlay, verifies pods, then applies the arm64 overlay and verifies pods again
- Prints the frontend-external LoadBalancer IP at the end

{{% notice Tip %}}
Run this from the microservices-demo repo root in Cloud Shell. Ensure you completed the previous steps. 
{{% /notice %}}

## Grant IAM permission to the Cloud Build service account

Cloud Build runs as a per-project service account: `<PROJECT_NUMBER>@cloudbuild.gserviceaccount.com`. Grant it the minimal roles needed to build, push, log, and interact with GKE.

Grant the required roles:

```bash
# Uses env vars set earlier: PROJECT_ID, REGION, CLUSTER_NAME, GAR
PROJECT_NUMBER="$(gcloud projects describe "${PROJECT_ID}" --format='value(projectNumber)')"
CLOUD_BUILD_SA="${PROJECT_NUMBER}@cloudbuild.gserviceaccount.com"

gcloud projects add-iam-policy-binding "${PROJECT_ID}" --member="serviceAccount:${CLOUD_BUILD_SA}" --role="roles/cloudbuild.builds.builder" --condition=None --quiet

gcloud projects add-iam-policy-binding "${PROJECT_ID}" --member="serviceAccount:${CLOUD_BUILD_SA}" --role="roles/container.developer" --condition=None --quiet

gcloud projects add-iam-policy-binding "${PROJECT_ID}" --member="serviceAccount:${CLOUD_BUILD_SA}" --role="roles/artifactregistry.writer" --condition=None --quiet

gcloud projects add-iam-policy-binding "${PROJECT_ID}" --member="serviceAccount:${CLOUD_BUILD_SA}" --role="roles/logging.logWriter" --condition=None --quiet
```

## Update the Skaffold configuration

Create a `skaffold.yaml` file for Cloud Build. This lets Cloud Build handle image builds and uses Skaffold only to apply the Kustomize overlays.

Create the configuration:

```yaml
# From the repo root (microservices-demo)
[ -f skaffold.yaml ] && cp skaffold.yaml "skaffold.yaml.bak.$(date +%s)"
cat > skaffold.yaml <<'YAML'

# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

apiVersion: skaffold/v3
kind: Config
metadata:
  name: app
manifests:
  kustomize:
    paths:
      - kustomize/base
deploy:
  kubectl: {}
profiles:
- name: deploy-amd
  patches:
  - op: replace
    path: /manifests/kustomize/paths/0
    value: kustomize/overlays/amd64
- name: migrate-arm
  patches:
  - op: replace
    path: /manifests/kustomize/paths/0
    value: kustomize/overlays/arm64
---
apiVersion: skaffold/v3
kind: Config
metadata:
  name: loadgenerator
requires:
- configs: [app]
manifests:
  rawYaml:
    - ./kubernetes-manifests/loadgenerator.yaml
deploy:
  kubectl: {}
YAML

```

## Create a YAML file for Cloud Build 

This pipeline installs Docker with Buildx in the runner, enables QEMU, builds two services as examples (extend as desired), connects to your cluster, deploys to amd64, verifies, migrates to arm64, verifies, and prints the external IP.  ￼

Run the commands to create the `cloudbuild.yaml` file.

```yaml
cat > cloudbuild.yaml <<'YAML'

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START cloudbuild_microservice_demo_cloudbuild]

# This configuration file is used to build and deploy the app into a
# GKE cluster using Google Cloud Build.
#
# PREREQUISITES:
# - Cloud Build service account must have role: "Kubernetes Engine Developer"

# USAGE:
# GCP zone and GKE target cluster must be specified as substitutions
# Example invocation:
# `gcloud builds submit --config=cloudbuild.yaml --substitutions=_ZONE=us-central1-b,_CLUSTER=demo-app-staging .`

substitutions:
  _REGION: ${REGION}
  _CLUSTER: ${CLUSTER_NAME}
  _REPO: ${GAR}

options:
  machineType: "N1_HIGHCPU_8"
  logging: CLOUD_LOGGING_ONLY
timeout: "7200s"

steps:
  # 1) Authenticate Docker to Artifact Registry
  - name: gcr.io/google.com/cloudsdktool/cloud-sdk
    entrypoint: bash
    args:
      - -ceu
      - |
        echo "Auth to GAR..."
        gcloud auth configure-docker "$(echo "${_REPO}" | awk -F/ '{print $1}')" --quiet

  # 2) Build and push multi-arch images (examples: adservice, cartservice)
  - name: gcr.io/google.com/cloudsdktool/google-cloud-cli:stable
    entrypoint: bash
    env:
      - DOCKER_BUILDKIT=1
      - CLOUDSDK_CORE_DISABLE_PROMPTS=1
    args:
      - -ceu
      - |
        apt-get update && apt-get install -y docker.io curl
        mkdir -p ~/.docker/cli-plugins/
        curl -sSL https://github.com/docker/buildx/releases/download/v0.14.0/buildx-v0.14.0.linux-amd64 \
          -o ~/.docker/cli-plugins/docker-buildx
        chmod +x ~/.docker/cli-plugins/docker-buildx

        # Start Docker daemon in the runner
        dockerd > /var/log/dockerd.log 2>&1 &
        timeout 30 sh -c 'until docker info >/dev/null 2>&1; do sleep 1; done'

        # Enable QEMU for cross-arch builds and create builder
        docker run --privileged --rm tonistiigi/binfmt --install all
        docker buildx create --name multi --use || true
        docker buildx inspect --bootstrap

        # Build and push multi-arch images
        docker buildx build --platform linux/amd64,linux/arm64 \
          -t "${_REPO}/adservice:v1" \
          src/adservice --push

        docker buildx build --platform linux/amd64,linux/arm64 \
          -t "${_REPO}/cartservice:v1" \
          src/cartservice/src --push

  # 3) Connect kubectl to the target cluster
  - name: gcr.io/google.com/cloudsdktool/cloud-sdk:slim
    entrypoint: bash
    args:
      - -ceu
      - |
        gcloud container clusters get-credentials "${_CLUSTER}" --region "${_REGION}"

  # 4) Deploy to amd64 node pool
  - name: gcr.io/k8s-skaffold/skaffold:v2.16.1
    id: deploy-amd
    entrypoint: bash
    args:
      - -ceu
      - |
        skaffold deploy --filename=skaffold.yaml --config loadgenerator -p deploy-amd

  # 5) Verify pods on amd64
  - name: gcr.io/google.com/cloudsdktool/cloud-sdk:latest
    entrypoint: bash
    args:
      - -ceu
      - |
        echo "Pods on amd64:"
        kubectl get pods -o wide

  # 6) Migrate to arm64 node pool
  - name: gcr.io/k8s-skaffold/skaffold:v2.16.1
    id: migrate-arm
    entrypoint: bash
    args:
      - -ceu
      - |
        skaffold deploy --filename=skaffold.yaml --config loadgenerator -p migrate-arm

  # 7) Verify pods on arm64 and print the external IP
  - name: gcr.io/google.com/cloudsdktool/cloud-sdk:latest
    entrypoint: bash
    args:
      - -ceu
      - |
        echo "Pods on arm64:"
        kubectl get pods -o wide
        echo "Fetching external IP for the frontend service..."
        IP=$(kubectl get svc frontend-external -o=jsonpath='{.status.loadBalancer.ingress[0].ip}')
        echo "Open http://$${IP} in your browser."
YAML
```

{{% notice Note %}}
In production, add one build step per microservice (or a loop) and enable caching. The example above builds two images for brevity, mirroring the manual steps you completed earlier.  ￼
{{% /notice %}}

## Run the pipeline

Submit the build from the root of the repository: 

```bash
gcloud builds submit --config=cloudbuild.yaml --substitutions=_CLUSTER="${CLUSTER_NAME}",_REGION="${REGION}",_REPO="${GAR}"
```

The final step prints in the build description:

```
Open http://<EXTERNAL-IP> in your browser.
```

Open the URL to load the storefront and confirm the full build, deploy, and migrate flow is automated:
![Storefront reachable after Cloud Build deploy/migrate (arm64) #center](images/storefront-running-on-Google-Axion.jpeg "Storefront after Cloud Build automation on Axion (arm64)")
