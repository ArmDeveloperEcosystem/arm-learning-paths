---
title: Verify and prepare Gemini CLI
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

In this section, you verify that Gemini CLI is installed and authenticated, and confirm that it is ready for use in this Learning Path.

{{% notice Note %}}This Learning Path assumes that Gemini CLI has already been installed. Installation steps are provided separately in the [Gemini CLI install guide](/install-guides/gemini/).
{{% /notice %}}

## Before you begin

To continue with this Learning Path, ensure that:

- Gemini CLI is installed on your system
- You have completed authentication (for example, using Google OAuth or an API key)
- You can access a terminal on macOS or Arm Linux

## Verify Gemini CLI installation

Confirm that the Gemini CLI binary is available by checking the version:

```console
gemini --version
```

Output similar to the following indicates that Gemini CLI is installed correctly:

```output
0.20.0
```

## Verify authentication and start a session

Start an interactive Gemini CLI session:

```console
gemini
```

On first run, you are prompted to authenticate if authentication has not already been configured. After successful authentication, the interactive Gemini CLI session opens.

If authentication fails or you need to change your authentication method, follow the instructions in the
[Gemini CLI Install Guide](/install-guides/gemini-cli/).

## What you have accomplished and what is next

You have verified that Gemini CLI is installed and ready to use.

Next, you configure Gemini CLI with persistent context so it can provide more relevant guidance for Arm development tasks.

