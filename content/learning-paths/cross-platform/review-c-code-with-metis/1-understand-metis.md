---
title: Understand the Metis review workflow
description: Learn how Metis gathers evidence, runs security reviews, and presents findings for human triage.
weight: 2
layout: "learningpathall"
---

## What is Metis?

Arm Metis is an open-source, agentic security code-review framework. It combines language-aware source tooling with a large language model (LLM) to investigate security-relevant behavior and return structured review candidates. Metis supports multiple programming and hardware description languages through language plugins. This Learning Path uses C examples, but the same concepts can be applied to the other supported languages.

You first run Metis on a small C program with known vulnerabilities. This gives you a quick look at the command flow, JSON output, SARIF output, and reported findings. You then prepare a libpng source tree from the [Magma](https://hexhive.epfl.ch/magma/) benchmark and triage a captured Metis finding against the source diff.

The exercises show how to use Metis during a security review. They do not benchmark Metis accuracy. Model choice, provider behavior, Metis version, and source changes can all affect a run. Use published benchmark results for comparative performance data.

{{% notice Note %}}
Model-backed review can consume substantial API tokens. The initial exercise is less expensive than the optional live libpng run. A pre-captured libpng report candidate is included so you can complete the triage exercise without running the larger review.
{{% /notice %}}

## How Metis reviews code

A Metis review starts with source files and project context. Metis collects language-aware evidence, asks your configured model to investigate possible vulnerabilities, and returns structured findings for a human reviewer.

Metis offers two review approaches:

- **Simple LLM review (default):** the model examines source code or a patch using language-specific security prompts and project guidance. It returns structured findings without requiring a code graph. This is also the review path for languages without C/C++ reachability support.
- **Optional reachability review:** for C/C++, Tree-sitter builds a CodeGraph of functions, calls, and source facts. When enabled, `reachability` reviews selected functions with this evidence and surrounding caller/callee context. Graph evidence does not by itself prove attacker control, build reachability, or exploitability.

In Metis 2.0.0, the packaged Review stage runs `simple_llm_review`, `finding_dedup`, and `result`. `review_code` and `review_file` use simple LLM review by default. Metis builds a CodeGraph for triage, but runs reachability review only when you enable it.

## Follow a review workflow with Metis

A security review with Metis typically follows these steps:

1. Choose a codebase, directory, file, or patch to review.
2. Add project-specific security context in `.metis.md` when needed.
3. Run a review and save the findings as JSON or SARIF.
4. Optionally use automated triage to check the findings against more source code.
5. Verify the findings against the source code, build configuration, and tests.

## Assess findings with automated triage

Automated triage checks a reported finding against more source code and marks it `valid`, `invalid`, or `inconclusive`. Metis checks the source lines cited for a `valid` or `invalid` verdict, but the verdict does not prove that the finding is correct or that an exploit works.

## How this Learning Path uses Metis

You will use two review commands on C code:

- In the first exercise, you use `review_code` to review the small C codebase.
- In the second exercise, you use `review_file` to focus on `pngrutil.c` with context from the rest of the libpng codebase.

The exercises start Metis with `--interactive` and run these commands at its prompt. Each command initializes the target automatically, so you do not need to run `init` first. You will inspect the findings yourself without enabling automated triage.

## Interpret Metis findings

A Metis finding normally includes the issue, source location, reasoning, suggested mitigation, Common Weakness Enumeration (CWE) identifier, severity, and confidence.

{{% notice Note %}}
CWE identifiers, such as `CWE-190` for integer overflow, provide standard names for common classes of software weakness.
{{% /notice %}}

You still decide whether a candidate is reachable, exploitable, already mitigated, or worth fixing.

## What you've learned and what's next

You have seen how Metis reports possible issues and why each finding needs a source check. Next, you will install the tested release and add your provider API key.
