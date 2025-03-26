---
title: Setup
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Introduction

Often, the programmer has deeper insights into their software's behavior and its inputs than the compiler does. For instance, if a loop's size is determined at runtime, the compiler must conservatively handle the possibility of variable sizes, potentially limiting optimization opportunities. However, a developer might know more about the application's runtime characteristics—such as the fact that the loop size always adheres to specific constraints, like being a multiple of a particular number.

To illustrate how you can explicitly provide this valuable context to the compiler, we'll walk through a simple C++ example.

## Setup

In this learning path, I will be demonstrating the examples using an Arm-based `r7g.large` instance from AWS; however, you're welcome to follow along using any Arm-based machine that suits your environment or preference.

To get started, you'll first need to install the `g++` compiler on your system. Use the following commands as a guide, adjusting them accordingly based on the operating system or distribution you're working with.

```bash
sudo apt update
sudo apt install g++
```

