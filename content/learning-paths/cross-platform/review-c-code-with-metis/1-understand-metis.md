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

In Metis 2.0.0, the packaged Review stage runs `simple_llm_review`, `finding_dedup`, and `result`. Reachability is opt-in, not part of this default review. Initialize still builds the CodeGraph for Triage. The exercises use the shipped graph through `review_code` and `review_file` without enabling reachability.

## Follow the review workflow

A typical Metis workflow looks like this:

1. Pick the review question, such as "review this parser file" or "review this patch."
2. Choose a review command: `review_code`, `review_dir`, `review_file`, or `review_patch`.
3. Add project-specific security context in `.metis.md` when the source needs extra assumptions.
4. Run Metis and save the result as JSON, SARIF, or both.
5. Optionally run Metis triage to assess the candidates against additional source evidence.
6. Check the remaining findings against the source code, input boundaries, build configuration, and tests.

Metis supplies the review workflow, source navigation, prompts, validation stages, and output handling. The model provider supplies the reasoning model. Results can vary between models and providers even when the source code is unchanged.

## Choose the review scope

Use the narrowest scope that answers your review question:

- `review_code` reviews files selected from the codebase and is useful for a broad first pass.
- `review_dir` focuses on one directory.
- `review_file` focuses on one source file while retaining codebase context.
- `review_patch` focuses on changed code and is suited to pull-request or pre-merge review.

This Learning Path demonstrates `review_code` and `review_file` at the prompt started with `--interactive`. Direct review commands run their Initialize prerequisites automatically, so the exercises do not need a separate `init` command.

## Strengthen findings with automated triage

Review discovers candidate issues; triage assesses existing findings. Metis starts with a source window around the reported location. For C/C++, available CodeGraph context adds the enclosing function, callers, and callees. The model can use navigation tools to inspect missing definitions, macros, or guards, then decide whether the evidence supports the finding (`valid`), refutes it (`invalid`), or cannot settle it (`inconclusive`). Keyword rules do not override these verdicts.

In the built-in workflow, both `valid` and `invalid` require citations and a resolution chain. Metis checks that cited lines were displayed to the model for that finding, remain inside the codebase, and match current source. Unusable citations produce `inconclusive`. These checks validate citation provenance, not the semantic truth of the model's reasoning; even `valid` is not proof of a working exploit.

Without `--interactive`, Metis 2.0.0 runs the full configured graph. The packaged graph includes Initialize, Review, and Triage, so it triages findings automatically. In interactive mode, `--triage` optionally chains Triage after `review_code`, `review_dir`, `review_file`, or `review_patch`; the `triage` command can instead assess an existing Metis review JSON or SARIF report.

Automated triage can consume additional model tokens. These exercises use `--interactive` without `--triage` so you can inspect review-only findings and practice manual triage. See the [Metis 2.0.0 triage flow](https://github.com/arm/metis/blob/metis-v2.0.0/docs/triage-flow.md) for decisions, citation validation, and report annotations.

## Configure the workflow with graph YAML

The execution graph describes the workflow, not the source code's call graph. In `metis.yaml`, `metis_engine.execution` selects stages and their nodes. The packaged graph runs `initialize` to prepare context and build the CodeGraph, `review` to run simple LLM review and deduplicate findings, and `triage` to assess Review's SARIF findings. Input bindings pass data and establish dependencies; `depends_on` adds ordering without passing a value.

The exercises configure only the model provider and inherit this graph. An explicit `execution` section replaces the whole packaged graph rather than merging individual nodes. To customize it or enable reachability, start from the [Metis 2.0.0 execution-graph configuration](https://github.com/arm/metis/blob/metis-v2.0.0/docs/execution-graph.md#default-graph) and retain the required stages, outputs, and dependencies.

## Interpret Metis findings

A Metis finding normally includes the issue, source location, reasoning, suggested mitigation, Common Weakness Enumeration (CWE) identifier, severity, and confidence. These fields provide a starting point for you to then investigate the findings.

{{% notice Note %}}
CWE identifiers, such as `CWE-190` for integer overflow, provide standard names for common classes of software weakness.
{{% /notice %}}

The main benefit is that Metis can reduce the amount of source navigation you do before a review becomes in-depth. You still decide whether a candidate is reachable, exploitable, already mitigated, or worth fixing.

For each finding, ask:

- Can untrusted data reach the reported value or operation?
- Does the build configuration include the reported code?
- Are the arithmetic limits and platform assumptions correct?
- Does an existing check or caller contract invalidate the report?
- Can you reproduce the behavior with a focused test or sanitizer?
- Does the proposed mitigation preserve intended behavior?

You will apply these questions to the libpng report later in the Learning Path.

## What you've learned and what's next

You have seen how default simple LLM review and optional reachability review find candidates, how automated triage assesses the evidence, and why human validation is still needed. Next, you will install the tested release and add your provider API key.
