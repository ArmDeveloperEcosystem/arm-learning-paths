---
title: Understand SVE2 MATCH for multi-key search
description: Learn how SVE2 MATCH searches for multiple keys in byte and halfword arrays on Arm servers.
weight: 2
layout: "learningpathall"
---

## Understand the search task

Searching an array for any of several keys is common in data-processing workloads. The same multi-key search pattern appears in the following workflows:

- Database value checks
- Character searches for text processing
- Byte pattern searches for network packet inspection
- Pixel value searches for image processing 

You'll implement scalar and Scalable Vector Extension 2 (SVE2) MATCH functions to search for any occurrence of a set of keys in an array. The function should return true if any element in the array matches any of the keys, and false otherwise. You'll then benchmark them using 8-bit and 16-bit array elements on an Arm server that supports SVE2.

## What SVE2 MATCH is

SVE2 is an extension to the Arm architecture that provides vector processing capabilities with a length-agnostic programming model. The MATCH instruction is a specialized SVE2 instruction that efficiently searches for elements in a vector that match any element in another vector.

## What you've learned and what's next

You've learned what SVE2 MATCH is and the common multi-key search pattern that you'll implement. 

Next, you'll implement scalar and SVE2 versions of the search function before measuring their performance.
