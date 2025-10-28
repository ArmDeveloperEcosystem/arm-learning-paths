---
title:  Automate builds and rollout with Cloud Build & Skaffold
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

Google [**Cloud Build**](https://cloud.google.com/build/docs/set-up) is a managed CI/CD service that runs your containerized build and deploy steps in isolated runners. In this page you'll automate the flow you performed manually: **build multi-arch images, deploy to GKE on amd64, then migrate to arm64**, and print the app's external IP.

## What this pipeline does
- Authenticates Docker to **Artifact Registry**.
- Builds and pushes **amd64 + arm64** images with **Docker Buildx** (QEMU enabled in the runner).
- Connects to your **GKE** cluster.
- Applies the **amd64** Kustomize overlay, verifies pods, then applies the **arm64** overlay and verifies again.
- Prints the **frontend-external** LoadBalancer IP at the end. 


{{% notice Tip %}}
Run this from the **microservices-demo** repo root in **Cloud Shell**. Ensure you completed earlier pages (GAR created, images path/tag decided, GKE cluster with amd64 + arm64 node pools, and Kustomize overlays present).
{{% /notice %}}

## Grant IAM to the Cloud Build service account
Cloud Build runs as a per-project service account: `<PROJECT_NUMBER>@cloudbuild.gserviceaccount.com`. Grant it the minimal roles needed to build, push, log, and interact with GKE.

```bash
# Uses env vars set earlier: PROJECT_ID, REGION, CLUSTER_NAME, GAR
PROJECT_NUMBER="$(gcloud projects describe "${PROJECT_ID}" --format='value(projectNumber)')"
CLOUD_BUILD_SA="${PROJECT_NUMBER}@cloudbuild.gserviceaccount.com"

gcloud projects add-iam-policy-binding "${PROJECT_ID}" \
  --member="serviceAccount:${CLOUD_BUILD_SA}" \
  --role="roles/cloudbuild.builds.builder"

gcloud projects add-iam-policy-binding "${PROJECT_ID}" \
  --member="serviceAccount:${CLOUD_BUILD_SA}" \
  --role="roles/container.developer"

gcloud projects add-iam-policy-binding "${PROJECT_ID}" \
  --member="serviceAccount:${CLOUD_BUILD_SA}" \
  --role="roles/artifactregistry.writer"

gcloud projects add-iam-policy-binding "${PROJECT_ID}" \
  --member="serviceAccount:${CLOUD_BUILD_SA}" \
  --role="roles/logging.logWriter"
```

## Update skaffold.yaml for deploy-only

This will let Cloud Build handle image builds and use Skaffold only to apply the Kustomize overlays.

```yaml
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

```

##  Create cloudbuild.yaml

This pipeline installs `Docker + Buildx` in the runner, enables QEMU, builds two services as examples (extend as desired), connects to your cluster, deploys to amd64, verifies, migrates to arm64, verifies, and prints the external IP.  ￼

```yaml
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
          src/cartservice --push

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
        echo "Open http://${IP} in your browser."
```

{{% notice Note %}}
In production, add one build step per microservice (or a loop) and enable caching. The example above builds two images for brevity, mirroring the manual steps you completed earlier.  ￼
{{% /notice %}}

## Run the pipeline

From the repo root:

```bash
gcloud builds submit --config=cloudbuild.yaml --substitutions=_CLUSTER="${CLUSTER_NAME}",_REGION="${REGION}",_REPO="${GAR}"
```

The final step prints in the build description:

```
Open http://<EXTERNAL-IP> in your browser.
```

Open that URL to load the storefront and confirm the full build - deploy - migrate flow is automated.
