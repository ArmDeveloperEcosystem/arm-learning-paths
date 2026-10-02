---
title:  Deploy Node.js on Google Cloud C4A Arm-based Axion virtual machines

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for software developers migrating Node.js workloads from x86_64 to Arm-based servers, specifically on Google Cloud C4A virtual machines (VMs) built on Axion processors.

learning_objectives:
  - Provision an Arm-based SUSE Linux Enterprise Server VM on Google Cloud C4A instances with Axion processors.
  - Install and configure Node.js on a SUSE Arm64 (C4A) instance.
  - Validate Node.js functionality with baseline HTTP server tests.
  - Benchmark Node.js performance using Autocannon on Arm64 (AArch64) architecture.

prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free) account with billing enabled
  - Familiarity with networking concepts and [Node.js event-driven architecture](https://nodejs.org/en/docs/guides/event-loop-timers-and-nexttick)

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-10-01T19:41:01Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: c21d775ef47f9befc1046df0d89f746550a180b29974c45261e0478f59df503e
  summary_generated_at: '2026-10-01T19:41:01Z'
  summary_source_hash: c21d775ef47f9befc1046df0d89f746550a180b29974c45261e0478f59df503e
  faq_generated_at: '2026-10-01T19:41:01Z'
  faq_source_hash: c21d775ef47f9befc1046df0d89f746550a180b29974c45261e0478f59df503e
  summary: >-
    You'll deploy and benchmark a Node.js workload on an Arm-based Google Cloud C4A VM.
    First, you'll provision a SUSE Linux Enterprise Server instance on Google Axion, then install Node.js
    with Node Version Manager (NVM). You'll then validate the runtime in the read-eval-print loop (REPL)
    and with a minimal HTTP server. Finally, you'll use Autocannon to measure request throughput
    and latency and capture a baseline for the VM.
  faqs:
  - question: Which VM options should I select when creating the instance?
    answer: >-
      Use a C4A machine type, such as `c4a-standard-4` with four vCPUs and 16 GB. Select a SUSE Linux
      Enterprise Server image for Arm64.
  - question: How do I select Node.js v24 for new terminal sessions?
    answer: >-
      After installing Node.js with `nvm install v24`, add `nvm use v24` to your `~/.bashrc` file.
      Place it after the commands that load NVM so that new Bash sessions select Node.js v24.
  - question: How do I confirm that Node.js is working before I benchmark?
    answer: >-
      Run the REPL test to print a message and start the sample HTTP server. Proceed when the
      server responds to an HTTP request on the configured port.
  - question: What URL should I pass to Autocannon?
    answer: >-
      Use the address and port where your sample Node.js server is listening, such as `localhost`
      with the configured port. Run Autocannon against that endpoint to collect results.
  - question: How can I change the load and duration of the Autocannon benchmark?
    answer: >-
      Adjust `-c` to set the number of concurrent connections and `-d` to set the test duration
      in seconds. The example uses `-c 100 -d 10` to run 100 concurrent connections for ten seconds.
# END generated_summary_faq

author: Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

##### Tags
skilllevels: Introductory
subjects: Web
platforms:
  - Google Axion

armips:
  - Neoverse

tools_software_languages:
  - Node.js
  - npm
  - Autocannon

operatingsystems:
  - Linux

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
further_reading:
  - resource:
      title: Google Cloud documentation
      link: https://cloud.google.com/docs
      type: documentation

  - resource:
      title: Node.js documentation
      link: https://nodejs.org/en
      type: documentation

  - resource:
      title: Autocannon documentation
      link: https://www.npmjs.com/package/autocannon/v/5.0.0
      type: documentation

weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
