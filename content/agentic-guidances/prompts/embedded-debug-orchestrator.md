---
title: Embedded Debug Orchestrator
description: Placeholder orchestration prompt for embedded Arm debugging workflows.
layout: agenticguidanceall
date: 2026-06-16
lastmod: 2026-06-16
minutes_to_complete: 10
agentic_guidance_kind: prompt
guidance_type: Orchestration Prompt
category: Embedded
job_to_do: Assess
requirements:
  - Board access
tools_software_languages:
  - CMSIS
  - GDB
  - C
blueprints:
  - Embedded Bring-up Checklist
when_to_use: When an agent needs to coordinate a first-pass debug flow for an embedded Arm target.
how_to_use: Provide the target board, toolchain, debugger, logs, and the observed failure mode.
prompt: |
  Coordinate an embedded Arm debug session. Confirm the board, firmware image, debugger connection, memory map, clock setup, and fault symptoms. Propose a minimal sequence of checks before suggesting code changes.
---

This is placeholder content for a future embedded debug prompt.
