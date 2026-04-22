---
title: Migrate MySQL from on-premises x64 to Azure Cobalt 100 Arm VMs

description: Learn how to migrate a MySQL database from an on-premises x64 environment to an Arm-based Azure Cobalt 100 VM and validate performance with sysbench.

draft: true
cascade:
    draft: true

minutes_to_complete: 30   

who_is_this_for: This Learning Path is for developers who want to migrate MySQL from an on-premises x64 environment to an Arm-based Azure Cobalt 100 virtual machine.

learning_objectives: 
    - Provision an Arm-based Azure Cobalt 100 virtual machine by using Terraform and Azure CLI.
    - Export and restore a MySQL database from an on-premises x64 simulator into the Arm VM.
    - Run sysbench on the migrated database and interpret key performance metrics.

prerequisites:
    - A [Microsoft Azure](https://azure.microsoft.com/) account with access to Cobalt 100 based instances (Dpsv6)
    - Basic familiarity with SSH and MySQL command-line tools


author: Doug Anson

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
cloud_service_providers:
  - Microsoft Azure

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
      link: https://manpages.ubuntu.com/manpages/trusty/man1/sysbench.1.html 
      type: documentation


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
