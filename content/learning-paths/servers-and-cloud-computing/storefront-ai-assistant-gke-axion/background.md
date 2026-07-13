---
title: Understand mixed placement for a storefront AI assistant
description: Learn why the storefront and assistant tiers use different Axion placements before you build and deploy the assistant.
weight: 2
layout: "learningpathall"
---

## How the application is organized

Modern AI applications often contain more than one workload shape. For example, a storefront is steady, service-oriented, and always on. An AI assistant is burstier and more latency-sensitive because it runs only when users ask for help.

This Learning Path uses that split in a live Online Boutique storefront on Google Kubernetes Engine (GKE). The storefront starts on N4A nodes powered by Google Axion processors and Arm Neoverse N3. You add the missing `shoppingassistantservice`, run it on N4A first, and then move only that assistant tier to C4A nodes powered by Google Axion and Arm Neoverse V2.

The goal isn't to prove that one Axion-based machine series replaces the other. You use N4A for the steady storefront tier and evaluate C4A for the AI reasoning tier so you can decide which machine series fits each workload.

![Architecture diagram showing the existing multi-architecture storefront image workflow and the final GKE placement on Axion. Core storefront services run on N4A, while the shopping assistant, Ollama sidecar, and Gemma model run together on C4A and call the live cart and catalog services.#center](images/mixed-placement-agentic-storefront-on-axion.webp "Mixed-placement agentic storefront on Axion")

The diagram shows the final mixed-placement pattern you build toward. Its left side summarizes the multi-architecture image publishing process used for the existing storefront images; you don't repeat that process here. The assistant image you build later targets only `linux/arm64` because both destination node pools are Arm-based. The right side shows the final placement: core services remain on N4A while the assistant, its Ollama sidecar, and the Gemma model move together to C4A.

## How the storefront already runs on Arm

The storefront baseline uses container images that can run on Arm nodes. A common way to publish portable container images is to use a multi-architecture image, which is one image reference that contains variants for more than one CPU architecture, such as `linux/amd64` and `linux/arm64`.

When Kubernetes schedules a pod that uses a multi-architecture image on an Arm node, the container runtime pulls the Arm-compatible variant from the same image reference. That is why the storefront can already run on Axion nodes before you build the assistant image.

This Learning Path starts with Arm-compatible storefront images already available. To learn the full build-and-publish workflow for multi-architecture images on GKE, see [Migrate x86 workloads to Arm on Google Kubernetes Engine with Axion processors](/learning-paths/servers-and-cloud-computing/gke-multi-arch-axion/).

One image reference can therefore contain an Arm-compatible variant. You confirm the storefront image reference from the source tree after you set up your tools and cluster access.

## How assistant requests flow

The `shoppingassistantservice` is the AI layer for the application. It runs as its own Kubernetes service and handles requests sent through the storefront frontend. When a shopper uses the assistant, the request follows this path:

1. The browser sends the request to `frontend`.
2. `frontend` forwards the request to `shoppingassistantservice`.
3. The assistant calls `productcatalogservice` or `cartservice` through its application tools.
4. The assistant sends the live storefront context to an Ollama sidecar in the same pod. The sidecar runs the `gemma3:1b-it-qat` model for the reasoning step.
5. The assistant returns the response through `frontend`.

The assistant is agentic because it does more than generate text. It uses application tools, keeps short-lived session state, and asks for confirmation before it calls `cartservice` to update the cart.

The `search_catalog` and `get_product_details` tools query the live catalog. The `get_cart` tool reads the current cart, while `add_to_cart` updates it only after user confirmation.

This design keeps the placement comparison focused. You don't add a separate vector database, retrieval pipeline, or hosted large language model API. When you move the assistant pod, you move the assistant logic and local reasoning runtime together as one AI tier.


In the next section, you'll set up environment variables, connect to the GKE cluster, and clone the source tree that contains the assistant implementation.
