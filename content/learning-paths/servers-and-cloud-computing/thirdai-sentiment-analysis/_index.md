---
title: Run Text Classification with ThirdAI on Arm servers

minutes_to_complete: 10

who_is_this_for: This is for software developers who want to learn how to run text classification tasks with ThirdAI on Arm servers.

learning_objectives: 
    - Train, evaluate, and deploy a ThirdAI model.
    - Set up your Arm server for text classification tasks with ThirdAI.

prerequisites:
    - An [Arm-based instance](/learning-paths/servers-and-cloud-computing/csp/) from a cloud service provider or an on-premise Arm server.

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T02:10:25Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 0aaee75d902b938e63e37eca421dd28b91f583e784acdf3cccb1e20b8dda71bd
  summary_generated_at: '2026-06-02T05:17:40Z'
  summary_source_hash: 0aaee75d902b938e63e37eca421dd28b91f583e784acdf3cccb1e20b8dda71bd
  faq_generated_at: '2026-06-03T02:10:25Z'
  faq_source_hash: 0aaee75d902b938e63e37eca421dd28b91f583e784acdf3cccb1e20b8dda71bd
  summary: >-
    Learn how to run a text classification workflow with ThirdAI on Arm servers running Linux.
    You will provision an Arm-based instance in the cloud (AWS, Microsoft Azure, Google Cloud,
    or Oracle) or use an on-prem Arm server, install Python and ThirdAI, create a virtual environment,
    and follow an introductory example to train, evaluate, and deploy a model. The steps use Ubuntu
    commands, though other Linux distributions can be used. By the end, you will have a trained
    and evaluated text classifier and know how to invoke ThirdAI’s high-level APIs to make predictions.
    No explicit prerequisites are listed beyond access to an Arm-based server.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need access to an Arm-based instance from a cloud service provider or an on-premise
      Arm server. The steps assume a Linux environment.
  - question: Can I follow the instructions on Linux distributions other than Ubuntu?
    answer: >-
      Yes. The instructions show Ubuntu commands, but you can use other Linux distributions.
  - question: Which setup commands prepare Python and an isolated environment?
    answer: >-
      Install python3-pip and python3-venv, then create and activate a virtual environment. The
      terminal prompt showing a (thirdai) prefix indicates the environment is active.
  - question: How do I install and activate ThirdAI for this example?
    answer: >-
      Install the package inside the virtual environment with pip3 install thirdai. The evaluation
      script includes a thirdai.licensing.activate(...) call; use that line as shown in the example.
  - question: How do I evaluate the trained model and what result should I expect?
    answer: >-
      Use the provided evaluate.py script to load the saved model (sentiment_analysis.model) and
      run evaluation on the test file (amazon_polarity_test.csv). The script reports categorical_accuracy
      and includes a sample prediction; specific metric values are not listed.
# END generated_summary_faq

author: ThirdAI

### Tags
skilllevels: Introductory
subjects: ML
cloud_service_providers:
  - AWS
  - Microsoft Azure
  - Google Cloud
  - Oracle
armips:
    - Neoverse
tools_software_languages:
    - Python
    - ThirdAI
operatingsystems:
    - Linux


further_reading:
    - resource:
        title: ThirdAI Demos Repository
        link: https://github.com/ThirdAILabs/Demos
        type: documentation
    - resource:
        title: ThirdAI Website
        link: https://www.thirdai.com
        type: blog



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

