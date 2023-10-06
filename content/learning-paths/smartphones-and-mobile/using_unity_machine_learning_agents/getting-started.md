---
title: If starting from scatch...
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

# Without our pre-built assets

## Pre-requisites
You will need to:

- Install [ML-Agents](https://github.com/Unity-Technologies/ml-agents)
- Follow instructions there to integrate with your own code.

# With our pre-built assets (path of least resistance)

## Pre-requisites

You will should have:

* Downloaded and Installed [Unity Game Studio](https://unity.com/download#how-get-started)
* Intalled [Python](https://www.python.org/downloads/)
* Installed [PyTorch](https://pytorch.org/)
* Unzipped the [ML Agents Workshop Supporting Files](MLAgentsWorkshopSupportingFiles.zip)


### Install Python, PyTorch and ML Agents
In command or terminal prompt:
1. Install python 3.7.9 (or a later 3.7), and pip 20.1.1 or later. The official python installer can be found on:
https://www.python.org/downloads/
2. Pip can be installed by following the instructions on this page, for your operating system: https://pip.pypa.io/en/stable/installation/
3. Change directory to where you’ve unzipped the workshop scene. Then create a python virtual
environment: (note that you may need to use python3 instead of python, depending on yoiur install)

`md python-envs`
`python -m venv .\python-envs\mlagents-r18-env`

4. Activate the virtual environment:

`.\python-envs\mlagents-r18-env\Scripts\activate`

5. Install PyTorch:

`pip install torch==1.7.1 -f https://download.pytorch.org/whl/torch_stable.html`

This includes Tensorboard, which will be used during the workshop.
6. Install ml-agents python package:

`python -m pip install mlagents==0.28.0`

7. Downgrade protobuf to work with tensorboard:

`pip install protobuf==3.19`

If this complains use the `-I` option to force it.

### Project Setup 
1. Within Unity open the project directory
2. Once the project is imported, navigate to the _Project_ tab, then to _Assets->#DevSummit2022->Scenes->Level_DevSummit2022_ and select it (See Figure 1.)
![Project Scene Assets](project-assets.png "Figure 1. Project->Assets->#DevSummit2022->Scenes->Level_DevSummit2022")
3. Double click the aforementioned scene to load it.
5. Right click on _ML-Player_ and select _Align View to Selected_
6. The scene should now look like the one in Figure 2.
![Align View to ML-Player](ml-player-aligned-view.png "Figure 2. Align View to ML-Player")
7. Check that the Package Manger is updated and everthing is correctly installed by navigating to _Window->Package Manager_. The screen that appears should look similar to Figure 3.
![Unity Package Manager](package-manager.png "Figure 3. Unity Package Manager")