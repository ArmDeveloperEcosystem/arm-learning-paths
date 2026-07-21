---
title: Install and enable the skill
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Get the skill files

Use one of these options to get the skill files.

### Option 1: Clone from Gitee

Use this option if you prefer managing the skill source with Git.

From the root of the project where your assistant works, clone the skills
repository:

```bash
git clone https://gitee.com/anolis/anolis-skills.git
```

Copy only the `arm-performix` skill folder into your assistant's project skills
directory:

```bash
mkdir -p .github/skills
cp -R anolis-skills/skills/arm-performix .github/skills/
```

### Option 2: Download from SkillHub

Use this option if you prefer downloading a package directly from the web.

Go to the [arm-performix SkillHub page](https://skillhub.openanolis.cn/skill/arm-performix)
and download the skill.

The downloaded skill is a `.zip` package. Extract it, then place the
`arm-performix` folder in your assistant's skills directory.

## Place the skill files

The skill is a folder that contains `SKILL.md`, `README.md`, and a
`references/` directory. Put it where your assistant discovers skills. For GitHub
Copilot in VS Code, use the `.github/skills/` directory of your workspace. Other
assistants use different project directories, such as `.claude/skills/` or
`.agents/skills/`, so use the directory that matches your assistant:

```text
.github/
  skills/
    arm-performix/
      SKILL.md
      README.md
      references/
        <references>.md
```

The `SKILL.md` file describes the profiling workflow; `README.md` provides
supporting overview information; and files under `references/` provide detailed
reference materials that the assistant reads on demand.

## Confirm the skill is discovered

Reload your assistant or IDE, then ask your assistant a profiling question (see
the next page). In VS Code, confirm that Agent Skills are enabled in the
**Configure Chat** skills view or with the `/skills` command. A correctly
installed skill is picked up automatically when your request matches its
triggers; you do not need to invoke it with an explicit command.

{{% notice Tip %}}
The skill only *describes* how to use Performix. You still need Performix itself
available: either the `apx` CLI on your `PATH`, or the Arm MCP Server configured.
The skill tells you when neither is reachable rather than guessing.
{{% /notice %}}

## Choose how Performix runs

The skill can start Performix in two ways. You do not have to pick manually, but
it helps to know which path you have set up:

- **apx CLI**: the full-capability path. Install it on your host, add the `apx`
  directory to your `PATH`, and confirm it with `apx version` from the same
  terminal environment your assistant can use. This path works best for remote
  Secure Shell (SSH) targets, automation, and CI.
- **Arm MCP Server**: bundles its own `apx`, so your host needs no CLI install.
  This path works best for fully agent-driven launch-mode profiling. The skill
  routes here only when you ask, or when the CLI is not installed and you confirm
  MCP. Use the CLI or GUI for attach-to-process ID (PID), system-wide profiling,
  run export/import, custom result queries, CI/CD automation, and System
  Characterization.
