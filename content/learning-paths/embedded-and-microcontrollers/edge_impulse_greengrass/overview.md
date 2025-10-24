---
title: 0. Overview
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

# Edge Impulse with AWS IoT Greengrass

AWS IoT Greengrass is an AWS IoT service that enables edge devices with customizable/downloadable/installable "components" that can be run to augment what's running on the edge device itself.  AWS IoT Greengrass permits the creation and publication of a "Greengrass Component" that is effectively a set of instructions and artifacts that, when installed and run, create and initiate a custom specified service. 

For more information about AWS IoT Core and AWS Greengrass please review: [AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/what-is-iot-greengrass.html)

## Overview

The Edge Impulse integration with AWS IoT Core and AWS IoT Greengrass is structured as follows:

![Architecture](images/Architecture.png)

* The Edge Impulse "Runner" service now has a "--greengrass" option that enables the integration. 
* AWS Secrets Manager is used to protect the Edge Impulse API Key by removing it from view via command line arguments.
* The Edge Impulse "Runner" service can relay inference results into IoT Core for further processing in the cloud
* The Edge Impulse "Runner" service relays model performance metrics, at configurable intervals, into IoTCore for further processing.
* The Edge Impulse "Runner" service has accessible commands that can be used to configure the service real-time as well as retrieve information about the model/service/configuration.
* More information regarding the Edge Impulse "Runner" service itself can be found [here](https://docs.edgeimpulse.com/docs/tools/edge-impulse-for-linux/linux-node-js-sdk).

Edge Impulse has several custom Greengrass components that can be deployed and run on the Greengrass-enabled edge device to enable this integration. The component recipes and artifacts can be found [here](https://github.com/edgeimpulse/aws-greengrass-components). Lets examine one of those components that we'll used for this workshop!

### The "EdgeImpulseLinuxRunnerServiceComponent" Greengrass Component

The Edge Impulse "Runner" service downloads, configures, installs, and executes an Edge Impulse model, developed for the specific edge device, and provides the ability to retrieve model inference results.  In this case, our component for this service will relay the inference results into AWS IoT Core under the following topic:

		/edgeimpulse/device/<EdgeImpulseDeviceName>/inference/output
		
Additionally, model performance metrics will be published, at defined intervals, here:

		/edgeimpulse/device/<EdgeImpulseDeviceName>/model/metrics
		
Lastly, the Edge Impulse "Runner" service has been upgrade to support a set of bi-directional commands that can be accessed via publication of specific JSON structures to the following topic:

		/edgeimpulse/device/<EdgeImpulseDeviceName>/command/input
		
Command results are published to the following topic:

		/edgeimpulse/device/<EdgeImpulseDeviceName>/command/output

The command reference, including JSON structure details, can be found [here](https://docs.edgeimpulse.com/docs/integrations/aws-greengrass#commands-january-2025-integration-enhancements).

Lets dive deeper into this integration starting with setting up our own edge device!  

Lets go!
