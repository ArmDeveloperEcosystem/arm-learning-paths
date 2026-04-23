---
title: Creating the model 
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## What is this all for? 

Think of the Neural Graphics Pipeline as a way of teaching a game to “fill in the visual details” using a machine learning model, instead of doing all the heavy work the traditional way.

In a normal graphics pipeline, everything you see— textures, lighting, shadows— is calculated explicitly by the GPU. That can be expensive, especially on a mobile device. Neural graphics changes this by using machine learning models to approximate or enhance parts of the image. The game can render something simpler first, then let a neural network improve it.

This is effectively like having a model trained to generate images based on smaller inputs and then we are sorting the model out to be put in the game. 

This is especially useful for mobile games because:

Better visuals with less power – you get high-quality graphics without overloading the GPU
Longer battery life – less heavy rendering means lower energy use
Smaller game sizes – fewer large textures are needed if detail can be reconstructed
Real-time performance – AI models can run quickly on dedicated hardware like the Ethos-U NPUs


this learning path aims to teach you the methodology of preparing a model for a neural graphics pipeline. we are using a basic model here for teaching purposes. 


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

