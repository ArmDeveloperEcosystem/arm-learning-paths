---
title: Performance Investigation Q&A
description: Placeholder standard prompt for asking performance investigation questions.
layout: agenticguidanceall
date: 2026-06-16
lastmod: 2026-06-16
minutes_to_complete: 5
agentic_guidance_kind: prompt
guidance_type: Standard Prompt
category: Server & Cloud
job_to_do: Optimize
requirements:
  - Performance data
tools_software_languages:
  - Linux perf
  - GCC
  - Python
blueprints:
  - CI Performance Regression Guard
when_to_use: When you need an agent to ask clarifying questions before investigating an Arm performance issue.
how_to_use: Paste this prompt with logs, benchmark commands, hardware details, and the performance symptom.
prompt: |
  Help me investigate this Arm performance issue. Start by listing the missing measurements you need, then inspect the data I provide for CPU, memory, compiler, and workload clues. Separate confirmed evidence from hypotheses.
---

This is placeholder content for a future performance Q&A prompt.
