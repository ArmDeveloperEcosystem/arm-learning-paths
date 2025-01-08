---
title: Overview
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is Sentiment Analysis?

* Sentiment analysis, sometimes called *opinion mining*,  is a natural language processing (NLP) technique used to identify and categorize opinions expressed in digital text. 

* Sentiment analysis can help gauge public opinion, identify trends and patterns, and improve decision-making. 

## What can Sentiment Analysis achieve?


## Why analyze posts on X?

* Social media platforms, such as X, provide a wealth of information about public opinion, trends, and events. Sentiment analysis is important because it provides insights into how people feel about a particular topic or issue, and can help to identify emerging trends and patterns.

, such as an X post or a product review. It  

## Architecting a Solution

Two relevant factors to consider when designing the architecture for this solution are the following:

* Real-time sentiment analysis is a computationally-intensive task and can rapidly quickly drive up resources and increase costs if not managed effectively.

* Tracking real-time changes enables you to understand sentiment patterns and make informed decisions promptly, allowing for timely and appropriate actions


Using an Arm-based Amazon EKS cluster offers flexibility, strong performance and cost efficiences. 

Figure 1 shows the architecture that this solution uses:

![sentiment analysis #center](_images/Sentiment-Analysis.png "Figure 1: Sentiment Analysis Architecture." )

The technology stack for the solution includes the following steps:

- Use the X developer API to fetch posts based on certain keywords.
- Process the captured data using Amazon Kinesis.
- Run a sentiment analysis model to classify the text and tone of the text.
- Process the sentiment of the posts using Apache Spark streaming API.
- Use Elasticsearch and Kibana to store the processed Tweets and showcase the activity on a dashboard.
- Monitor the CPU and RAM resources of the Amazon EKS cluster with Prometheus and Grafana.
