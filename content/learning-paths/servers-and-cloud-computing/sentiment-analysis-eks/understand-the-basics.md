---
title: Overview
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is Sentiment Analysis?

* Sentiment analysis, sometimes called *opinion mining*,  is a natural language processing (NLP) technique used to identify and categorize sentiment expressed in digital text. 
* Sentiment analysis uses tools to scan text and dicipher the emotion behind the message, which might broadly be interpreted as postive, negative, or neutral.  

## What can Sentiment Analysis achieve, and why analyze posts on X?

* Sentiment analysis can help identify trends and patterns, and inform predictions.
* Sentiment analysis provides insights into how people feel about a particular topic or issue, and can help to identify emerging viewpoints.
* It is a scalable way of providing organizations and businesses with valuable data such as insights into user feedback, which can then be used in reputation management.
* Tracking real-time changes enables you to understand sentiment patterns and make informed decisions promptly, allowing for timely and appropriate actions.
* X is one of the most popular social media platforms, and provides a wealth of rapidly-changing information about public opinion, trends, and events.


## Solution Architecture

Real-time sentiment analysis is a computationally-intensive task and can rapidly consume resources and increase costs if not managed effectively. 

Using an Arm-based Amazon EKS cluster can address these issues by offering flexibility, strong performance and cost efficiencies.  

Figure 1 shows the solution architecture:

![sentiment analysis #center](_images/Sentiment-Analysis.png "Figure 1: Sentiment Analysis Architecture." )

The technology stack for this solution includes the following steps:

- Use the X developer API to fetch posts based on certain keywords.
- Process the captured data using Amazon Kinesis.
- Run a sentiment analysis model to categorize the text and classify the tone.
- Process the sentiment of the posts using Apache Spark streaming API.
- Use Elasticsearch and Kibana to store the processed Tweets and showcase the activity on a dashboard.
- Monitor the CPU and RAM resources of the Amazon EKS cluster with Prometheus and Grafana.
