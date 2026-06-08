---
title: Learn how to deploy PostgreSQL

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for software developers who want to deploy PostgreSQL on Arm.

learning_objectives: 
    - Learn about the various ways PostgreSQL can be deployed.
    - Learn how to interact with a PostgreSQL database using the psql client tool.

prerequisites:
    - An Arm based instance from a cloud service provider, or an on-premise Arm server.
    - If you do not have an Arm node, the next section discusses some options.

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:51:17Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: a60cc2148a83f919467076e9d5a49fc4c9cec85670a919c7ba044cba72bfe219
  summary_generated_at: '2026-06-02T04:48:33Z'
  summary_source_hash: a60cc2148a83f919467076e9d5a49fc4c9cec85670a919c7ba044cba72bfe219
  faq_generated_at: '2026-06-03T01:51:17Z'
  faq_source_hash: a60cc2148a83f919467076e9d5a49fc4c9cec85670a919c7ba044cba72bfe219
  summary: >-
    This introductory Learning Path shows how to deploy PostgreSQL on Arm-based infrastructure
    running Linux. In about 30 minutes, you will review deployment choices on Arm, including bare
    metal, cloud VMs, and SQL services from AWS, Microsoft Azure, Google Cloud, and Oracle. You
    will consider installation and configuration options, learn how to check your database, and
    use the psql client tool to interact with PostgreSQL. A prerequisite is access to an Arm-based
    instance from a cloud service provider or an on-premise Arm server; if you do not yet have
    an Arm node, the path outlines options. The content targets Arm server platforms, including
    Neoverse-based systems.
  faqs:
  - question: What do I need before running this Learning Path?
    answer: >-
      You need access to an Arm-based instance from a cloud provider or an on-premise Arm server.
      The path targets Linux. If you do not have an Arm node, the next section discusses options.
  - question: Which Arm deployment options does this path cover?
    answer: >-
      It discusses deploying PostgreSQL on bare metal, on cloud virtual machines, and via managed
      SQL services. Cloud providers listed include AWS, Microsoft Azure, Google Cloud, and Oracle.
  - question: Will I use the psql client, and for what?
    answer: >-
      Yes. You will use the psql client tool to interact with the PostgreSQL database, run SQL,
      and validate connectivity.
  - question: How do I know my PostgreSQL installation is working?
    answer: >-
      The steps include configuring and checking your PostgreSQL database, then connecting with
      psql. Successful connection and basic SQL interaction indicate that the database is running.
  - question: Can I skip any sections if I already have experience or hardware?
    answer: >-
      If you already know how to deploy PostgreSQL, you can skip this path and explore the Learn
      how to Tune PostgreSQL path. If you already have an Arm system, you can skip the subsection
      about Arm deployment options and continue reading.
# END generated_summary_faq

author: Jason Andrews
### Tags
skilllevels: Introductory
subjects: Databases
cloud_service_providers:
  - AWS
  - Microsoft Azure
  - Google Cloud
  - Oracle
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

