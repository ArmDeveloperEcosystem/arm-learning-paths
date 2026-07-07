---
title: Build and push the assistant image
description: Build the shopping assistant container image for arm64 and push it to Artifact Registry for deployment on Axion.
weight: 6
layout: "learningpathall"
---

## Build one Arm image for both Axion placements

Both the N4A and C4A node pools in this Learning Path use Arm-based Google Axion processors. You only need one `linux/arm64` assistant image, and that image can run in either placement.

{{% notice Note %}}
This is an Arm-targeted build for Axion, not a full multi-architecture build. A multi-architecture image is useful when the same tag must support non-Arm environments such as `linux/amd64`.
{{% /notice %}}

If you opened a new terminal, return to the source tree and restore the required variables:

```bash
cd "${HOME}/n4a-c4a/microservices-demo"

export PROJECT_ID="$(gcloud config get-value project)"
export ARTIFACT_REGION="us-central1"
export ARTIFACT_REPO="axion-workshop"
```

## Define the image name

Create one reusable image path:

```bash
export ASSISTANT_IMAGE_REPO="${ARTIFACT_REGION}-docker.pkg.dev/${PROJECT_ID}/${ARTIFACT_REPO}/shoppingassistantservice"
export ASSISTANT_IMAGE_TAG="lab-v1"
export ASSISTANT_IMAGE="${ASSISTANT_IMAGE_REPO}:${ASSISTANT_IMAGE_TAG}"

echo "${ASSISTANT_IMAGE}"
```

## Verify Docker and Buildx

Confirm that Docker and Buildx are available:

```bash
docker version
docker buildx version
```

If Docker is not running in your environment, start it before you continue.

## Configure Artifact Registry authentication

Configure Docker authentication for Artifact Registry:

```bash
gcloud auth configure-docker "${ARTIFACT_REGION}-docker.pkg.dev" --quiet
```

Cloud Shell might print a warning about existing credential helpers. You can continue if the command finishes successfully.

## Create a Buildx builder

Create or reuse a Buildx builder:

```bash
if docker buildx inspect axion-builder >/dev/null 2>&1; then
  docker buildx use axion-builder
else
  docker buildx create --name axion-builder --use
fi

docker buildx inspect --bootstrap
```

The output should show a working builder. Confirm that the `Platforms` line includes `linux/arm64` before you continue.

## Build and push the assistant image

Build the assistant image for `linux/arm64` and push it to Artifact Registry:

```bash
docker buildx build --platform linux/arm64 -t "${ASSISTANT_IMAGE}" --push src/shoppingassistantservice
```

The command packages the Flask assistant service, protobuf stubs, and Python dependencies. The important success signal is that the build finishes and pushes the image to your Artifact Registry path.

## Verify the pushed tag

List the tags for the assistant image:

```bash
gcloud artifacts docker tags list "${ASSISTANT_IMAGE_REPO}"
```

The output should include the `lab-v1` tag.

## What you've accomplished

You've built and published an Arm image for the shopping assistant. Kubernetes can now pull this image when you deploy the assistant on N4A.

Next, you'll create the N4A overlay and add the assistant to the running storefront.
