---
title: Install the Python packages
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

The application you will develop requires a few additional Python packages besides CMSIS-DSP. These need to be installed before you start writing code.

You should install the packages in a Python virtual environment. For example, you can use:

```
python -m venv cmsis-dsp-venv
```

The first package to install is CMSIS-DSP:

```bash
pip install cmsisdsp
```
It will also install `NumPy`, which is a dependency of the CMSIS-DSP Python package.

You'll be working with a Jupyter notebook, so the `jupyter` package must also be installed:

```bash
pip install jupyter
```

Finally, you'll need packages to read sound files, play sound using widgets, and display plots:

```bash
pip install soundfile ipywidgets matplotlib
```

You can now launch the Jupyter notebook with the following command:

```bash
jupyter notebook
```
A browser window should open showing the source tree your terminal launched from. Create a new Jupyter notebook by clicking the `New` dropdown and selecting `Python 3 (ipykernel)`. The new notebook will be named `Untitled`. Rename it to something more descriptive, for example `cmsis-dsp`.

You can now import all the required packages. Copy the following Python code into your notebook and run the cell (Shift+Enter).
All the Python code blocks in this learning path are intended to be executed in the same Jupyter notebook.

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

You're now ready to move on to the next steps, where you will set up some audio files for processing.