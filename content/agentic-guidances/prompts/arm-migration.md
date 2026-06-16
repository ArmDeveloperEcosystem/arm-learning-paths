---
title: Arm Migration
description: Placeholder orchestration prompt for migrating a codebase from x86 to Arm.
layout: agenticguidanceall
date: 2026-06-16
lastmod: 2026-06-16
minutes_to_complete: 10
agentic_guidance_kind: prompt
guidance_type: Orchestration Prompt
category: Server & Cloud
job_to_do: Migration
requirements:
  - Arm MCP Server
tools_software_languages:
  - Docker
  - Skopeo
  - C/C++
blueprints:
  - Cloud Service Migration to Arm64
when_to_use: When directing your agent to migrate an x86 codebase to Arm.
how_to_use: Use this in an interactive agentic session or as an automated slash command following your agent instructions.
prompt: |
  Your goal is to migrate a codebase from x86 to Arm. Use the MCP server tools to check x86-specific dependencies, build flags, intrinsics, libraries, container images, and CI settings. Change them to Arm architecture equivalents where needed, then explain compatibility and performance risks.

  Steps to follow:
  - Inspect Dockerfiles and container image references for Arm64 support.
  - Look at packages, build scripts, compiler flags, and architecture-specific code paths.
  - Recommend Arm-compatible replacements or guarded build logic.
  - Summarize the files changed and the tests needed to validate the migration.
---

This is placeholder content for a future Arm migration prompt.
