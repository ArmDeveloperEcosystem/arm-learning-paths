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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T22:07:49Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 0e653bdbf5e5b08a6a00ba68e5ed215a0082e22c634d7d632d088851d48bb01c
  summary_generated_at: '2026-06-01T21:29:13Z'
  summary_source_hash: 0e653bdbf5e5b08a6a00ba68e5ed215a0082e22c634d7d632d088851d48bb01c
  faq_generated_at: '2026-06-02T22:07:49Z'
  faq_source_hash: 0e653bdbf5e5b08a6a00ba68e5ed215a0082e22c634d7d632d088851d48bb01c
  summary: >-
    This advanced Learning Path guides you through building an end-to-end IoT solution in Azure
    for Arm devices using Python and Visual Studio Code. You will set up Azure IoT Hub, register
    a device, and stream telemetry using the Azure IoT SDK. The path shows how to process data
    with Azure Stream Analytics, persist it in Azure Cosmos DB, trigger alerts and aggregate readings
    with Azure Functions, and publish aggregated results to a public-facing web app hosted on
    Azure Blob Storage. The steps target Windows, Linux, and macOS. Prerequisites include Python
    3, Visual Studio Code, and an Azure account with permissions to create IoT Hub, Functions,
    and Cosmos DB resources.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need Python 3, Visual Studio Code, and an active Azure account with permissions to create
      resources such as IoT Hub, Azure Functions, and Cosmos DB. Development can be done on Windows,
      Linux, or macOS.
  - question: Do I need physical Arm hardware, or can I simulate device telemetry?
    answer: >-
      The path includes a Python-based telemetry simulator that generates sensor readings. Physical
      hardware requirements are not explicitly listed, though the content references streaming
      from an Arm64-powered IoT device.
  - question: Which Azure services will I create and how are they used in the workflow?
    answer: >-
      You will use Azure IoT Hub for device communication, Azure Stream Analytics to process and
      route telemetry, and Azure Cosmos DB to store data. Azure Functions monitor thresholds and
      aggregate readings, and results are published to a web app hosted on Azure Blob Storage.
  - question: How do I know my simulator is successfully sending data to Azure IoT Hub?
    answer: >-
      After configuring your Python app to connect securely to IoT Hub, you should observe continuous,
      real-time telemetry streaming as described in the steps. Subsequent Stream Analytics inputs
      and queries confirm that messages from IoT Hub are being received and processed.
  - question: What outcome should I expect after configuring Stream Analytics and Cosmos DB?
    answer: >-
      Stream Analytics will process and route incoming telemetry, and the data will be persisted
      into Cosmos DB. This stored data enables the next steps: Azure Functions for threshold-based
      alerts and aggregation, followed by publishing aggregated results to a public-facing Blob
      Storage web app.
# END generated_summary_faq

author: Dawid Borycki

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

