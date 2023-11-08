---
title: Clean up and summary
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Clean up
To remove all the cloud resources, we deployed for this tutorial, open the Cloud Shell, and type the following command:

```console
az group delete -n rg-arm64 --yes --no-wait
```

## Summary

This tutorial taught you how to create the Azure Kubernetes cluster with the arm64-powered virtual machines. Then, you learned how to deploy a containerized application to this cluster. Finally, you exposed the application over the Internet using the LoadBalancer service. Along the way, you saw how to use the Cloud Shell built-in code editor to modify the Kubernetes workload declaration file.