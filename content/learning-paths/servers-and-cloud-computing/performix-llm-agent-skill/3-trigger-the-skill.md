---
title: Best practices for prompting AI assistants to use the arm-performix skill
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Ensure the prompt shows performance and profiling intent

The skill activates on performance and profiling intent. 

The following are examples of prompts that show the expected intent:

- "Profile this workload on Arm and find the hotspots."
- "Why is this binary slow on my Arm Neoverse server?"
- "Use Performix to check whether my hot loop uses vector instructions."
- "Investigate cache and translation lookaside buffer stalls on my Neoverse target."

Prompts that are vague or don't show the expected intent won't activate the skill.

The following are example prompts that won't work:

- "Will my code build on Arm?" 
- "Make my code faster" 

## Provide context up front

In addition to prompting with the right intent, you need to provide the following context:

1. Target: a local Arm machine, or `user@host` for a remote Secure Shell (SSH) target
2. Binary: the absolute path to the executable on the target
3. Workload: the exact command and arguments, ideally repeatable
4. Goal: hotspots, vector instruction usage, memory locality, or a regression
   to investigate

If the AI assistant needs anything else, such as the source tree for line-level attribution or
your build flags, it'll prompt you for it rather than making an assumption.

The following is a good starting prompt:

```text
Profile /home/me/build/myapp --input /home/me/data/bench.dat on my Arm Neoverse target
me@neoverse-box with Performix. I want to know where the time goes.
```

This prompt gives the assistant the workload command and the SSH target. The
skill picks Code Hotspots first, runs it, and reports back with an analysis.

## Provide absolute paths

Always provide the absolute path to the binary. Use absolute paths for all files your workload reads or writes. 

If the workload must run from a specific directory, include the directory in the prompt. Performix can launch the process from a different working directory, so relative paths can resolve unexpectedly.

## What you've learned and what's next

You've now learned how to best structure your prompts to profile an application using the `arm-performix` skill.

Next, you'll learn how to use generated reports to drive performance improvements. 
