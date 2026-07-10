---
title: Build IoT Solutions in Azure for Arm Devices

description: Learn how to build a complete IoT solution in Azure that streams, stores, monitors, aggregates, and visualizes telemetry data from Arm devices using IoT Hub, Stream Analytics, Cosmos DB, and Azure Functions.

minutes_to_complete: 180

who_is_this_for: This is an advanced topic for developers who want to build a comprehensive IoT solution in Azure that streams, stores, monitors, aggregates, and visualizes telemetry data from Arm IoT devices.

learning_objectives:
    - Set up and configure Azure IoT Hub for device communication.
    - Register an IoT device and stream telemetry data using the Azure IoT SDK.
    - Route IoT data to Azure services using Azure Stream Analytics.
    - Store incoming data in Azure Cosmos DB through a Stream Analytics job.
    - Monitor data and send alerts using an Azure Function that reads from Cosmos DB and triggers notifications based on thresholds.
    - Aggregate sensor readings using an Azure Function that calculates average values from stored data.
    - Publish aggregated data to a public-facing web app hosted on Azure Blob Storage.

prerequisites:
    - A machine with Python 3 and Visual Studio Code installed
    - An active Azure account with sufficient permissions to create resources (such as IoT Hub, Functions, and Cosmos DB)

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-08T15:24:58Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 0e653bdbf5e5b08a6a00ba68e5ed215a0082e22c634d7d632d088851d48bb01c
  summary_generated_at: '2026-07-08T15:24:58Z'
  summary_source_hash: 0e653bdbf5e5b08a6a00ba68e5ed215a0082e22c634d7d632d088851d48bb01c
  faq_generated_at: '2026-07-08T15:24:58Z'
  faq_source_hash: 0e653bdbf5e5b08a6a00ba68e5ed215a0082e22c634d7d632d088851d48bb01c
  summary: >-
    You'll build a complete Azure-based IoT pipeline for Arm
    devices. First, you'll create an Azure IoT Hub, implement a Python simulator that emits temperature,
    pressure, humidity, and timestamp readings, and stream telemetry securely into the cloud.
    Then, you'll configure Azure Stream Analytics to query, transform, and route events, and persist
    processed data to Azure Cosmos DB. You'll extend the pipeline with Azure Functions for
    monitoring thresholds and aggregating sensor values, and conclude by publishing aggregated
    results to a static web app on Azure Blob Storage. You'll choose how to shape messages and
    what to store, and validate the flow at each stage.
  faqs:
  - question: How do I know the Python telemetry simulator is sending data to Azure IoT Hub?
    answer: >-
      Run the simulator and verify that downstream services receive events. A quick check is to
      confirm that the Stream Analytics job connected to the IoT Hub input observes incoming records.
  - question: Which fields should my Stream Analytics query select from incoming messages?
    answer: >-
      The simulator emits temperature, pressure, humidity, and a timestamp. Select these fields
      and any additional metadata you need for storage in Cosmos DB or for later functions and
      visualization.
  - question: What should I check if the Stream Analytics job shows no output?
    answer: >-
      Confirm that IoT Hub is configured as the input, the simulator is running, and your query
      actually returns rows. Also verify that the job has a valid output configured for the next
      stage, such as Cosmos DB.
  - question: How can I confirm data is being stored correctly in Azure Cosmos DB?
    answer: >-
      Expect new items corresponding to each sensor reading with the selected fields (temperature,
      pressure, humidity, timestamp). If you changed field names in the query, check that the
      stored document structure matches your projection.
  - question: When adding Azure Functions for alerting and aggregation, what result should I expect
      before publishing to Blob Storage?
    answer: >-
      Verify one function reads from Cosmos DB and flags readings that cross your defined thresholds,
      and another computes averages from stored data. The aggregated output should be ready to
      surface in the web app hosted on Azure Blob Storage.
# END generated_summary_faq

author: Dawid Borycki

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
armips:
    - Cortex-A
operatingsystems:
    - Windows
    - Linux
    - macOS
tools_software_languages:    
    - Python
    - Azure
    - Visual Studio Code

further_reading:
    - resource:
        title: Official Azure IoT SDK for Python Documentation
        link: https://learn.microsoft.com/azure/iot-hub/iot-hub-devguide-sdks
        type: documentation    
    - resource:
        title: Azure IoT Hub Python Quickstart
        link: https://learn.microsoft.com/azure/iot-hub/quickstart-send-telemetry-python
        type: website
    - resource:
        title: End-to-End IoT Solution Tutorial with Python and Azure
        link: https://github.com/Azure-Samples/azure-iot-samples-python
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

