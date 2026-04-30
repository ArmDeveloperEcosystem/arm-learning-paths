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

generate_summary_faq: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-04-30T18:58:15Z'
  generator: template
  source_hash: 0e653bdbf5e5b08a6a00ba68e5ed215a0082e22c634d7d632d088851d48bb01c
  summary: >-
    Learn how to build a complete IoT solution in Azure that streams, stores, monitors, aggregates,
    and visualizes telemetry data from Arm devices using IoT Hub, Stream Analytics, Cosmos DB,
    and Azure Functions. It is designed for developers who want to build a comprehensive IoT solution
    in Azure that streams, stores, monitors, aggregates, and visualizes telemetry data from Arm
    IoT devices. By the end, you will be able to set up and configure Azure IoT Hub for device
    communication, register an IoT device and stream telemetry data using the Azure IoT SDK, and
    route IoT data to Azure services using Azure Stream Analytics. It focuses on tools and technologies
    such as Python, Azure, and Visual Studio Code, Windows, Linux, and macOS environments, and
    Arm platforms including Cortex-A. The main steps cover Overview, Create Azure IoT Hub, Build
    a Python-based IoT telemetry simulator, Process IoT telemetry in real time with Azure Stream
    Analytics, and Store data in Azure Cosmos DB with Azure Stream Analytics.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will set up and configure Azure IoT Hub for device communication, register an IoT device
      and stream telemetry data using the Azure IoT SDK, and route IoT data to Azure services
      using Azure Stream Analytics. Learn how to build a complete IoT solution in Azure that streams,
      stores, monitors, aggregates, and visualizes telemetry data from Arm devices using IoT Hub,
      Stream Analytics, Cosmos DB, and Azure Functions.
  - question: Who is this Learning Path for?
    answer: >-
      This is an advanced topic for developers who want to build a comprehensive IoT solution
      in Azure that streams, stores, monitors, aggregates, and visualizes telemetry data from
      Arm IoT devices.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: A machine with Python 3 and Visual Studio
      Code installed; An active Azure account with sufficient permissions to create resources
      (such as IoT Hub, Functions, and Cosmos DB).
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including Python, Azure, and Visual Studio Code, Windows,
      Linux, and macOS environments, and Arm platforms such as Cortex-A.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Overview, Create Azure IoT Hub, Build a Python-based
      IoT telemetry simulator, Process IoT telemetry in real time with Azure Stream Analytics,
      and Store data in Azure Cosmos DB with Azure Stream Analytics.
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

