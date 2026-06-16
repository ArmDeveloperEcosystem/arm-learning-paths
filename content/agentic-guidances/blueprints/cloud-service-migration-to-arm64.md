---
title: Cloud Service Migration to Arm64
description: Placeholder blueprint that combines prompts and skills for a cloud service migration workflow.
layout: agenticguidanceall
date: 2026-06-16
lastmod: 2026-06-16
minutes_to_complete: 20
agentic_guidance_kind: blueprint
guidance_type: Blueprint
category: Server & Cloud
job_to_do: Migration
requirements:
  - Arm MCP Server
tools_software_languages:
  - Docker
  - Skopeo
  - GitHub Actions
blueprints:
  - Arm Migration
  - SVE2 Loop Optimization
when_to_use: When you want to validate that an existing cloud deployment can move to Arm64 machines.
how_to_use: Integrate the main orchestration prompt into your CI/CD pipeline, then call supporting skills when the agent detects containers, dependencies, or performance-sensitive code.
blueprint_nodes:
  - label: Persona prompt
    title: Arm Code Review Persona
    link: /agentic-guidances/prompts/code-review-persona/
  - label: Orchestration prompt
    title: Arm Migration
    link: /agentic-guidances/prompts/arm-migration/
blueprint_subagents:
  - title: SVE2 Loop Optimizer
    link: /agentic-guidances/skills/sve2-loop-optimization/
  - title: Container Image Compatibility
    link: /agentic-guidances/skills/container-image-compatibility/
  - title: Dependency Architecture Check
    link: /agentic-guidances/skills/dependency-architecture-check/
---

This is placeholder content for a future cloud service migration blueprint.
