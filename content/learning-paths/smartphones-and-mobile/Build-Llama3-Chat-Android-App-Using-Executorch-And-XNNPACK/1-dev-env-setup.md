---
title: Development Environment Set Up
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Set up your development environment

In this learning path we will look at building and deploying a simple LLM based chat app to an Android device using ExecuTorch and XNNPACK. We will learn how to build ExecuTorch runtime for LLaMA models, build JNI libraries for our Android application and finally using the libraries in the application.

We need to prepare development environment with these things before we can get going:

1. Install Android Studio (latest version recommended)
2. Install Android NDK
3. Install Java 17 JDK
4. Install Git
5. Install Python 3.10

## 1. Install Android Studio and Android NDK

First off, if you haven't already installed, we recommend following steps to install Android Studio and Android NDK

- Download Android Studio by following the instructions at [Android SDK API Level 34](https://developer.android.com/about/versions/14/setup-sdk).
- Download and Install Android NDK using:
  - Android Studio Tools -> SDK Manager -> Android SDK -> SDK Tools -> NDK (Side by side) -> Check v25.0.8775105

## 2. Install Java 17 JDK

- Download and install MacOS or Linux installation of [Java 17 JDK](https://www.oracle.com/java/technologies/javase/jdk17-archive-downloads.html)

## 3. Install Git

- MacOS
  - Install [Homebrew](https://brew.sh/), if you haven't already
  
  ``` bash
  brew install git
  ```

- Linux
  
  ``` bash
  sudo apt install git-all
  ```

## 3. Install Python 3.10

- MacOS
  
  ``` bash
  brew install python@3.10
  ```

- Linux
  
  ``` bash
  sudo apt update
  udo apt install software-properties-common -y
  sudo add-apt-repository ppa:deadsnakes/ppa
  sudo apt install Python3.10
  ```
