---
title: Run MongoDB on Arm-based Azure Cobalt 100 instances

minutes_to_complete: 30   

who_is_this_for: This is an introductory topic for software developers who want to migrate MongoDB workloads to Arm-based platforms, with a focus on Microsoft Azure Cobalt 100 Arm64 instances.

description: Deploy MongoDB on Azure Cobalt 100-based Arm virtual machines (VMs) and benchmark database performance using mongotop and mongostat monitoring tools.

learning_objectives: 
    - Provision an Arm64-based VM in Azure that's powered by Cobalt 100 and uses Ubuntu Pro 24.04 LTS.
    - Deploy MongoDB on the Cobalt 100-based instance.
    - Run baseline tests and performance benchmarks on MongoDB in the Arm64 environment.

prerequisites:
    - A [Microsoft Azure](https://azure.microsoft.com/) account with access to Cobalt 100-based instances (Dpsv6)
    - Familiarity with the [MongoDB architecture](https://www.mongodb.com/) and deployment practices on Arm64 platforms

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-28T19:52:05Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: b5b5b07acc800d54023e63ec6b670fdd1750787cce37a508128fb5fb11a422e4
  summary_generated_at: '2026-09-28T19:52:05Z'
  summary_source_hash: b5b5b07acc800d54023e63ec6b670fdd1750787cce37a508128fb5fb11a422e4
  faq_generated_at: '2026-09-28T19:52:05Z'
  faq_source_hash: b5b5b07acc800d54023e63ec6b670fdd1750787cce37a508128fb5fb11a422e4
  summary: >-
    You'll deploy and monitor MongoDB on an Azure Cobalt 100-based VM. First, you'll provision a Dpsv6 instance
    with Ubuntu Pro 24.04 LTS, install MongoDB and `mongosh`, and configure `mongod` for local access.
    You'll validate CRUD, indexing, concurrency, and storage behavior with `mongosh` and `fio`. Finally,
    you'll generate load and use `mongotop` to observe per-collection read and write activity in real
    time.
  faqs:
  - question: Which Azure VM size and OS image should I select?
    answer: >-
      Select an Azure Cobalt 100-based VM from the Dpsv6 general-purpose series. In the Azure portal,
      choose Ubuntu Pro 24.04 LTS and set **VM architecture** to **Arm64**.
  - question: How do I confirm that MongoDB started correctly on the VM?
    answer: >-
      Start `mongod` locally and confirm that it binds to `127.0.0.1`. Connect with `mongosh`,
      run the service health checks, and review the MongoDB log for errors.
  - question: Why is access control disabled, and what should I change before allowing remote access?
    answer: >-
      Access control is disabled because `mongod` remains bound to `127.0.0.1`.
      Before you accept remote connections, set `--bind_ip` or `bindIp`, create users, and enable
      authorization.
  - question: What should be running before I start mongotop?
    answer: >-
      Ensure that `mongod` is bound to `127.0.0.1`, `long_system_load.js` is generating traffic
      in another terminal, and the MongoDB Database Tools are installed. Run `mongotop` while
      the workload is active.
  - question: What results should I expect from the baseline and monitoring steps?
    answer: >-
      Confirm that `fio` completes without errors and that your CRUD, index, and concurrency checks
      succeed in `mongosh`. While the workload runs, `mongotop` should update per-collection read
      and write times in real time.
# END generated_summary_faq

author: Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Databases
platforms:
  - Microsoft Azure Cobalt

armips:
    - Neoverse

tools_software_languages:
    - MongoDB
    - mongotop
    - mongostat

operatingsystems:
    - Linux

further_reading:
    - resource:
        title: MongoDB Manual
        link: https://www.mongodb.com/docs/manual/
        type: documentation
    - resource:
        title: MongoDB Performance Tool
        link: https://github.com/idealo/mongodb-performance-test#readme
        type: documentation
    - resource:        
        title: MongoDB on Azure
        link: https://azure.microsoft.com/en-us/solutions/mongodb
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
