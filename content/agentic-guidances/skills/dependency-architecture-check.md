---
title: Dependency Architecture Check
description: Placeholder one-off skill for checking dependency architecture support.
layout: agenticguidanceall
date: 2026-06-16
lastmod: 2026-06-16
minutes_to_complete: 10
agentic_guidance_kind: skill
guidance_type: One-off Skill
category: Laptops & Desktops
job_to_do: Assess
requirements:
  - Package manifest
tools_software_languages:
  - npm
  - Python
  - GitHub Actions
blueprints:
  - CI Performance Regression Guard
when_to_use: When a project may depend on packages or binaries that do not publish Arm64 artifacts.
how_to_use: Run this skill against package manifests, lockfiles, release assets, and CI logs.
prompt: |
  Inspect project dependencies for Arm64 support. Flag binary packages, native extensions, container images, or release downloads that may not provide Arm64 artifacts. Recommend validation commands and replacement options.
---

This is placeholder content for a future dependency architecture skill.
