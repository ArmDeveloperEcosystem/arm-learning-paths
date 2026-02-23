---
title: Increase application performance with libhugetlbfs 

minutes_to_complete: 60

who_is_this_for: This is an advanced topic for engineers looking for ways to increase performance on Arm servers.

learning_objectives:
    - Enable libhugetlbfs on an Arm server running Linux
    - Evaluate performance improvements for workloads such as MySQL.

prerequisites:
    - An Arm server or virtual machine instance from a cloud service provider with Ubuntu installed
    - Knowledge of how to build a MySQL server and run the sysbench benchmark test

author: Bolt Liu

skilllevels: Advanced
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
    - MySQL
    - GCC
    - Runbook


test_images:
    - ubuntu:latest
test_link: null
test_maintenance: false

further_reading:
    - resource:
        title: libhugetlbfs manual page
        link: https://linux.die.net/man/7/libhugetlbfs
        type: documentation
    - resource:
        title: libhugetlbfs HOW TO
        link: https://github.com/libhugetlbfs/libhugetlbfs/blob/master/HOWTO
        type: documentation


weight: 1
layout: learningpathall
learning_path_main_page: 'yes'
---
