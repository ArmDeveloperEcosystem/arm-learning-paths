---
title: Learn about Topo Templates
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Before you begin

[Topo](https://github.com/arm/topo) is an open-source command-line tool developed by Arm that you can use to deploy projects to an Arm-based Linux target over SSH. Topo builds container images on the host, transfers them to the target, and starts the services on the target. Topo can also build and deploy directly on the target.

Before getting started with this Learning Path, complete the Learning Path [Deploy containerized workloads to Arm-based Linux targets with Topo](/learning-paths/cross-platform/deploy-containerized-workloads-with-topo/).

After completing the Learning Path, you'll have Topo installed on your host machine and an Arm-based Linux target available over SSH. 

You'll use the same target pattern in this Learning Path as the previous one. The target can be a Raspberry Pi, an Arm-based Amazon EC2 instance, or another Arm-based Linux system:

```bash
--target user@my-target
```

If your host machine is also a Linux target, you can use `--target localhost`.

## What a Topo Template is

A Topo Template is a containerized sample project for Arm-based Linux systems. At minimum, it's a directory containing a `compose.yaml`, Dockerfiles, and source code. The `compose.yaml` file contains an `x-topo` metadata block that describes what the Template does, what hardware features it requires, and what parameters a user can configure.

The [Topo Template Format Specification](https://github.com/arm/topo-template-format) is based on the [Compose Specification](https://github.com/compose-spec/compose-spec), extended with `x-topo` metadata that describes requirements such as CPU features and build arguments. 

The Compose Specification is a standard, YAML-based format for describing multi-container applications. Instead of starting containers individually, you define all services, images, connections, and configuration in a single `compose.yaml` file.

By creating a Topo Template, you enable deployment of your project with Topo or any other tool that supports the Topo Template format specification. Going further and sharing your Topo Template with the community, by including it in the Topo Catalog, allows others to easily deploy your project.

## Where you can find Topo Templates

The Topo Templates specification is an open specification. Anyone can publish their own Topo Templates. Any tool can read and act on `x-topo` metadata to discover, validate, and deploy Templates.

You can find a curated list of example Templates using the Topo Templates command used in the previous Learning Path:

```bash
topo templates --target user@my-target
```

Alternatively, you can find Topo Templates in the [Topo Catalog](https://github.com/arm/topo/blob/main/internal/catalog/data/catalog.json).

To propose adding a Topo Template you created to the Template list, see [Propose your Template to Topo](https://github.com/arm/topo-template-format#propose-your-template-to-topo).

## How you can create a Topo Template

To create a Topo Template, start with a Docker Compose project and add `x-topo` metadata. The `x-topo` section extends the Compose file with Topo-specific information, such as:

- Build arguments
- Hardware requirements (features such as Scalable Vector Extension (SVE) or Neon, or required RAM)
- Clone-time project configuration 

## What you've accomplished and what's next

You now understand what a Topo Template is, and why you might create one. 

Next, you'll clone and deploy an existing Topo Template.
