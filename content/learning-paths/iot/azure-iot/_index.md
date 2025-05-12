---
title: Create IoT Solutions in Azure for Arm-Powered Devices

minutes_to_complete: 180

who_is_this_for: This is an advanced topic for developers who want to build a comprehensive IoT solution in Azure that streams, stores, monitors, aggregates, and visualizes data from Arm64-powered IoT devices.

learning_objectives:
    - Set up and configure Azure IoT Hub.
    - Register an IoT device and stream data using the Azure IoT SDK.
    - Stream IoT data into Azure services using Azure Stream Analytics.
    - Store and persist streamed data in Azure Cosmos DB through a Stream Analytics job.
    - Monitor data and send alerts by creating an Azure Function that reads sensor data from Cosmos DB and triggers notifications when thresholds are exceeded.
    - Aggregate sensor readings using an Azure Function that calculates average values from data stored in Cosmos DB.
    - Publish aggregated IoT data to a public-facing web portal, by deploying a static web app hosted on Azure Blob Storage.

prerequisites:
    - A machine with Python 3, and Visual Studio Code installed. 
    - An Azure Account and subscription.

author: Dawid Borycki

### Tags
skilllevels: Advanced
subjects: Internet of Things
armips:
    - Cortex-A
    - Neoverse
operatingsystems:
    - Windows
    - Linux
    - macOS
tools_software_languages:    
    - Azure
    - VS Code

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
