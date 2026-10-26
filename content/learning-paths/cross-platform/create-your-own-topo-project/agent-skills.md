---
title: Use Agent Skills to author Topo Projects
description: Install and use Topo Project Agent Skills to help create, review, and refine Topo Projects.
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Skills for authoring Topo Projects

If you already have a Docker Compose project and want to convert it to a Topo Project, you can do so with an Agent Skill. You can also use a skill to create your own Topo Project from scratch. These skills are optional authoring aids. 

[Topo](https://github.com/arm/topo) currently provides the following skills:

- `topo-project-context`: provides Topo and Topo Project reference context for questions about x-topo metadata, schema, docs, and CLI project behavior.
- `topo-project-bootstrap`: converts a repository into a Topo Project by adding or improving `compose.yaml` and `x-topo` metadata.
- `topo-project-lint`: reviews an existing Topo Project for correctness, consistency, and authoring best practices.
- `topo-project-optimize-deployment`: optimizes feedback loop by measuring and applying the highest-leverage Docker build improvement.

For the most up-to-date list of the available Topo skills, see [Topo Skills](https://github.com/arm/topo/tree/main/skills).

## Install the skills

Install the Topo skills with [npx skills](https://github.com/vercel-labs/skills):

{{% notice Note %}}
`npx` requires Node.js. If you don't have Node.js installed on your machine, install it before running the following command.
{{% /notice %}}

```bash
npx skills add arm/topo
```

Restart your AI coding agent after installing or updating skills to make sure new skills are loaded for use.

## Use the skills

After installing skills, you can prompt your agent to use a skill.

For example, to create a Topo Project from an existing project:

```text
Use the topo-project-bootstrap skill to convert this repository into a Topo Project.
```

## What you've accomplished 

You've now learned how you can install and use Agent Skills to help author Topo Projects.

You can now create, modify, and deploy Topo Projects to Arm-based Linux targets. To find more projects to clone and modify, explore the [Topo Catalog](https://github.com/arm/topo-project-catalog/blob/main/data/catalog.json).
