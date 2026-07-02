---
title: Automate MCP server testing using Pytest and Testcontainers

description: Learn how to automate integration testing of MCP servers using Testcontainers and PyTest, with hands-on examples and GitHub Actions CI/CD configuration.

minutes_to_complete: 60

who_is_this_for: This is an introductory topic for software developers and QA engineers who want to automate integration testing of Model Context Protocol (MCP) servers using Testcontainers and PyTest.

learning_objectives:
    - Set up Testcontainers with PyTest for containerized testing of MCP servers
    - Write and run integration tests that validate MCP server functionality
    - Configure GitHub Actions to automate MCP server testing in CI/CD pipelines

prerequisites:
    - A computer with [Docker](/install-guides/docker/) and Python 3.11 or later installed
    - Basic familiarity with Python, PyTest, and container concepts
    - Familiarity with the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) specification

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-02T17:12:52Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 597877722e5f277e5558e29ecd33878ac2262b70a84a9769325b3c3b0ce06e58
  summary_generated_at: '2026-07-02T17:12:52Z'
  summary_source_hash: 597877722e5f277e5558e29ecd33878ac2262b70a84a9769325b3c3b0ce06e58
  faq_generated_at: '2026-07-02T17:12:52Z'
  faq_source_hash: 597877722e5f277e5558e29ecd33878ac2262b70a84a9769325b3c3b0ce06e58
  summary: >-
    You'll automate integration testing of Model Context Protocol (MCP)
    servers using PyTest and Testcontainers. First, you'll prepare a Python and Docker environment,
    verify Docker availability, and run a short Testcontainers example to start a disposable container
    and execute commands inside it. Then, you'll build a minimal integration test suite for
    the Arm MCP server, focusing on JSON-RPC 2.0 communication over standard input and output.
    Finally, you'll add a GitHub Actions workflow to run the tests on every push and pull request
    using native arm64 runners with Docker. By the end, you'll have containerized tests that validate
    MCP server behavior locally and in continuous integration.
  faqs:
  - question: How do I know Docker is ready before running the examples?
    answer: >-
      Run `docker info` and confirm it returns configuration details without errors. If it fails,
      start the Docker daemon and retry.
  - question: What should I expect when I run the basic Testcontainers example?
    answer: >-
      It starts a long-running container, executes a command inside it, and then cleans up when
      the script ends. Seeing the command output and a clean exit indicates the example worked.
  - question: How do the integration tests communicate with an MCP server?
    answer: >-
      MCP uses JSON-RPC 2.0 over standard input/output, so tests exchange JSON-RPC messages with
      the server process. When containerized, Testcontainers manages the server lifecycle during
      each test run.
  - question: Where can I find a complete reference implementation of the tests?
    answer: >-
      A full test implementation is available in the Arm MCP repository under `mcp-local/tests/`.
      You can consult those files while building your own suite.
  - question: Which events should trigger the GitHub Actions workflow, and where is it defined?
    answer: >-
      The workflow runs on `push` and `pull_request` and is defined at `.github/workflows/integration-tests.yml`.
      GitHub’s native Arm64 runners include Docker.
# END generated_summary_faq

author: Neethu Elizabeth Simon

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: CI-CD
armips:
    - Neoverse
    - Cortex-A
operatingsystems:
    - Linux
    - macOS
    - Windows
tools_software_languages:
    - Python
    - Pytest
    - Docker
    - GitHub Actions
    - Testcontainers
    - MCP

shared_path: true
shared_between:
    - servers-and-cloud-computing
    - laptops-and-desktops

further_reading:
    - resource:
        title: Arm MCP Server GitHub Repository
        link: https://github.com/arm/mcp
        type: website
    - resource:
        title: Testcontainers for Python Documentation
        link: https://testcontainers-python.readthedocs.io/
        type: documentation
    - resource:
        title: Model Context Protocol Specification
        link: https://modelcontextprotocol.io/
        type: website
    - resource:
        title: PyTest Documentation
        link: https://docs.pytest.org/
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
