---
title: Configuring GitHub
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## How do I configure my GitHub Application to use my API?

Open the GitHub App that you created in [the first GitHub Copilot Extension Learning Path](learning-paths/servers-and-cloud-computing/gh-copilot-simple).

Navigate to the **Copilot** tab, and add your URL to the field under the **Agent Definition** section:

 ![Configure URL](configure.png)

Now update the **Callback URL** in the **General** tab. This is the complete URL to which GitHub redirects after a user authorizes an installation.

## Test your Extension

Now that your Extension is production-ready, it is time to test it. For guidance on testing, see [Test your Copilot Extension](http://localhost:1313/learning-paths/servers-and-cloud-computing/gh-copilot-simple/copilot-test/) in the previous Copilot Extension Learning Path.

## Next Steps

You are now ready to build a more advanced Copilot Extension using RAG techniques. To learn how, see the Learning Path [Create a RAG-based GitHub Copilot Extension in Python](../copilot-extension).