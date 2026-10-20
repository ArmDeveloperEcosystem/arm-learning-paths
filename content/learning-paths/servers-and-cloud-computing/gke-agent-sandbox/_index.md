---
title: Run agent-generated Python in GKE Agent Sandbox on Google Axion

author: Jason Andrews

description: Run Python workloads on Google Axion with GKE Agent Sandbox, then connect Antigravity for remote Linux execution.

minutes_to_complete: 90

who_is_this_for: This is an advanced topic for developers who use coding agents and want to run agent-generated Python in an isolated Arm Linux workspace on Google Kubernetes Engine (GKE).

learning_objectives:
    - Create a GKE sandbox warm pool on Google Axion processors.
    - Verify non-root execution and filesystem restrictions, then inspect the sandbox's user, filesystem, and Linux environment interactively.
    - Run a CSV analysis Python program in the sandbox and retrieve the results.
    - Connect Antigravity CLI and run agent-generated Python in a remote GKE sandbox.

prerequisites:
    - A Google Cloud project with billing enabled and permission to create GKE clusters, node pools, and VPC networks
    - An Ubuntu Linux or macOS local machine with internet access, a route to the GKE API endpoint, and permission to install the required tools
    - Familiarity with Bash, Python, and Kubernetes Pods
    - A Google account for [Antigravity CLI](/install-guides/antigravity/) authentication

generate_summary_faq: true
rerun_summary: false
rerun_faqs: false
skilllevels: Advanced
subjects: Containers and Virtualization
armips:
    - Neoverse
platforms:
    - Google Axion
tools_software_languages:
    - Google Kubernetes Engine
    - gVisor
    - Python
    - Antigravity
    - Model Context Protocol
operatingsystems:
    - Linux
    - macOS

further_reading:
    - resource:
        title: Enable Agent Sandbox on GKE
        link: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/how-install-agent-sandbox
        type: documentation
    - resource:
        title: GKE Sandbox isolation model
        link: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods
        type: documentation
    - resource:
        title: Arm workloads on GKE
        link: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/arm-on-gke
        type: documentation
    - resource:
        title: Antigravity MCP configuration
        link: https://www.antigravity.google/docs/mcp/
        type: documentation
    - resource:
        title: Antigravity permissions
        link: https://www.antigravity.google/docs/permissions/
        type: documentation

### FIXED, DO NOT MODIFY
weight: 1
layout: learningpathall
learning_path_main_page: "yes"
---
