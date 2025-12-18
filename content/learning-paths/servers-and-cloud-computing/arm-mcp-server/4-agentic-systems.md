---
title: Configure Different Agentic Systems
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Agentic AI Systems for Migration

Different AI coding tools have different ways of configuring persistent instructions and prompt files. This section shows how to set up Arm migration workflows in a couple other popular agentic systems.

The goal is the same across all systems: provide the AI with structured instructions that enable it to use the Arm MCP Server tools effectively and execute multi-step migration workflows autonomously.

## Kiro Steering Documents

[Kiro](https://kiro.dev/) uses "steering documents" - markdown files stored in `.kiro/steering/` that provide persistent context to the AI. Steering files support different inclusion modes based on when you want the instructions to apply.

### Create Arm Migration Steering Document

Create a file at `.kiro/steering/arm-migration.md`:

```markdown
---
inclusion: manual
---

Your goal is to migrate a codebase from x86 to Arm. Use the MCP server tools to help you with this. Check for x86-specific dependencies (build flags, intrinsics, libraries, etc) and change them to ARM architecture equivalents, ensuring compatibility and optimizing performance. Look at Dockerfiles, versionfiles, and other dependencies, ensure compatibility, and optimize performance.

Steps to follow:
* Look in all Dockerfiles and use the check_image and/or skopeo tools to verify ARM compatibility, changing the base image if necessary.
* Look at the packages installed by the Dockerfile and send each package to the knowledge_base_search tool to check each package for ARM compatibility. If a package is not compatible, change it to a compatible version. When invoking the tool, explicitly ask "Is [package] compatible with ARM architecture?" where [package] is the name of the package.
* Look at the contents of any requirements.txt files line-by-line and send each line to the knowledge_base_search tool to check each package for ARM compatibility. If a package is not compatible, change it to a compatible version.
* Look at the codebase that you have access to, and determine what the language used is.
* Run the migrate_ease_scan tool on the codebase, using the appropriate language scanner based on what language the codebase uses, and apply the suggested changes.
* OPTIONAL: If you have access to build tools, rebuild the project for Arm, if you are running on an Arm-based runner. Fix any compilation errors.
* OPTIONAL: If you have access to any benchmarks or integration tests for the codebase, run these and report the timing improvements to the user.

Pitfalls to avoid:

* Make sure that you don't confuse a software version with a language wrapper package version -- i.e. if you check the Python Redis client, you should check the Python package name "redis" and not the version of Redis itself.
* NEON lane indices must be compile-time constants, not variables.

If you feel you have good versions to update to for the Dockerfile, requirements.txt, etc. immediately change the files, no need to ask for confirmation.

Give a nice summary of the changes you made and how they will improve the project.
```

Reference this steering document in chat with `#arm-migration`.

## OpenAI Codex Prompt Files

[OpenAI Codex](https://openai.com/codex/) uses markdown prompt files stored in `~/.codex/prompts/` or `$CODEX_HOME/prompts/`. The filename becomes the command name.

### Create Arm Migration Prompt

Create a file at `~/.codex/prompts/arm-migrate.md`:

```markdown
---
description: Migrate codebase from x86 to Arm architecture
---

Your goal is to migrate a codebase from x86 to Arm. Use the MCP server tools to help you with this. Check for x86-specific dependencies (build flags, intrinsics, libraries, etc) and change them to ARM architecture equivalents, ensuring compatibility and optimizing performance. Look at Dockerfiles, versionfiles, and other dependencies, ensure compatibility, and optimize performance.

Steps to follow:
* Look in all Dockerfiles and use the check_image and/or skopeo tools to verify ARM compatibility, changing the base image if necessary.
* Look at the packages installed by the Dockerfile and send each package to the knowledge_base_search tool to check each package for ARM compatibility. If a package is not compatible, change it to a compatible version. When invoking the tool, explicitly ask "Is [package] compatible with ARM architecture?" where [package] is the name of the package.
* Look at the contents of any requirements.txt files line-by-line and send each line to the knowledge_base_search tool to check each package for ARM compatibility. If a package is not compatible, change it to a compatible version.
* Look at the codebase that you have access to, and determine what the language used is.
* Run the migrate_ease_scan tool on the codebase, using the appropriate language scanner based on what language the codebase uses, and apply the suggested changes.
* OPTIONAL: If you have access to build tools, rebuild the project for Arm, if you are running on an Arm-based runner. Fix any compilation errors.
* OPTIONAL: If you have access to any benchmarks or integration tests for the codebase, run these and report the timing improvements to the user.

Pitfalls to avoid:

* Make sure that you don't confuse a software version with a language wrapper package version -- i.e. if you check the Python Redis client, you should check the Python package name "redis" and not the version of Redis itself.
* NEON lane indices must be compile-time constants, not variables.

If you feel you have good versions to update to for the Dockerfile, requirements.txt, etc. immediately change the files, no need to ask for confirmation.

Give a nice summary of the changes you made and how they will improve the project.
```

### Running the Codex Prompt

Invoke the prompt with:

```bash
codex /prompts:arm-migrate
```

## Other AI assistants

You should now have a good feel for how agents generally implement these types of instructions. You can search for documentation on how your specific AI coding assistent implements them.
