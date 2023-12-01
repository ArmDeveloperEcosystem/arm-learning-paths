---
title: Overview
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

BOLT is an optimisation tool that uses an executable performance profile to re-order the executable code layout to reduce memory overhead and improve performance.

The BOLT optmisiation process is performed over a number of steps:
1. A performanance profile is collected of the executable on an Arm Linux target system
2. A BOLT conversion is performed on the performance profile
3. BOLT optimises target executable using the converted performance profile and outputs an optmised executable

After these steps have been run the optmised executable should have improved performance compared to the original executable. 

There are different ways of collecting a performance profile with different BOLT conversions and these steps can be run on 1 or more system. All these different ways of using BOLT are described in more detail in this guide.
