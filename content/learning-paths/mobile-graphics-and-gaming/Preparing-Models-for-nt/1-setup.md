---
title: Set up
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In this learning path you will learn how to take a model and prepare it for NGP through various pipelines. You will explore the use of model explorer for a dive into your sample model's operations and the use of Executorch for lowering to backend and running simulations on your sample model

# OS requirements
This learning path requires that you are on linux or arm mac.  

## Reccomended platfoming: 
This learning path will give you snippets of code, in jupyter notebook fashion where the cells would run sequentially, in order to get the most out of this guide it is heavily reccomended that you create a notebook and follow along.   

## Setup requirements
This learning path will be using python 3.11 so you will need to install that version alternatively you can run this script (Link to download setup script) to get the environment set-up and ready to go

Be sure to follow the steps below so we can start using the sample code

    cd repo/executorch
    ./install_executorch.sh
    bash examples/arm/setup.sh --i-agree-to-the-contained-eula --disable-ethos-u-deps --enable-mlsdk-deps


