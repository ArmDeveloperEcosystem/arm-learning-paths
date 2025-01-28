---
title: PLACEHOLDER STEP TITLE 1
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is a Vector Database?

A vector database is a specialized database designed to store and query vector representations of data. They are a crucial component of many AI applications. But what exactly are they, and how do they work?

Traditional databases store data in tables or objects with defined attributes. However, they struggle to recognize similarities between data points that aren't explicitly defined. Vector databases, on the other hand, is simply an array of numbers, making it much easier to identify similarities.

We can take complex ideas, like words, and translate them into an Nth dimensional vector using a process called embedding.

## Embeddings

Embeddings are vectors generated through an AI model. We can convert "tokens" (sections of text) into a point in Nth dimensional space. 

Then for any given vector, like the embedded token input of a user, we can querying our vector database to find embedded data that is most similar. This is typically done using distance metrics like cosine similarity or Euclidean distance1.

For example, if we want to know which Arm learning path is most relavent to a question a user asks, what we have to do is:

1. Convert the raw data into more comsumable "chunks". In our case, small `yaml` files.
1. Embed the content of the chunks and place into a vector database
1. Take the input from the user and embed it using the same model
1. Find the closest (meaning, most similar) vector in the database, and the original chunk file that vector came from.
1. Use the data from that `chunk.yaml` to retrive the Arm resource(s) most relavent for the user's questions

These retrieved resources are then used to augment the context for the LLM, which generates a final response that is both accurate and contextually relevant.

## Collecting Data into Chunks

To convert data into `chunk.yaml` files, we used...

## Combine Chunks into `.bin` file

Some words will go here