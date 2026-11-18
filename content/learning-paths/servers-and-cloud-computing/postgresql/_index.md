---
title: Deploy PostgreSQL on Arm

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for software developers who want to deploy PostgreSQL on Arm.

learning_objectives: 
    - Identify various ways that PostgreSQL can be deployed on Arm.
    - Interact with a PostgreSQL database using the psql client tool.

prerequisites:
    - An Arm based instance from a cloud service provider, or an on-premise Arm server.
    - If you do not have an Arm node, the next section discusses some options.

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-11-18T20:25:15Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 95fb3d07b9161c973aed512687c3a2bd70e974e52df15e7a07bbb97725bf6f35
  summary_generated_at: '2026-11-18T20:25:15Z'
  summary_source_hash: 95fb3d07b9161c973aed512687c3a2bd70e974e52df15e7a07bbb97725bf6f35
  faq_generated_at: '2026-11-18T20:25:15Z'
  faq_source_hash: 95fb3d07b9161c973aed512687c3a2bd70e974e52df15e7a07bbb97725bf6f35
  summary: >-
    You'll review ways to run PostgreSQL on Arm, including bare metal, cloud VMs, and managed
    services. First, you'll compare deployment options and identify the relevant installation
    documentation for your environment. Then, you'll inspect the PostgreSQL build configuration
    with `pg_config`. Finally, you'll connect to a database with `psql` and try SQL commands to check that
    your database responds.
  faqs:
  - question: Which PostgreSQL deployment option should I choose on Arm?
    answer: >-
      Review the self-managed options for bare metal or cloud VMs if you need control over the
      server. Consider a managed service if you prefer provider-operated maintenance.
  - question: How do I know PostgreSQL started correctly?
    answer: >-
      After you install PostgreSQL, use `psql` to connect to the database. A successful prompt
      and basic SQL command show that your database responds.
  - question: Can I use psql with a managed PostgreSQL service?
    answer: >-
      Use the hostname of your managed service and credentials with `psql`, then run a basic query to
      check access.
  - question: How can I inspect the PostgreSQL build configuration?
    answer: >-
      Run `pg_config` on your Arm server. Check the `CONFIGURE` line for compiler and linker flags,
      including `CFLAGS`, `CXXFLAGS`, and `LDFLAGS`.
  - question: What should I check if psql can't connect?
    answer: >-
      Check that your server or managed endpoint is running and reachable. Verify the database
      name, user, and authentication settings before you retry `psql`.
# END generated_summary_faq

author: Jason Andrews

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Databases
platforms:
  - AWS Graviton
  - Microsoft Azure Cobalt
  - Google Axion
  - Oracle Cloud Infrastructure (OCI) Ampere Compute
armips:
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - SQL
    - PostgreSQL

further_reading:
    - resource:
        title: PostgreSQL Manual
        link: https://www.postgresql.org/docs/current/tutorial-install.html
        type: documentation

    - resource:
        title: Ansible
        link: https://docs.ansible.com/
        type: documentation 

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

