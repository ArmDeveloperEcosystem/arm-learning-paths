---
title: Motivation
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is the hybrid-runtime? 
The hybrid runtime enables the deployment of software onto other processors, Cortex-M/Cortex-R, in the system via Linux running on the application cores using cloud-native technologies. It allows the following:

It makes firmware updates easy, secure and controllable at scale, normally firmware on Cortex-M microcontrollers is updated to address bugs, security vulnerabilities, performance or update a functionality. The hybrid runtime makes it possible to update what's running on the Cortex-M on-demand for example to upgrade the functionality.
It enables applications to be partitioned into multiple parts where each part runs on a different core depending on its requirements. For example, in a scenario where we want to preserve energy, one part can run on a Cortex-M while the main CPU is asleep, once an event is detected Cortex-A is woken up and can start running its part of the application. The parts can then be deployed and managed in uniform way, meaning we can deploy the software running on the Cortex-M cores as an integral part of the total application deployment – all the software running on both Cortex-A and Cortex-M can be deployed and managed in unison.

It allows applications that are segmented into multiple services where each service runs on a different core depending on its requirement to be deployed and managed in uniform way, meaning we can deploy the software running on the Cortex-M cores as an integral part of the total application deployment – all the software running on both Cortex-A and Cortex-M can be deployed and managed in unison, for example, in a scenario where we want to preserve energy, one service can run on a Cortex-M while the main CPU is asleep, once an event is detected Cortex-A is woken up and can start running its service.
We can leverage existing cores on every edge node. meaning there exists additional computational power on boards, and most of the times it just sits there, idle. By making it easy to access them, we can take fully advantage of all the resources available in our system.

More details on the runtime can be found on the GitHub page https://github.com/smarter-project/hybrid-runtime.git.

