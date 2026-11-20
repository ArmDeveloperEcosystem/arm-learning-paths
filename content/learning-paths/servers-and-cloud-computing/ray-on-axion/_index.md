---
title: Scale AI workloads with Ray on an Arm-based Google Cloud C4A VM
description: Deploy and run distributed AI workloads using Ray on Google Cloud C4A Arm-based VMs powered by Axion, covering parallel tasks, hyperparameter tuning, and model serving with Ray Core, Train, Tune, and Serve.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for DevOps engineers, ML engineers, and software developers who want to deploy and run distributed workloads using Ray on SUSE Linux Enterprise Server (SLES) Arm64, run parallel tasks, perform hyperparameter tuning, and serve models at scale.

learning_objectives:
    - Install and configure Ray on Google Cloud C4A Axion processors for Arm64.
    - Run distributed tasks and parallel workloads using Ray Core.
    - Perform distributed training and hyperparameter tuning using Ray Train and Ray Tune.
    - Deploy scalable APIs using Ray Serve and validate end-to-end execution.

prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free) account with billing enabled
  - Basic familiarity with Python and distributed systems concepts

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-11-19T16:02:33Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: c4924540b24617061378fbf4f2037973c30cd2b5a3dec1de80119721fa618d6a
  summary_generated_at: '2026-11-19T16:02:33Z'
  summary_source_hash: c4924540b24617061378fbf4f2037973c30cd2b5a3dec1de80119721fa618d6a
  faq_generated_at: '2026-11-19T16:02:33Z'
  faq_source_hash: c4924540b24617061378fbf4f2037973c30cd2b5a3dec1de80119721fa618d6a
  summary: >-
    You'll run Ray on a single Google Cloud C4A VM with SUSE Linux. You'll provision a
    `c4a-standard-4` instance and configure firewall access for the Ray Dashboard and Ray Serve.
    After installing Ray, you'll initialize the runtime and run `ray_test.py` to verify parallel
    tasks. You'll then explore distributed training and hyperparameter tuning, using task output
    and the Ray Dashboard to inspect execution.
  faqs:
  - question: Which Google Cloud machine type should I select?
    answer: >-
      Choose `c4a-standard-4`, which provides four vCPUs and 16 GB of memory.
  - question: How do I verify that Ray runs on the virtual machine?
    answer: >-
      Run `ray_test.py`. You should see `Results:` followed by squared values from 0 through
      81.
  - question: Which ports do I need for Ray Dashboard and Ray Serve?
    answer: >-
      Allow TCP port `8265` for the Dashboard and TCP port `8000` for Serve. Check that the
      firewall rule applies to your VM. Use its external IP to connect.
  - question: Do I need a multi-node cluster?
    answer: >-
      No. You can complete these steps on one C4A VM with a single-node Ray runtime.
  - question: What should I check if I can't connect to the Ray cluster?
    answer: >-
      Check whether you started the Ray head node with `ray start --head`, then run `ray
      status` to inspect the cluster before retrying your script.
# END generated_summary_faq

author: Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

##### Tags
skilllevels: Introductory
subjects: AI/ML
platforms:
  - Google Axion

armips:
  - Neoverse

tools_software_languages:
  - Ray
  - Python
  - PyTorch

operatingsystems:
  - Linux

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================

further_reading:
  - resource:
      title: Ray official documentation
      link: https://docs.ray.io/
      type: documentation

  - resource:
      title: Ray GitHub repository
      link: https://github.com/ray-project/ray
      type: documentation

  - resource:
      title: PyTorch documentation
      link: https://pytorch.org/docs/stable/index.html
      type: documentation

weight: 1
layout: "learningpathall"
learning_path_main_page: yes
---

