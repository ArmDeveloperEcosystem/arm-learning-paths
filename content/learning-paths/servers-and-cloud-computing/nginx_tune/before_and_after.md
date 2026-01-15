---
title: "Before and after tuning Nginx"
weight: 2
layout: "learningpathall"
---

##  Importance of tuning

Application tuning allows you to gain performance without scaling your deployment up (bigger machines/nodes) or out (more machines/nodes). This gained performance can either be used, or traded for cost savings by reducing the amount of compute resources provisioned. The graphs below shows the performance gains of an Nginx file server, Reverse Proxy, and API Gateway when they are tuned.

![File Server Before and after Tuning](beforeandafterfileserver.png)

![Reverse Proxy Before and after Tuning](beforeandafterrp.png)

![API Gateway Before and after Tuning](beforeandafterapigw.png)

Requirements vary based on the use case. In the example shown above, the AWS m7g.2xlarge instance type could be down sized to a m7g.xlarge to gain cost savings.
