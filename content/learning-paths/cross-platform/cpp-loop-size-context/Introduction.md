---
title: Setup
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Introduction

Often the programmer will have a better understanding of their software and the inputs than the compiler. For example, if the loop size is calculated at runtime, the compiler will have to account for a variable size. However, a developer may have knowledge of the runtime profile, for example if the loop size is always a multiple of a specific number. 

To provide this context to the compiler we will use a simple example written in C++. 

## Setup

In this learning path I will be using an Arm-based `r7g.large` instance from AWS but any Arm-based machine can be used. 

Install the `g++` compiler with the following commands. Adjust to the appropriate commands for your operating system.

```bash
sudo apt update
sudo apt install g++
```

