---
title: Run agent-generated Python in GKE Agent Sandbox on Google Axion

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-10-20T20:33:25Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 01c3d485119ac2dfa452ed8d87f46b0d4909b4a2a0076dd41a4f0a13dddddb3f
  summary_generated_at: '2026-10-20T20:33:25Z'
  summary_source_hash: 01c3d485119ac2dfa452ed8d87f46b0d4909b4a2a0076dd41a4f0a13dddddb3f
  faq_generated_at: '2026-10-20T20:33:25Z'
  faq_source_hash: 01c3d485119ac2dfa452ed8d87f46b0d4909b4a2a0076dd41a4f0a13dddddb3f
  summary: >-
    You'll run agent-generated Python in GKE Agent Sandbox on Google Axion, with local
    tools directing work into an isolated Arm Linux environment. First, you'll prepare your
    client and provision a GKE cluster with an Axion node pool. Then, you'll create a sandbox
    warm pool, claim a sandbox, and verify its restrictions. Next, you'll correct a failing CSV
    analysis and retrieve reports. You'll then inspect the environment interactively, connect
    Antigravity to run code remotely, and clean up cloud resources.
  # faqs:
  # - question: Which node pool should I use to run sandboxes on Google Axion?
  #   answer: >-
  #     Use the Arm gVisor pool backed by `c4a-standard-2` machines. The provided
  #     `sandbox.yaml` selects that node pool for your Python sandbox workloads.
  # - question: What should I set in my terminal before running the cluster commands?
  #   answer: >-
  #     Keep `LP_WORKDIR` set and run `cd "$LP_WORKDIR"` before continuing. If you open
  #     a new terminal, source `env.sh` if you saved it, or re-export variables such as
  #     `LOCATION`, `REGION`, `CLUSTER_NAME`, `NODE_POOL_NAME`, and `MACHINE_TYPE`.
  # - question: How do I verify the sandbox runs as non-root and has restricted filesystem access?
  #   answer: >-
  #     Run the Python test and check that it reports UID 1000. You should also see a
  #     denied write under `/etc` and a successful write to `/workspace`. Later, use
  #     `kubectl exec` to inspect the running sandbox interactively.
  # - question: What result should I expect from the CSV analysis demo?
  #   answer: >-
  #     Your first run with `analyze_sales_initial.py` fails as expected. The runner
  #     replaces it with `analyze_sales.py` in the same sandbox workspace, runs six
  #     tests, and retrieves `summary.json` and `report.html`.
  # - question: How do I keep Antigravity from running code on my local machine?
  #   answer: >-
  #     In `agy`, open `/permissions` and select **Project**. Allow
  #     `mcp(gke-sandbox/*)` and deny `command(*)`, `read_file(*)`, and
  #     `write_file(*)`. Check that your session uses the `gke-sandbox` tools.
# END generated_summary_faq

author: Jason Andrews

description: Run Python workloads on Google Axion with GKE Agent Sandbox, then connect Antigravity for remote Linux execution.

minutes_to_complete: 90

who_is_this_for: This is an advanced topic for developers who use coding agents and want to run agent-generated Python in an isolated Arm Linux workspace on Google Kubernetes Engine (GKE).

learning_objectives:
    - Create a GKE sandbox warm pool on Google Axion processors.
    - Verify non-root execution and filesystem restrictions, then inspect the sandbox user, filesystem, and Linux environment interactively.
    - Run a CSV analysis Python program in the sandbox and retrieve the results.
    - Connect Antigravity CLI and run agent-generated Python in a remote GKE sandbox.

prerequisites:
    - A Google Cloud project with billing enabled and permission to create GKE clusters, node pools, and VPC networks
    - An Ubuntu Linux or macOS local machine with internet access, a route to the GKE API endpoint, and permission to install the required tools
    - Familiarity with Bash, Python, and Kubernetes Pods
    - A Google account for [Antigravity CLI](/install-guides/antigravity/) authentication

generate_summary_faq: false
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
