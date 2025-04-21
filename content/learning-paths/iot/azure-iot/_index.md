---
title: Creating IoT Solutions in Azure for Arm64-Powered Devices

draft: true
cascade:
    draft: true

minutes_to_complete: 320

who_is_this_for: This is an advanced topic for software developers interested in learning how to build a comprehensive IoT solution in Azure that streams, stores, monitors, aggregates, and visualizes data from Arm64-powered IoT devices.

learning_objectives:
    - Set up and configure an Azure IoT Hub.
    - Register an IoT device and stream data using the Azure IoT SDK.
    - Stream IoT data into Azure services using Azure Stream Analytics.
    - Store and persist streamed IoT data in Azure Cosmos DB by configuring a Stream Analytics job.
    - Implement data monitoring and alerts by creating an Azure Function that checks sensor data from Cosmos DB and sends notifications when thresholds are exceeded.
    - Aggregate sensor readings by developing an Azure Function that calculates average values from data stored in Cosmos DB.
    - Publish aggregated IoT data to a public-facing web portal, by deploying a Static Web App hosted on Azure Blob Storage

prerequisites:
    - A machine that can run Python3, and Visual Studio Code. 
    - Azure Account and Subscription.
    - Azure CLI (Command Line Interface).
    - Azure IoT SDK for Python.      

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
    - Coding
    - VS Code
shared_path: true
shared_between:
    - servers-and-cloud-computing
    - laptops-and-desktops
    - mobile-graphics-and-gaming

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
