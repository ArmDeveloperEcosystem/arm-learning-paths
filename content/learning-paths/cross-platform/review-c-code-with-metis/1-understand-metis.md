---
title: Understand the Metis review workflow
description: Learn how Metis gathers evidence, runs security reviews, and presents findings for human triage.
weight: 2
layout: "learningpathall"
---

## What Metis is

Arm Metis is an open-source, agentic security code-review framework. It investigates security-relevant behavior and returns structured review candidates. To do this, Metis combines language-aware source tooling with a large language model (LLM).

Metis supports multiple programming and hardware description languages through language plugins. The code in this Learning Path is in C, but the same concepts can be applied to other supported languages.

You'll learn how to use Metis during a security review. First, you'll run Metis on a small C program with known vulnerabilities. You'll export JSON and SARIF reports, then inspect the JSON findings. You'll then prepare a libpng source tree from the [Magma](https://hexhive.epfl.ch/magma/) benchmark and triage a captured Metis finding against the source diff.

{{% notice Note %}}

- The Learning Path isn't an exercise to benchmark Metis accuracy. Model choice, provider behavior, Metis version, and source changes can all affect a run. Use published benchmark results for comparative performance data.
- Model-backed review can consume substantial API tokens. The initial Metis run is less expensive than the optional live libpng run. A pre-captured libpng report candidate is included so that you can complete triage without running the larger review.
{{% /notice %}}

## How Metis reviews code

A Metis review starts with source files and project context. Metis collects language-aware evidence, asks your configured model to investigate possible vulnerabilities, and returns structured findings for a human reviewer.

Metis offers two review approaches:

- Simple LLM review: The model examines source code or a patch using language-specific security prompts and project guidance. It returns structured findings without a code graph. This approach also covers languages without C or C++ reachability support.
- Optional reachability review: For C or C++, Tree-sitter builds a CodeGraph of functions, calls, and source facts. When enabled, `reachability` uses this evidence and surrounding caller and callee context to review selected functions. Graph evidence alone doesn't prove attacker control, build reachability, or exploitability.

In Metis 2.0.0, the packaged Review stage runs `simple_llm_review`, `finding_dedup`, and `result`. `review_code` and `review_file` use simple LLM review by default. Metis builds a CodeGraph for triage, but runs reachability review only when you enable it.

## Follow a review workflow with Metis

A security review with Metis typically involves completing the following steps:

1. Choose a codebase, directory, file, or patch to review.
2. Add project-specific security context in `.metis.md` when needed.
3. Run a review and save the findings as JSON or SARIF.
4. Optionally use automated triage to check the findings against more source code and mark it `valid`, `invalid`, or `inconclusive`. Metis checks the source lines cited for a `valid` or `invalid` verdict.
5. Verify the findings against the source code, build configuration, and tests.

## How you'll use Metis to complete the Learning Path

You'll use the following review commands on C code:

- `review_code` to review the small C codebase
- `review_file` to focus on `pngrutil.c` with context from the rest of the libpng codebase

You'll start Metis with `--interactive` and run these commands at its prompt. Each command initializes the target automatically, so you don't need to run `init` first. You'll inspect the findings yourself without enabling automated triage.

## How to interpret Metis findings

A Metis finding usually includes the following information:

- Issue
- Source location
- Reasoning
- Suggested mitigation
- Common Weakness Enumeration (CWE) identifier
- Severity
- Confidence

{{% notice Note %}}
CWE identifiers, such as `CWE-190` for integer overflow, provide standard names for common classes of software weakness.
{{% /notice %}}

You still decide whether a candidate is reachable, exploitable, already mitigated, or worth fixing.

## What you've learned and what's next

You've learned what Metis reports about possible issues and why each finding needs a source check.

Next, you'll install the tested release and add your provider API key.
