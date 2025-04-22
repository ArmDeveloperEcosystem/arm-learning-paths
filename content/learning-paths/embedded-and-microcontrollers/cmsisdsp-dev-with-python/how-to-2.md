---
title: Install the Python packages
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Installing the Python packages
The application you will develop with CMSIS-DSP requires a few additional Python packages besides CMSIS-DSP. These need to be installed before you start writing code.

Activate the Python environment you have chosen.

The first package to install is CMSIS-DSP:

```bash
pip install cmsisdsp
```
It will also install `NumPy`, which is a dependency of the CMSIS-DSP Python package.

You'll be working with a Jupyter notebook, so the jupyter package must also be installed:

```bash
pip install jupyter
```

In the Jupyter notebook, you'll be using widgets to play sound, so you'll need to install some additional Jupyter widgets.

```bash
pip install ipywidgets
```

Finally, you'll need packages to read sound files and display plots:


```bash
pip install soundfile
pip install matplotlib
```

you can now launch the Jupyter notebook:

```bash
jupyter notebook
```
Create a new Jupyter notebook by clicking `new` and selecting `Python 3 (ipykernel)`.

The new notebook will be named `Untitled`. Rename it to something more descriptive.

You can now import all the required packages. 

Type the following Python code into your notebook and run the cell (shift-enter).
All the Python code in this learning path is intended to be executed in the same Jupyter notebook.

```python
import cmsisdsp as dsp 
import cmsisdsp.fixedpoint as fix
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

# To load test patterns from the Arm Virtual Hardware Echo Canceller dem
from urllib.request import urlopen
```

You're now ready to move on to the next steps.