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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T21:31:11Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 597877722e5f277e5558e29ecd33878ac2262b70a84a9769325b3c3b0ce06e58
  summary_generated_at: '2026-06-01T21:01:02Z'
  summary_source_hash: 597877722e5f277e5558e29ecd33878ac2262b70a84a9769325b3c3b0ce06e58
  faq_generated_at: '2026-06-02T21:31:11Z'
  faq_source_hash: 597877722e5f277e5558e29ecd33878ac2262b70a84a9769325b3c3b0ce06e58
  summary: >-
    This introductory path shows how to automate integration testing of Model Context Protocol
    (MCP) servers using PyTest and Testcontainers, with local runs and CI on GitHub Actions. You
    will set up a Python environment with Docker, run a basic Testcontainers example, and build
    a minimal integration test suite that exercises MCP server behavior over JSON-RPC 2.0 via
    standard input/output. You will also create a .github/workflows/integration-tests.yml workflow
    to run tests on pushes and pull requests, with support for Arm64 runners. The path targets
    Linux, macOS, and Windows, and expects Docker, Python 3.11 or later, Git, and familiarity
    with Python, PyTest, containers, and the MCP specification.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      Install Docker and Python 3.11 or later with virtual environment support, and have Git available.
      On Linux, ensure the python3-venv package is installed. You should also be familiar with
      Python, PyTest, container concepts, and the MCP specification.
  - question: How do I check if Docker is ready before I start?
    answer: >-
      Run the command docker info. If it fails or shows that the daemon is not running, start
      the Docker daemon and try again.
  - question: How do MCP servers communicate in these tests?
    answer: >-
      MCP uses JSON-RPC 2.0 over standard input and output. Your integration tests interact with
      the server through this protocol to validate functionality.
  - question: What result should I expect from the basic Testcontainers example?
    answer: >-
      The example starts an alpine:latest container running a long-lived sleep process and then
      executes a command inside it. You should see the container start successfully and the command
      complete while the container is alive.
  - question: Which triggers and runners does the GitHub Actions workflow use, and where is it
      defined?
    answer: >-
      The workflow is defined at .github/workflows/integration-tests.yml and runs on push and
      pull_request events. It uses GitHub’s native Arm64 runners with Docker pre-installed, and
      supports parallel execution.
# END generated_summary_faq

author: Neethu Elizabeth Simon

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

