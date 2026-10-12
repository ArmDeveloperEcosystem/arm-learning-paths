---
title: Manage the machine learning lifecycle with MLflow on a Google Cloud C4A Axion virtual machine

description: Set up MLflow on Google Cloud C4A Axion Arm VMs running SUSE Linux to track ML experiments, version models with the Model Registry, and deploy a trained model as a REST API.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for DevOps engineers, ML engineers, and software developers who want to manage the machine learning lifecycle using MLflow on SUSE Linux Enterprise Server (SLES) Arm64, track experiments, version models, and deploy models as scalable APIs.

learning_objectives:
    - Install and configure MLflow on an Arm-based Google Cloud C4A virtual machine (VM).
    - Track experiments, log metrics, and compare runs using MLflow Tracking.
    - Manage and version models using the MLflow Model Registry.
    - Deploy models as APIs and validate end-to-end ML workflows.

prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free) account with billing enabled
  - Basic familiarity with Python and machine learning concepts

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-28T19:51:43Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 41aedb5bead9c642212381adcb6c73040930e7f068a7553b2c08ff53ce077f3f
  summary_generated_at: '2026-09-28T19:51:43Z'
  summary_source_hash: 41aedb5bead9c642212381adcb6c73040930e7f068a7553b2c08ff53ce077f3f
  faq_generated_at: '2026-09-28T19:51:43Z'
  faq_source_hash: 41aedb5bead9c642212381adcb6c73040930e7f068a7553b2c08ff53ce077f3f
  summary: >-
    You'll manage the machine learning lifecycle with MLflow on a Google Axion C4A virtual machine. First, you'll
    provision a SUSE Linux VM, configure firewall access, and install MLflow with Python 3.11. Then, you'll
    start the tracking server, run experiments, and compare logged metrics. Finally, you'll register model
    versions and aliases, start model serving, and validate the deployment through the MLflow interface
    and REST API predictions.
  faqs:
  - question: Which VM configuration should I select for this setup?
    answer: >-
      Select a Google Axion C4A instance with the `c4a-standard-4` machine type, which provides
      four vCPUs and 16 GB of memory. Use SUSE Linux for the VM.
  - question: What firewall rules do I need before launching MLflow?
    answer: >-
      Allow inbound TCP access to port `5000` for the MLflow interface and port `6000` for the
      model-serving API. Attach the firewall rule to your VM through its network tag.
  - question: How do I know that the MLflow tracking server is running?
    answer: >-
      Check the startup log for the listening address, then open `http://<VM-IP>:5000`. You should
      see the MLflow interface after the server starts.
  - question: Why do I need to set MLFLOW_TRACKING_URI?
    answer: >-
      Set `MLFLOW_TRACKING_URI` to direct your MLflow client to the tracking server instead of
      a local directory. Run `export MLFLOW_TRACKING_URI=http://127.0.0.1:5000`.
  - question: How can I confirm that my model is registered and served correctly?
    answer: >-
      Confirm that your model appears in the MLflow Model Registry with a version and assigned
      alias. Then, call the REST endpoint and verify that its response contains predictions from
      the served model.
# END generated_summary_faq

author: Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

##### Tags
skilllevels: Introductory
subjects: ML
platforms:
  - Google Axion

armips:
  - Neoverse

tools_software_languages:
  - MLflow
  - Python
  - scikit-learn

operatingsystems:
  - Linux

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================

further_reading:
  - resource:
      title: MLflow official documentation
      link: https://mlflow.org/docs/latest/index.html
      type: documentation

  - resource:
      title: MLflow GitHub repository
      link: https://github.com/mlflow/mlflow
      type: documentation

  - resource:
      title: Scikit-learn documentation
      link: https://scikit-learn.org/stable/
      type: documentation

weight: 1
layout: "learningpathall"
learning_path_main_page: yes
---
