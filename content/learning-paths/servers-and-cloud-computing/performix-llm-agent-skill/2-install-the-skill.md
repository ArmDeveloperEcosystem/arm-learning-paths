---
title: Install and enable the skill
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Get the skill files

You can get the skill in either of these ways:

- Clone the skills repository from Gitee:

```bash
git clone https://gitee.com/anolis/anolis-skills.git
```

Use this if you prefer managing the skill source with Git.

- Download the skill package from the SkillHub page:
  https://skillhub.openanolis.cn/skill/arm-performix

Use this if you prefer downloading a package from the web page. The downloaded
skill is a `.zip` package, so extract it before placing the folder.

## Place the skill files

The skill is a folder that contains `SKILL.md`, `README.md`, and a
`references/` directory. Put it where your assistant discovers skills. For
GitHub Copilot in VS Code, that is the `.github/skills/` directory of your
workspace:

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

Reload VS Code, then ask your assistant a profiling question (see the next page).
A correctly installed skill is picked up automatically when your request matches
its triggers; you do not invoke it with an explicit command.

{{% notice Tip %}}
The skill only *describes* how to use Performix. You still need Performix itself
available: either the `apx` CLI on your `PATH`, or the Arm MCP Server configured.
The skill tells you when neither is reachable rather than guessing.
{{% /notice %}}

## Choose how Performix runs

The skill can drive Performix two ways. You do not have to pick manually, but it
helps to know which you have set up:

- **apx CLI**: the full-capability path. Install it on your host and confirm it
  with `apx version`. Best for remote SSH targets, automation, and CI.
- **Arm MCP Server**: bundles its own `apx`, so your host needs no CLI install.
  Best for fully agent-driven workflows. The skill routes here only when you ask,
  or when the CLI is not installed and you confirm MCP.
