---
title: "Before and after tuning PostgreSQL"
weight: 2
layout: "learningpathall"
---

##  About database performance tuning

Keep in mind that deployment configurations and the profile of SQL requests made by clients will be different. This means there is no one size fits all set of tuning parameters for `PostgreSQL`.  Use the information in this learning path to help you tune `PostgreSQL` for your use case.

##  Importance of tuning

Application tuning allows you to gain performance without scaling your deployment up (bigger machines) or out (more machines). You have the option to use the gained performance or trade it for cost savings by reducing the total compute resources provisioned. Below is a graph that shows the difference performance tuning on `PostgreSQL` can make.

![Before and after Tuning](BeforeAndAfter.png)

Requirements vary based on the use case. In the example shown above, the AWS c7g.8xlarge instance could be down sized to a c7g.4xlarge to gain cost savings.