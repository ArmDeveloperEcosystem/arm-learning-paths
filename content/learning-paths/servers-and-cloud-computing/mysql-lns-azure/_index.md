---
title: Migrate MySQL from on-premises x64 to Arm-based Azure virtual machines

description: Learn how to migrate a MySQL database from an on-premises x64 environment to an Arm-based Azure Cobalt 100 VM and validate performance with sysbench.

minutes_to_complete: 30

who_is_this_for: This Learning Path is for developers who want to migrate MySQL from an on-premises x64 environment to an Arm-based virtual machine (VM) powered by Azure Cobalt 100.

learning_objectives: 
    - Provision an Arm-based Azure VM powered by Cobalt 100 using Terraform and Azure CLI.
    - Export and restore a MySQL database from an on-premises x64 simulator into the Arm VM.
    - Run sysbench on the migrated database and interpret key performance metrics.

prerequisites:
    - A [Microsoft Azure](https://azure.microsoft.com/) account with access to Cobalt 100 based instances (Dpsv6)
    - Basic familiarity with SSH and MySQL command-line tools

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-10-01T19:36:51Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: d6d2cda672e5ed693210356f269aa015cb9b3b80fc92c9c33c200e6d83717b15
  summary_generated_at: '2026-10-01T19:36:51Z'
  summary_source_hash: d6d2cda672e5ed693210356f269aa015cb9b3b80fc92c9c33c200e6d83717b15
  faq_generated_at: '2026-10-01T19:36:51Z'
  faq_source_hash: d6d2cda672e5ed693210356f269aa015cb9b3b80fc92c9c33c200e6d83717b15
  summary: >-
    You'll migrate a MySQL database from a simulated on-premises x64 server to an Arm-based Azure VM powered by Cobalt
    100. First, you'll prepare the source VM, install the required tools, and load a sample
    database. You'll then configure and run the migration scripts to provision the target and restore
    the database. Finally, you'll connect to the Arm VM, run a `sysbench` workload, and review the
    results.
  faqs:
  - question: Which architecture should I choose for the on-premises simulator VM?
    answer: >-
      Choose x64 for the simulator VM. It acts as the on-premises MySQL source that you migrate
      from.
  - question: Where do I run the migration scripts, and what SSH key do they generate?
    answer: >-
      Run the scripts from the downloaded asset repository, for example in `$HOME/lift-n-shift-assets`.
      The `scripts/create_ssh_key.sh` script generates an SSH key pair in `$HOME/.ssh` and prints the public
      key. Press **Enter** to leave the passphrase empty, and save the printed `ssh-rsa`
      public key string for use with the Azure VM.
  - question: Where can I find the password requested when restoring the database on the cloud VM?
    answer: >-
      Open a second SSH session to the Arm-based Azure VM. Run `sudo su -`, then
      `cat /root/mysql_root_password.txt` to retrieve the password. Enter it at the restore
      prompt in your original session on the on-premises simulator.
  - question: How do I connect to the Arm-based Azure VM before running the benchmark, and which
      user and key should I use?
    answer: >-
      From the on-premises simulator, SSH to the Arm VM using the key created in `$HOME/.ssh`
      and the `azureadmin` user at the VM’s public IP. Use the filename that you identified for the Azure
      cloud key.
  - question: Where should I create and run the benchmarking script, and what result should I
      expect?
    answer: >-
      Create and run the script, for example `run.sh`, on the Arm-based Azure VM after
      connecting with SSH. Expect `sysbench` to produce a summary of performance metrics that you
      can review to validate the migrated database.
# END generated_summary_faq

author: Doug Anson

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
    - MySQL
    - Terraform
    - Azure CLI
    - sysbench
    - Bash

operatingsystems:
    - Linux

further_reading:
  - resource:
      title: Azure Virtual Machines documentation
      link: https://learn.microsoft.com/en-us/azure/virtual-machines/
      type: documentation
  - resource:
      title: Copying MySQL databases to another machine
      link: https://dev.mysql.com/doc/refman/8.4/en/copying-databases.html
      type: documentation
  - resource:
      title: mysqldump reference
      link: https://dev.mysql.com/doc/refman/8.4/en/mysqldump.html
      type: documentation
  - resource:
      title: sysbench benchmarking tools for MySQL
      link: https://github.com/akopytov/sysbench
      type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
