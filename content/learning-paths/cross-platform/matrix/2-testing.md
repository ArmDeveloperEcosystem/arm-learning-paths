---
title: Testing our work
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

It's a common practice when developing a library to do so with unit tests. While it might appear to be unnecessary in the beginning, tests are bringing significant advantages:

- confidence for the developer, when adding new functionality, or when porting to a new platform / target
- confidence for the users
- catch regressions
- demonstrate how to use the library in practice
- enable new comers to the project
- ...

You'll notice that in this learning path setting up the testing comes almost first, and in any case before the actual library development !

Many unit testing frameworks exist in general, and C++ is not short of them as you can notice on this
[wikipedia article](https://en.wikipedia.org/wiki/List_of_unit_testing_frameworks#C++)
that attempts to enumerate them, so we have no need to reinvent the wheel.

In this learning path, we will use [GoogleTest](https://github.com/google/googletest) as an example.

## Setting up GoogleTest

One great point with GoogleTest is that it provides a seamless integration with CMake, so let's set it up for our project !

## Adding our first test !

## What have we achieved so far ?
