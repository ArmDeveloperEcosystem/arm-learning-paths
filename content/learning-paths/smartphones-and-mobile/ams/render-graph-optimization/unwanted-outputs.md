---
title: Problem solving – unused resources
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Problem

Your application might contain execution nodes which produce resources (outputs) that are unused. Here is an excerpt from our sample trace which shows the problem:

![A render pass creating an unused renderbuffer (highlighted)#center](unused-resources.png "Figure 1. A render pass creating an unused renderbuffer (highlighted)")

This excerpt shows a render pass (`RP0`) which writes three output resources to memory. These are a color image, texture 1 (`T1`), and the two aspects of a packed depth and stencil image, renderbuffer 1 (`RB1.d` and `RB.s`).

The texture is fed into another execution node, `Tr2`. This is a transfer node, number 2. From here, the data ultimately makes its way into the swapchain – and is therefore seen by the user.

The renderbuffer nodes `RB1.d` and `RB1.s` are different. They are not sent to another execution node. Instead, they are unused.

*This wastes both bandwidth and power.*

## Solution

Remove any API calls from your application which generate outputs which are unused. You can find the relevant API calls by:

- Clicking on the render pass
- Visiting Frame Advisor's API Calls view

