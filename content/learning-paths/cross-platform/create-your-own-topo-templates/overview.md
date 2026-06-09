---
title: What are Topo Templates?
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Before you begin

[Topo](https://github.com/arm/topo) is an open-source command-line tool developed by Arm used to deploy projects to an Arm-based Linux target over SSH. Topo builds container images on the host, transfers them to the target, and starts the services on the target. Topo can also build and deploy directly on the target.

Before getting started, you should complete the Learning Path [Deploy containerized workloads to Arm-based Linux targets with Topo](/learning-paths/cross-platform/deploy-containerized-workloads-with-topo/) to learn about Topo, why to use it, how to install it and how to use it for target inspection, listing Templates and deployment.

We now assume that you have Topo installed on your host machine and that you have an Arm-based Linux target available over SSH. Use the same target pattern from the previous Learning Path, for example a Raspberry Pi, an AWS Arm instance, or another Arm-based Linux system:

```bash
--target user@my-target
```

If your host machine is also a Linux target, you can use `--target localhost`.

## What is a Topo Template?

A Topo Template is a containerized sample project for Arm-based Linux systems. At minimum, it is a directory containing a `compose.yaml`, Dockerfiles, and source code, with an `x-topo` metadata block that describes what the Template does, what hardware features it requires, and what parameters a user can configure.

The [Topo Template Format Specification](https://github.com/arm/topo-template-format) is based on the [Compose Specification](https://github.com/compose-spec/compose-spec), extended with `x-topo` metadata that describes requirements such as CPU features and build arguments. The Compose Specification is a standard, YAML-based format for describing multi-container applications. Instead of starting containers individually, you define all services, images, connections, and configuration in a single `compose.yaml` file.

In this Learning Path, you'll learn how to create and modify your own Topo Template.

## Where can I find Topo Templates?

The Topo Templates specification is an open specification. Anyone can publish their own Topo Templates and any tool can read and act on `x-topo` metadata to discover, validate, and deploy Templates.

A curated list of example Templates can be found either via:

1. The Topo Templates command, used in the prior Learning Path.

```bash
topo templates --target user@my-target
```

2. The [Topo Catalog](https://github.com/arm/topo/blob/main/internal/catalog/data/catalog.json).

If you create your own Template, you can [Propose Your Template to Topo](https://github.com/arm/topo-template-format#propose-your-template-to-topo), by following the instructions at the link.

## Why create a Topo Template?

By creating a Topo Template, you enable deployment of your project via Topo or any other tool that supports the Topo Template Format Specification. Going further and sharing your Topo Template with the community, via inclusion in the Topo Catalog, enables others also easily deploy your project.

## How do I create a Topo Template?

To create a Topo Template, start with a Docker Compose project and add `x-topo` metadata. The `x-topo` section extends the Compose file with Topo-specific information, such as:

1. Build arguments
2. Hardware requirements (features like SVE or Neon, or required RAM).
3. Project configuration at Topo clone time.

We will achieve this by the end of this Learning Path.

## What you've accomplished and what's next

You should now understand what a Topo Template is, and why you might create one. Next we will take an existing Template and customize it, before moving onto creating a Template from scratch.
