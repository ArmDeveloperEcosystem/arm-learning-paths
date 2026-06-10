---
title: Use agent skills for Topo Templates
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Skills for authoring Templates

If you already have a Docker Compose project and want to convert it to a Topo Template, or you want to create your own Topo Template from scratch, you can do so with an Agent Skill.

These skills are optional authoring aids. The Template you created in this Learning Path works with Topo without them.

Visit [Topo Skills](https://github.com/arm/topo-template-format#authoring-skills) for the most up-to-date list of the available Topo Template skills and instructions on how to install them.

The [Topo Template Format Specification](https://github.com/arm/topo-template-format) currently provides the following skills:

1. `topo-template-context`: provides Topo and Topo Template reference context for questions about x-topo metadata, schema, docs, and CLI Template behavior.
2. `topo-template-bootstrap`: converts a repository into a Topo Template by adding or improving `compose.yaml` and `x-topo` metadata.
3. `topo-template-lint`: reviews an existing Topo Template for correctness, consistency, and authoring best practices.

## Install the skills

Install the Topo Template skills with [npx skills](https://github.com/vercel-labs/skills):

{{% notice Note %}}
`npx` requires Node.js. If Node.js is not installed on your machine, install it before running the command below.
{{% /notice %}}

```bash
npx skills add arm/topo-template-format --all --yes
```

Restart your agent after installing or updating skills.

## Use the skills

You can then prompt your agent to use the skill to create a Topo Template from an existing project:

```text
Use the topo-template-bootstrap skill to convert this repository into a Topo Template.
```

## What you've accomplished and what's next

You have now completed this Learning Path. You can create, modify, and deploy Topo Templates to Arm-based Linux targets, and use Agent Skills to assist with the authoring process.

Explore the [Topo Catalog](https://github.com/arm/topo/blob/main/internal/catalog/data/catalog.json) to find more Templates to clone and modify, or share your own Template with the community.
