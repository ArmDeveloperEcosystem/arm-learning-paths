---
title: Set up
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In this learning path you will learn how to take a model and prepare it for NGP through various pipelines. You will explore the use of model explorer for a dive into your sample model's operations and the use of Executorch for lowering to backend and running simulations on your sample model

## Important notice
<B> By running the given set-up script below you agree to the Executorch EULA. </B>
For more information on executorch see: https://docs.pytorch.org/executorch/stable/index.html


## OS requirements
This learning path requires that you are on linux or arm mac.  

## Setup requirements
This learning path will be using python 3.11.14 so you will need to install that version alternatively you can run this script (Link to download setup script) to get the environment set-up and ready to go

The script needs to be ran with the arguement "EULA-AGREED"

    source Setup.sh EULA-AGREED


## Reccomended platfoming: 
This learning path will give you snippets of code. whilst it's relatively simple to slot the code snippets in the correct order we reccommend that you use a jupyter notebook for ease of understanding to ensure you get the most out of this. as sequencing is a very important especially as models get more complicated and we perform heavier operations 