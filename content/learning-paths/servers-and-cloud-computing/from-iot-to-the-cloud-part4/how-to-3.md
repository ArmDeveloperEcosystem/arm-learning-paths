---
title: Pulumi project
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Objective
You'll now learn about the project structure of the Pulumi application you've just created.

## Pulumi project structure
To open the application, go to the azure-aci folder, and type:
```console
code . 
```

This will open Visual Studio Code, and you will see the folder, which resembles a typical structure of the Node.js application with node_modules and the package.json. On top of that, the Pulumi project contains the following files:

1.	Pulumi.yaml contains a global configuration of your project, including name, runtime, and description, which you provided on project creation with Pulumi CLI.
2.	Pulumi.dev.yaml contains additional, stack-specific configuration values. Here this includes the Azure region you configured with Pulumi CLI.
3.	index.ts is the main application file, which programmatically defines all the Azure resources to be deployed.

The generated index.ts looks as follows:

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as resources from "@pulumi/azure-native/resources";
import * as storage from "@pulumi/azure-native/storage";

// Create an Azure Resource Group
const resourceGroup = new resources.ResourceGroup("resourceGroup");

// Create an Azure resource (Storage Account)
const storageAccount = new storage.StorageAccount("sa", {
    resourceGroupName: resourceGroup.name,
    sku: {
        name: storage.SkuName.Standard_LRS,
    },
    kind: storage.Kind.StorageV2,
});

// Export the primary key of the Storage Account
const storageAccountKeys = storage.listStorageAccountKeysOutput({
    resourceGroupName: resourceGroup.name,
    accountName: storageAccount.name
});

export const primaryStorageKey = storageAccountKeys.keys[0].value;
```

The above listing gives us an idea of how the Pulumi works. It maps the Azure resources (like resource groups, Virtual Machines, and so on) to functions and objects. The form of them depends on the programming language you use with Pulumi. Here, we use TypeScript. So, we create the Azure resources like we would create TypeScript objects. For example, to create a resource group, you use resources.ResourceGroup. 