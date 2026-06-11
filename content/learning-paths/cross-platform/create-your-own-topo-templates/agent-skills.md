---
title: Use Agent Skills to author Topo Templates
description: Install and use Topo Template Agent Skills to help create, review, and refine Topo Templates.
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Skills for authoring Templates

If you already have a Docker Compose project and want to convert it to a Topo Template, you can do so with an Agent Skill. You can also use a skill to create your own Topo Template from scratch. These skills are optional authoring aids. 

The [Topo Template Format Specification](https://github.com/arm/topo-template-format) currently provides the following skills:

- `topo-template-context`: provides Topo and Topo Template reference context for questions about x-topo metadata, schema, docs, and CLI Template behavior.
- `topo-template-bootstrap`: converts a repository into a Topo Template by adding or improving `compose.yaml` and `x-topo` metadata.
- `topo-template-lint`: reviews an existing Topo Template for correctness, consistency, and authoring best practices.

For the most up-to-date list of the available Topo Template skills, see [Topo Skills](https://github.com/arm/topo-template-format#authoring-skills) . 

## Install the skills

Install the Topo Template skills with [npx skills](https://github.com/vercel-labs/skills):

{{% notice Note %}}
`npx` requires Node.js. If you don't have Node.js installed on your machine, install it before running the following command.
{{% /notice %}}

```bash
npx skills add arm/topo-template-format --all --yes
```

Restart your AI coding agent after installing or updating skills to make sure new skills are loaded for use.

## Use the skills

After installing skills, you can prompt your agent to use a skill to create a Topo Template from an existing project.

For example, to convert a repository into a template:

```text
Use the topo-template-bootstrap skill to convert this repository into a Topo Template.
```

## What you've accomplished 

You've now learned how you can install and use Agent Skills to help author Topo Templates.

Explore the [Topo Catalog](https://github.com/arm/topo/blob/main/internal/catalog/data/catalog.json) to find more Templates to clone and modify, or share your own Template with the community.
