---
title: Install and enable the arm-performix skill
description: Download and install the arm-performix skill, place it in an AI assistant's skills directory, and confirm that the assistant can discover it.
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Download the skill folder

Use one of the following options to download the skill files:

### Clone skills repository from Gitee

If you prefer managing the skill source with Git, clone the skill file from Gitee.  

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

### Download package from SkillHub

If you prefer downloading a package directly from the web, download the skill from SkillHub.

Go to the [`arm-performix` SkillHub page](https://skillhub.openanolis.cn/skill/arm-performix)
and download the skill.

The downloaded skill is a `.zip` package. Extract it, then place the
`arm-performix` folder in your assistant's skills directory.

## Make the skill folder discoverable

The skill folder contains `SKILL.md`, `README.md`, and a
`references/` directory. Place the folder where your AI assistant discovers skills. 

For GitHub Copilot in VS Code, use the `.github/skills/` directory of your workspace:

```text
.github/
  skills/
    arm-performix/
      SKILL.md
      README.md
      references/
        <references>.md
```

Other assistants use different project directories, such as `.claude/skills/` or
`.agents/skills/`, so use the directory that matches your assistant. 

The `SKILL.md` file describes the profiling workflow. `README.md` provides
supporting overview information. The files under `references/` provide detailed
reference materials that the assistant reads on demand.

## Confirm the skill is discoverable

Reload your assistant or IDE to confirm that it can discover the skill. 

In VS Code, confirm that Agent Skills are enabled in the **Configure Chat** skills view or with the `/skills` command.

A correctly installed skill is picked up automatically when your request shows profiling or performance intent. You don't need to use a specific command to invoke the skill. 

For prompts you can use to confirm skill discovery, see [Best practices for prompting AI assistants to use the arm-performix skill](/learning-paths/servers-and-cloud-computing/performix-llm-agent-skill/3-trigger-the-skill).

## What you've accomplished and what's next

You've now installed the `arm-performix` skill folder and made it discoverable to your AI assistant. 

Next, you'll learn best practices for writing prompts to profile an application using the skill. 
