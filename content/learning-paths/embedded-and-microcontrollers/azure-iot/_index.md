---
title: Build IoT Solutions in Azure for Arm Devices

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
    - A machine with Python 3 and Visual Studio Code installed. 
    - An active Azure account with sufficient permissions to create resources (such as IoT Hub, Functions, and Cosmos DB).

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
