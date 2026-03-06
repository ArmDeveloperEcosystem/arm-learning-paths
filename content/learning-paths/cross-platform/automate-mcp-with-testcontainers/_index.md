---
title: Automate MCP Server testing using Pytest and Testcontainers

minutes_to_complete: 60

who_is_this_for: This is an intermediate topic for anyone interested in automating their end-to-end testing of MCP (Model Context Protocol) servers using specialized software packages called TestContainers and PyTest. 

learning_objectives:
    - Understand how TestContainers work for containerized testing of MCP servers.
    - Write integration tests for MCP servers using PyTest and TestContainers.
    - Configure GitHub Actions to run MCP integration tests in CI/CD pipelines.

prerequisites:
    - A machine that can run Python 3 and Docker. 
    - Familiarity with [Docker](/install-guides/docker/) and container concepts.
    - Basic knowledge of Python and Pytest.
    - The [Arm MCP Server](https://github.com/arm/mcp) running with AI assistant client.

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
