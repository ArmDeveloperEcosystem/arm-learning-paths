---
title: Container Image Compatibility
description: Placeholder maintenance skill for validating container image architecture support.
layout: agenticguidanceall
date: 2026-06-16
lastmod: 2026-06-16
minutes_to_complete: 10
agentic_guidance_kind: skill
guidance_type: Maintenance Skill
category: Server & Cloud
job_to_do: Migration
requirements:
  - Arm MCP Server
tools_software_languages:
  - Docker
  - Skopeo
  - Kubernetes
blueprints:
  - Cloud Service Migration to Arm64
when_to_use: When a workflow uses container images that must run on Arm64 infrastructure.
how_to_use: Add this skill to migration or CI workflows that inspect Dockerfiles, Helm charts, and deployment manifests.
prompt: |
  Check all container image references for Arm64 compatibility. Use manifest inspection where possible. Flag single-architecture images, pinned amd64 digests, and base images without Arm64 variants.
---

This is placeholder content for a future container image skill.
