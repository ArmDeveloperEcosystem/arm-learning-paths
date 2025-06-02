---
title: Set up environment 
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Create a Python virtual environment 

To follow this Learning Path, you'll need to install a few additional Python packages alongside CMSIS-DSP.

Start by installing the packages in a Python virtual environment. For example, you can use:

```bash 
python -m venv cmsis-dsp-venv
```
If required, activate the environment. 

## Install CMSIS-DSP

Now install the required packages, starting with CMSIS-DSP:

```bash
pip install cmsisdsp
```
This will also install `NumPy`, which is a dependency of the CMSIS-DSP Python package.

## Install Jupyter

You'll be working with a Jupyter notebook, so install the `jupyter` package:

```bash
pip install jupyter
```
## Install additional tools 

Finally, you'll also need packages for reading sound files, playing sound using widgets, and displaying plots:

```bash
pip install soundfile ipywidgets matplotlib
```

## Launch Jupyter and set up your notebook

You can now launch the Jupyter notebook with the following command:

```bash
jupyter notebook
```
A browser window should open, displaying the source tree. 

Create a new Jupyter notebook by clicking **New** and selecting **Python 3 (ipykernel)**. The new notebook is called `Untitled`. Rename it to something descriptive, for example `cmsis-dsp`.

Now import all the required packages by copying and running the following Python code into your notebook and run the cell (Shift+Enter).

{{% notice Note%}}
All the Python code blocks in this Learning Path are intended to be executed in the same Jupyter notebook.
{{% /notice %}}



```python
import cmsisdsp as dsp
import cmsisdsp.fixedpoint as fix
from cmsisdsp import datatype as dt
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view

# Package for plotting
import matplotlib.pyplot as plt

# Package to display audio widgets in the notebook and upload sound files
import ipywidgets
from IPython.display import display,Audio

# To convert a sound file to a NumPy array
import io
import soundfile as sf

# To load test patterns from the Arm Virtual Hardware Echo Canceller demo
from urllib.request import urlopen
```

You're now ready to move on and set up the audio files you'll use for processing.