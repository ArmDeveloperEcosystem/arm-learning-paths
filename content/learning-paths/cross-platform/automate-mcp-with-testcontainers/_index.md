---
title: Automate MCP Server testing using Pytest and Testcontainers

draft: true
cascade:
    draft: true

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
