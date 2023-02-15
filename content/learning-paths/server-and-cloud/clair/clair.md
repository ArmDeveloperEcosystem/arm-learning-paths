---
# User change
title: "Introduction to Clair and its deployment models."

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## What is Clair

[Clair](https://github.com/quay/clair) is an application for parsing image contents and reporting vulnerabilities affecting the contents. This is done via static analysis and not at runtime.

Clair supports the extraction of contents and assignment of vulnerabilities from [these official base containers](https://quay.github.io/clair/whatis.html#what-is-clair).

## How Clair Works

Clair can run in several modes - Indexer, matcher, notifier or combined mode. In combined mode, everything runs in a single OS process.
Clair's analysis is broken into three distinct parts.

### Indexing

Indexing starts with submitting a manifest to Clair. On receipt, Clair will fetch layers, scan contents, and return an intermediate representation called as IndexReport.
Manifests are Clair's representation of a container image. Clair leverages the fact that OCI manifests and layers are content-addressed to reduce duplicated work.
Once manifest is indexed, the IndexReport is persisted for later retrieval.

### Matching

Matching is taking an IndexReport and correlating vulnerabilities affecting the manifest that report represents.
Clair is continually ingesting new security data and request to the matcher will always provide you with the last updated vulnerability analysis of the IndexReport.

### Notifications

Clair implements a notification service.
When new vulnerabilities are discovered, the notifier service will determine if these vulnerabilities affect any indexed manifests. The notifier will then take action according to its configuration.

## Postgres

Clair uses PostgreSQL for its data persistence. Clair supports migrations, so you should only have to point it to a fresh database and letting it do the setup for you.

## Deploying Clair

### Combined Deployment

![combo_mode_clair_pics](https://user-images.githubusercontent.com/87687089/213428835-6e54ee7e-885c-4114-9123-348e162924b2.PNG)

In combined deployment, the Clair processes run in a single OS process. So far, it is the easiest deployment model to configure as it involves limited resources. To configure this model, provide node types for the same database and start Clair in combined mode.
In this mode, any configuration informing Clair on how to talk to other nodes is ignored, it is not needed as all intra-process communications are done directly.
For added flexibility, it is also supported to split the databases while in combined mode.
Since Clair is conceptually a set of micro-services, its processes do not share database tables even when combined into the same OS process.

### Distributed Deployment

![distributive_mode_clair_pic](https://user-images.githubusercontent.com/87687089/213429015-2a574d77-cf44-4310-a003-99e7afacded2.PNG)

If your application needs to asymmetrically scale or you expect high load you may want to consider a distributed deployment.
In distributed deployment, each Clair process runs in its own OS process. Typically this will be a Kubernetes or OpenShift Pod.
A load balancer must be setup in this deployment model. The load balancer will route traffic between Clair nodes along with routing API requests via path based routing to the correct services. Keep in mind a config file per process is not required. Processes use the necessary values for the configured mode.

