---
title: Overview
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is Sentiment Analysis?

* Sentiment analysis, sometimes called *opinion mining*,  is a natural language processing (NLP) technique used to identify and categorize sentiment expressed in digital text. 

* Sentiment analysis uses tools to scan text and decipher the emotion behind the message, which might broadly be interpreted as positive, negative, or neutral.  

## What can Sentiment Analysis achieve, and why analyze posts on X?

* Sentiment analysis can help identify trends and patterns, and inform predictions.

* Sentiment analysis provides insights into how people feel about a particular topic or issue, and can help to identify emerging viewpoints.

* It is a scalable way of providing organizations and businesses with valuable data such as insights into user feedback, which can then be used in reputation management.

* Tracking real-time changes enables you to recognize sentiment patterns and make informed decisions promptly, allowing for timely and appropriate actions.

* X is one of the most popular social media platforms, and provides a wealth of rapidly-changing information about public opinion, trends, and events.

{{% notice A Note on Twitter %}}
Before 2023, X was formerly known as Twitter. Although often still referred to by many as Twitter, this Learning Path uses the official name, X. "Tweets" are also now known as "posts".
{{% /notice %}}

## Solution Architecture: Using an Arm-based Amazon EKS Cluster 

Real-time sentiment analysis is a compute-intense task and can rapidly consume resources and increase costs if not managed effectively.

Using an Arm-based Amazon EKS cluster can address these issues by offering flexibility, strong performance and cost efficiencies.  

Figure 1 shows the solution architecture that this Learning Path uses for sentiment analysis:

![sentiment analysis #center](_images/Sentiment-Analysis.png "Figure 1: Sentiment Analysis Architecture." )

The technology stack for this solution includes the following steps:

- Use the X developer API to fetch posts based on certain keywords.

- Process the captured data using Amazon Kinesis.

- Run a sentiment analysis model to categorize the text and classify the tone.

- Process the sentiment of the posts using Apache Spark streaming API.

- Use Elasticsearch and Kibana to store the processed Tweets and showcase the activity on a dashboard.

- Monitor the CPU and RAM resources of the Amazon EKS cluster with Prometheus and Grafana.
