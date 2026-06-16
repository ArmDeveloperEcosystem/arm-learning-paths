---
title: Why does this Docker image fail on Arm64?
question: Why does this Docker image fail on Arm64?
description: Placeholder insight for missing Arm64 container manifests.
summary: The image may not publish an Arm64 manifest or may be pinned to an amd64 digest.
layout: insightall
date: 2026-06-16
lastmod: 2026-06-16
minutes_to_complete: 5
insight_type: Problem Solution
platform: Neoverse
operatingsystems:
  - Linux
goal: Migration
tags_general:
  - Docker
  - Containers
  - Arm64
---

Inspect the image manifest and check whether an Arm64 variant exists.

If the deployment pins an amd64 digest, update the reference to a multi-architecture tag or a supported Arm64 digest. This placeholder should later link to the relevant install guide or migration workflow.
