---
title: Problem solving – unwanted execution nodes
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Problem

Your application might contain execution nodes which are _entirely_ unnecessary. For example:

![An unnecessary execution node (highlighted)#center](unused-execution-node.png "Figure 1. An unnecessary execution node (highlighted)")

This is a more extreme version of the problem discussed in [the previous section](../unwanted-outputs). There, we looked at execution nodes which produced _some_ outputs which are unnecessary. Here, _all_ outputs are unnecessary.

*It therefore follows that the computation producing the output is itself unnecessary.*

## Solution

The solution is similar to that in the previous section. Remove any API calls which represent the unused computation.

*Be careful, however: your application may be using an apparently “unused” output of an execution node in a later frame.*
