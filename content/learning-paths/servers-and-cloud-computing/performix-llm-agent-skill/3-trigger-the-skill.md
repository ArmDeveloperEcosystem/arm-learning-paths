---
title: Trigger the skill with profiling context
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Write a prompt that activates the skill

The skill activates on performance and profiling intent. Prompts that work:

- "Profile this workload on Arm and find the hotspots."
- "Why is this binary slow on my Arm Neoverse server?"
- "Use Performix to check whether my hot loop uses vector instructions."
- "Investigate cache and translation lookaside buffer stalls on my Neoverse target."

Prompts that don't activate the skill:

- "Will my code build on Arm?" — a migration question, not a profiling one.
- "Make my code faster" — too vague without a target or binary; add both.

## Provide context up front

The skill needs these details before it can profile. Supplying them in your first
message avoids a round of back-and-forth:

1. **Target**: a local Arm machine, or `user@host` for a remote Secure Shell (SSH) target
2. **Binary**: the **absolute path** to the executable on the target
3. **Workload**: the exact command and arguments, ideally repeatable
4. **Goal**: hotspots, vector instruction usage, memory locality, or a regression
   to investigate

If it needs anything else, such as the source tree for line-level attribution or
your build flags, the skill asks rather than guesses.

A good starting prompt looks like this:

```text
Profile /home/me/build/myapp --input /home/me/data/bench.dat on my Arm Neoverse target
me@neoverse-box with Performix. I want to know where the time goes.
```

This prompt gives the assistant the workload command and the SSH target. The
skill picks **Code Hotspots** first, runs it, and reports back with an analysis.

{{% notice Note %}}
Always give the **absolute path** to the binary, and use absolute paths for input
files, output files, and other files your workload reads or writes. If the
workload must run from a specific directory, tell the assistant that working
directory explicitly. Performix can launch the process from a different working
directory, so relative paths can resolve unexpectedly.
{{% /notice %}}
