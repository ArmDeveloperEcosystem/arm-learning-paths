---
title: Creating the model 
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---


## Creating the simple model 

For all intents and purposes of keeping this lab simple to not over complicate the process we will be using a simple AddSigmoid model just to show the basic procedure.  

Copy the below code into a cell / document to make the model: 

    import torch

    class AddSigmoid(torch.nn.Module):
        def __init__(self):
            super().__init__()
            self.sigmoid = torch.nn.Sigmoid()

        def forward(self, x: torch.Tensor, y: torch.Tensor) -> torch.Tensor:
            return self.sigmoid(x + y)

    example_inputs = (torch.ones(1,1,1,1),torch.ones(1,1,1,1))

    model = AddSigmoid()
    model = model.eval()
    exported_program = torch.export.export(model, example_inputs)
    graph_module = exported_program.module(check_guards=False)

    _ = graph_module.print_readable()

we can actally see the graph module of this model with the last line of code 

## What is this all for? 

TThe Neural Graphics Pipeline (NGP) is a way of using AI to handle parts of graphics rendering more efficiently, especially on power-constrained devices like mobile phones.

In a traditional graphics pipeline, the GPU (such as an Arm Mali GPU) calculates everything explicitly—geometry, textures, lighting, and shadows. This produces high-quality visuals, but it can be computationally expensive and consume a lot of power.

With NGP, some of this work is offloaded to machine learning models. Instead of computing every visual detail directly, a neural network can learn how a scene should look and reconstruct or enhance details. This might mean rendering a simpler image on the GPU and then using AI to improve it, or using a neural model to represent parts of the scene itself.

On Arm-based systems, this is particularly powerful because different processors can share the workload:

- The Mali GPU handles core rendering tasks

- The Ethos NPU accelerates neural network inference efficiently

- The CPU coordinates data and workloads between them

This combination enables:

* Better visuals with less power – AI reduces the need for heavy GPU computation
* Longer battery life – NPUs are more energy-efficient for ML tasks than GPUs
* Smaller game sizes – fewer large textures are needed if detail can be reconstructed
* Real-time performance – dedicated ML hardware allows fast inference alongside rendering

In short, NGP lets developers trade some traditional graphics work for AI-driven techniques, making it possible to deliver richer visuals within the tight power and performance budgets of Arm-based devices.

In simple terms, NGP lets developers trade some smart AI computation for a big reduction in traditional graphics workload— making it possible to deliver richer visuals on devices with limited resources.

this learning path aims to teach you the methodology of preparing a model for a neural graphics pipeline. we are using a basic model here for teaching purposes. 
