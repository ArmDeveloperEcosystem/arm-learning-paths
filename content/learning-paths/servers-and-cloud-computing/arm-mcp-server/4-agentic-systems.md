---
title: Configure AI agents to automate Arm migration workflows
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Set up an agent workflow

Different AI coding tools provide different mechanisms for defining persistent instructions, such as prompt files or configuration documents. While the configuration details vary by tool, the goal remains the same: provide the AI with clear, structured instructions so it can use the Arm MCP Server effectively and carry out multi-step migration workflows autonomously.

This section shows how to set up Arm migration workflows in popular agentic AI systems. You'll see that the core migration logic stays consistent across platforms, but each tool has its own format for defining these instructions.

{{% notice Note %}}
The migration instructions below are the same workflow you used in the previous section. Each AI tool simply wraps those instructions in a different format.
{{% /notice %}}

## Set up Kiro steering documents

[Kiro](https://kiro.dev/) uses "steering documents" - markdown files stored in `.kiro/steering/` that provide persistent context to the AI. You can configure steering documents with different inclusion modes to control when and how the instructions are applied.

### Create Arm migration steering document

To set up Arm migration in Kiro, create the following file at `.kiro/steering/arm-migration.md`:

```markdown
---
inclusion: manual
---

Your goal is to migrate a codebase from x86 to Arm. Use the MCP server tools to help you with this. Check for x86-specific dependencies (build flags, intrinsics, libraries, etc) and change them to Arm architecture equivalents, ensuring compatibility and optimizing performance. Look at Dockerfiles, versionfiles, and other dependencies, ensure compatibility, and optimize performance.

Steps to follow:
* Look in all Dockerfiles and use the check_image and/or skopeo tools to verify Arm compatibility, changing the base image if necessary.
* Look at the packages installed by the Dockerfile and send each package to the knowledge_base_search tool to check each package for Arm compatibility. If a package isn't compatible, change it to a compatible version. When invoking the tool, explicitly ask "Is [package] compatible with Arm architecture?" where [package] is the name of the package.
* Look at the contents of any requirements.txt files line-by-line and send each line to the knowledge_base_search tool to check each package for Arm compatibility. If a package isn't compatible, change it to a compatible version.
* Look at the codebase that you have access to, and determine what the language used is.
* Run the migrate_ease_scan tool on the codebase, using the appropriate language scanner based on what language the codebase uses, and apply the suggested changes.
* OPTIONAL: If you have access to build tools, rebuild the project for Arm, if you're running on an Arm-based runner. Fix any compilation errors.
* OPTIONAL: If you have access to any benchmarks or integration tests for the codebase, run these and report the timing improvements to the user.

Pitfalls to avoid:

* Don't confuse a software version with a language wrapper package version. For example, when checking the Python Redis client, check the Python package name "redis" rather than the Redis server version.
* NEON lane indices must be compile-time constants, not variables.

If you have good versions to update for the Dockerfile, requirements.txt, and other files, change them immediately without asking for confirmation.

Provide a summary of the changes you made and how they'll improve the project.
```

Reference this steering document in chat with `#arm-migration`.

## OpenAI Codex prompt files

[OpenAI Codex](https://openai.com/codex/) uses markdown prompt files stored in `~/.codex/prompts/` or `$CODEX_HOME/prompts/`. The filename determines the command name you'll use to invoke the prompt.

### Create Arm migration prompt

Create the following file at `~/.codex/prompts/arm-migrate.md`:

```markdown
---
description: Migrate codebase from x86 to Arm architecture
---

Your goal is to migrate a codebase from x86 to Arm. Use the MCP server tools to help you with this. Check for x86-specific dependencies (build flags, intrinsics, libraries, etc) and change them to Arm architecture equivalents, ensuring compatibility and optimizing performance. Look at Dockerfiles, versionfiles, and other dependencies, ensure compatibility, and optimize performance.

Steps to follow:
* Look in all Dockerfiles and use the check_image and/or skopeo tools to verify Arm compatibility, changing the base image if necessary.
* Look at the packages installed by the Dockerfile and send each package to the knowledge_base_search tool to check each package for Arm compatibility. If a package isn't compatible, change it to a compatible version. When invoking the tool, explicitly ask "Is [package] compatible with Arm architecture?" where [package] is the name of the package.
* Look at the contents of any requirements.txt files line-by-line and send each line to the knowledge_base_search tool to check each package for Arm compatibility. If a package isn't compatible, change it to a compatible version.
* Look at the codebase that you have access to, and determine what the language used is.
* Run the migrate_ease_scan tool on the codebase, using the appropriate language scanner based on what language the codebase uses, and apply the suggested changes.
* OPTIONAL: If you have access to build tools, rebuild the project for Arm, if you're running on an Arm-based runner. Fix any compilation errors.
* OPTIONAL: If you have access to any benchmarks or integration tests for the codebase, run these and report the timing improvements to the user.

Pitfalls to avoid:

* Don't confuse a software version with a language wrapper package version. For example, when checking the Python Redis client, check the Python package name "redis" rather than the Redis server version.
* NEON lane indices must be compile-time constants, not variables.

If you have good versions to update for the Dockerfile, requirements.txt, and other files, change them immediately without asking for confirmation.

Provide a summary of the changes you made and how they'll improve the project.
```

### Running the Codex prompt

Invoke the prompt with:

```bash
codex /prompts:arm-migrate
```

## Other AI assistants

You now have a general understanding of how agentic systems support persistent migration instructions. For other AI coding assistants, consult their documentation to learn how to define equivalent prompt files or configuration mechanisms and adapt the same Arm migration workflow.

## What you've accomplished and what's next

In this section, you've learned how to configure Arm migration workflows in different agentic AI systems including Kiro and OpenAI Codex. You've seen how the core migration logic remains consistent across platforms while each tool uses its own format for defining persistent instructions.

You're now equipped to use the Arm MCP Server with your preferred AI coding assistant to automate the migration of x86 applications to Arm-based cloud instances.
