---
title: Problem solving – unwanted execution nodes
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Problem

Your application might contain execution nodes which are _entirely_ unnecessary. 

For example, look at the render graph below:

![An unnecessary execution node (highlighted)#center](unused-execution-node.png "An unnecessary execution node (highlighted)")

This is a more extreme version of the problem discussed in the previous section. Previously, you saw execution nodes which produced _some_ outputs which are unnecessary. Here, _all_ outputs are unnecessary.

You can conclude that the computation producing the output is unnecessary.

## Solution

Remove any API calls which represent the unused computation.

Be careful, your application may be using an apparently “unused” output of an execution node in a later frame.
