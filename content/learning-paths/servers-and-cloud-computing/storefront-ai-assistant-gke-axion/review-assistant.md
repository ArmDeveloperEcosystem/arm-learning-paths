---
title: Review the shopping assistant implementation
description: Inspect the assistant source, tool functions, Dockerfile, and Kubernetes component before you build the image.
weight: 5
layout: "learningpathall"
---

## Inspect the assistant files

The source tree already contains the missing AI tier. Before you build it, review the files that make up the assistant:

```bash
find src/shoppingassistantservice -maxdepth 2 -type f | sort
find kustomize/components/shopping-assistant -maxdepth 2 -type f | sort
```

You should see the assistant source folder and the `shopping-assistant` Kustomize component.

{{% notice Note %}}
If you see a `__pycache__` directory, you can ignore it. Python creates that directory during local syntax checks.
{{% /notice %}}

## Review the runtime dependencies and gRPC stubs

The assistant uses a small Python runtime and generated gRPC stubs to call the live storefront services:

```bash
sed -n '1,20p' src/shoppingassistantservice/requirements.txt
sed -n '1,25p' src/shoppingassistantservice/demo_pb2.py
grep -nE 'class (CartServiceStub|ProductCatalogServiceStub)' \
  src/shoppingassistantservice/demo_pb2_grpc.py
```

The generated protobuf files are dense because they're machine-generated. You only need to confirm that the cart and product catalog stubs exist.

## Review the assistant service

Read the beginning and end of the assistant service:

```bash
sed -n '1,220p' src/shoppingassistantservice/shoppingassistantservice.py
tail -n 20 src/shoppingassistantservice/shoppingassistantservice.py
```

Focus on these parts of the file:

- Imports and environment variables
- Tool functions that call the live storefront services
- Request handlers that decide how the assistant responds
- The `app.run(...)` entrypoint

Highlight the tool functions:

```bash
grep -nE 'def (search_catalog|get_product_details|get_cart|add_to_cart|handle_[a-z_]+)' \
  src/shoppingassistantservice/shoppingassistantservice.py
```

These functions define the assistant behavior. The service searches the catalog, fetches product details, reads the cart, and updates the cart after confirmation. These are live application tool calls, not mock responses, which is what makes the assistant part of the storefront workflow.

## Confirm that the Python source is valid

Compile the assistant source:

```bash
python3 -m py_compile src/shoppingassistantservice/shoppingassistantservice.py
```

The command returns no output. Don't continue if this command fails.

## Review the container and Kubernetes component

Review the Dockerfile and the Kustomize component:

```bash
sed -n '1,80p' src/shoppingassistantservice/Dockerfile
sed -n '1,120p' kustomize/components/shopping-assistant/kustomization.yaml
sed -n '1,220p' kustomize/components/shopping-assistant/shoppingassistantservice.yaml
```

The Dockerfile packages the Python assistant service. The Kubernetes component creates `shoppingassistantservice`, adds the Ollama sidecar, and patches `frontend` so the assistant becomes part of the storefront experience. Because the assistant and Ollama run in the same pod, moving this deployment later moves the AI logic and local reasoning runtime together.

## What you've accomplished and what's next

You've now reviewed the source code, service contracts, container packaging, and Kubernetes component for the assistant tier.

Next, you'll build the assistant image for `linux/arm64` and push it to Artifact Registry.
