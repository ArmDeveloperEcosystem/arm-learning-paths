
---
title: Configure Gemini CLI context for Arm development
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

In this section, you configure Gemini CLI with persistent context so it can provide more relevant guidance for Arm development tasks.

By defining your development environment, architecture preferences, and constraints, you help Gemini generate responses that are tailored to Arm-based systems.

## Create the Gemini configuration directory

Gemini CLI reads context files from the `.gemini` directory in your home folder.

Create the directory if it does not already exist:

```console
mkdir -p ~/.gemini
```

## Define Arm development context

Create a context file named `GEMINI.md` that describes your Arm development environment.

```console
cat > ~/.gemini/GEMINI.md << 'EOF'
I am an Arm Linux developer.
I primarily work on Arm64 systems and prefer Arm-native solutions.
Please avoid x86-specific assumptions unless explicitly requested.
EOF
```

This file provides Gemini with persistent context that is automatically applied to all future sessions.

## Verify that context is applied

Start Gemini CLI:

```console
gemini
```

Ask a question related to development tooling:

```text
What should I consider when building software for Arm?
```

If context is loaded correctly, Gemini responds with Arm-specific guidance.

Next, you learn how Gemini CLI can be extended using the Arm Model Context Protocol.
