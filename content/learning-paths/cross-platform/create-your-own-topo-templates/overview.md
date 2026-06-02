---
title: Topo Template introduction
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Get started

Before getting started, you should complete the Learning Path [Deploy containerized workloads to Arm-based Linux targets with Topo](/learning-paths/cross-platform/deploy-containerized-workloads-with-topo/) to learn about Topo, why to use it, how to install it and how to use it for target inspection, listing templates and deployment.

## What is Topo?

[Topo](https://github.com/arm/topo) is an open-source command-line tool developed by Arm used to deploy projects to an Arm-based Linux target over SSH. Topo builds container images on the host, transfers them to the target, and starts the services on the target. Topo can also build and deploy directly on the target.

## What is a Topo Template?

A Topo Template is a containerized sample project for Arm-based Linux systems. At minimum, it is a directory containing a compose.yaml, Dockerfiles, and source code, with an x-topo metadata block that describes what the Template does, what hardware features it requires, and what parameters a user can configure.

The [Topo Template Format Specification](https://github.com/arm/topo-template-format) is based on the [Compose Specification](https://github.com/compose-spec/compose-spec), extended with `x-topo` metadata that describes requirements such as CPU features and build arguments. The Compose Specification is a standard, YAML-based format for describing multi-container applications. Instead of starting containers individually, you define all services, images, connections, and configuration in a single `compose.yaml` file.

In this learning path, you'll learn how to create and modify your own Topo Template.

## Where can I find Topo Templates?

Because the Topo Templates specification is an open one, anyone can publish their own Topo Templates and any tool can read and act on x-topo metadata to discover, validate, and deploy Templates.

A curated list of example Templates can be found either via:

1. the [topo templates](https://github.com/arm/topo?tab=readme-ov-file#3-find-a-template) command or
2. the [topo catalog](https://github.com/arm/topo/blob/main/internal/catalog/data/templates.json).

If you create your own Template, you can [Propose Your Template to Topo](https://github.com/arm/topo-template-format#propose-your-template-to-topo)

## Why create a Topo Template?

Creating a Topo Template allows you to inject the `x-topo` metadata on top of your docker compose project with extra information to the Docker Compose spec such as:

1. Build arguments
2. Hardware requirements (features like SVE or NEON or required RAM).
3. Project configuration at Topo clone time.

You can then share your Topo Template with the community, who will be able to deploy your project via Topo or any other tool that supports the Topo Template Format Specification.

## What you've accomplished and what's next

You have now installed Topo on your host and confirmed it is available.
You have got an understanding of what a Topo Template is and what its purpose is.
Next, you'll clone your first template and modify it.
