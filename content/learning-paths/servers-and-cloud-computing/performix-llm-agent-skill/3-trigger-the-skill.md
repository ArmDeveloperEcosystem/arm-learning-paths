---
title: Trigger the skill with the right context
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Phrase the request so the skill activates

The skill activates on performance and profiling intent. Phrasings that work:

- "Profile this workload on Arm and find the hotspots."
- "Why is this binary slow on my Arm Neoverse server?"
- "Use Performix to check whether my hot loop is vectorized."
- "Investigate cache and TLB stalls on my Neoverse target."

Phrasings that will *not* activate it, because these are migration or vague questions:

- "Will my code build on Arm?" That is a migration question, not a profiling one.
- "Make my code faster" with no target or binary, which is too vague; add context.

## Provide the context up front

The skill needs the following before it can profile. Supplying them in your first
message avoids a round of back-and-forth:

1. **Target**: a local Arm machine, or `user@host` for a remote SSH target
2. **Binary**: the **absolute path** to the executable on the target
3. **Workload**: the exact command and arguments, ideally repeatable
4. **Goal**: hotspots, SIMD usage, memory locality, or a regression to chase

If it needs anything else, such as the source tree for line-level attribution or
your build flags, the skill is designed to ask for it rather than guess.

A good first prompt looks like this:

```text
Profile /home/me/build/myapp --input bench.dat on my Arm Neoverse target
me@neoverse-box with Performix. I want to know where the time goes.
```

The skill picks **Code Hotspots** first, runs it, and reports back with the
analysis report described on the next page.

{{% notice Note %}}
Always give the **absolute path** to the binary, and use absolute paths for any
output files your workload writes. Performix may launch the process from a
temporary working directory, so relative paths can resolve unexpectedly.
{{% /notice %}}
