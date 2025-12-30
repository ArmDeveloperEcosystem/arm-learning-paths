
---
title: Use Gemini CLI for Arm code analysis and migration
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

In this section, you use Gemini CLI to reason about Arm compatibility and migration considerations for existing codebases.

Gemini CLI provides guidance and analysis, not automated code transformation.

## Analyze code portability

Ask Gemini questions such as:

```text
Are there common x86 assumptions in this codebase?
```

```text
What should I check when migrating this application to Arm64?
```

Gemini can help identify:
- Architecture-specific dependencies
- Build system assumptions
- Potential portability risks

## Migration guidance

Use Gemini CLI to reason about:
- Compiler flags
- Dependency availability
- Runtime behavior differences

This guidance helps you plan migrations more effectively.

Next, you explore how Gemini CLI can assist with optimization-related questions.
