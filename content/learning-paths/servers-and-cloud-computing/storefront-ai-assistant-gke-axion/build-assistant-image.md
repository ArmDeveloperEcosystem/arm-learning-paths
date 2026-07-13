---
title: Build and push the assistant image
description: Build the shopping assistant container image for arm64 and push it to Artifact Registry for deployment on Axion.
weight: 6
layout: "learningpathall"
---

## Build one Arm image for both Axion placements

You need only one `linux/arm64` assistant image for both the N4A and C4A pools, and that image can run in either placement.

{{% notice Note %}}
This is an Arm-targeted build for Axion, not a full multi-architecture build. A multi-architecture image is useful when the same tag must support non-Arm environments such as `linux/amd64`.
{{% /notice %}}

If you opened a new terminal, return to the source tree and restore the required variables:

```bash
source "${HOME}/.storefront-axion-env"
cd "${REPO}"
```

## Confirm the image name

Confirm the reusable image path you configured during setup:

```bash
echo "${ASSISTANT_IMAGE}"
```

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

The output includes the `lab-v1` tag.

## What you've accomplished and what's next

You've now built and published an Arm image for the shopping assistant. Kubernetes can now pull this image when you deploy the assistant on N4A.

Next, you'll create the N4A overlay and add the assistant to the running storefront.
