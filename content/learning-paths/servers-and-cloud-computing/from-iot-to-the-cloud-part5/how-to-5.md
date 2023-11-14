---
title: Clean up and summary
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Clean up
We have just deployed Azure resources using the Infrastructure as Code. The advantage of this approach is that we can now update the cloud infrastructure by modifying the index.ts and re-running the pulumi up command. It will compare the new declaration with the current state of the cloud deployment and update if needed. Also, you can use a single Pulumi command to de-provision all resources declared in the index.ts. To do so, you type:

```console
pulumi down
```

Pulumi will ask you to confirm your choice (select yes and press enter):

![Pulumi#left](figures/06.png)

After a few moments, you will see the delete confirmation message:

![Pulumi#left](figures/07.png)

## Summary
You learned how to use infrastructure as code using Pulumi in this learning path. This approach is particularly beneficial as you can code cloud infrastructure as an application. Therefore, you can keep the declarations of the cloud infrastructure in the git repository and apply typical workflows you use for the application code development and deployment, like pull requests.