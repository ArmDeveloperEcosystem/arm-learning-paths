---
title: Load an audio file
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Load an audio file

Load an audio file from one of the Arm demo repositories on GitHub.


```python
test_pattern_url="https://github.com/ARM-software/VHT-SystemModeling/blob/main/EchoCanceller/sounds/yesno.wav?raw=true"
f = urlopen(test_pattern_url)
filedata = f.read()
```

You can now play and listen to the audio:
```python
audio=Audio(data=filedata,autoplay=False)
audio
```

An audio widget will appear in your Jupyter notebook. It will look like this:

![audio widget alt-text#center](audiowidget.png "Figure 1. Audio widget")

You can use it to listen to the audio.

You'll hear a sequence of the words "yes" and "no", with some noise between them.
The goal of this learning path is to design an algorithm to remove the noise.


Next, convert the audio into a NumPy array so that it can be processed using CMSIS-DSP:

```python
data, samplerate = sf.read(io.BytesIO(filedata))
if len(data.shape)>1:
    data=data[:,0]
data = data.astype(np.float32)
data=data/np.max(np.abs(data))
dataQ15 = fix.toQ15(data)
```

The code above does the following:
- Converts the audio into a NumPy array
- If the audio is stereo, only one channel is kept
- Normalizes the audio to ensure no value exceeds 1
- Converts the audio to Q15 fixed-point representation to enable the use of CMSIS-DSP fixed-point functions

Now, plot the audio waveform:

```python
plt.plot(data)
plt.show()
```

You'll get the following output:

![audio signal alt-text#center](signal.png "Figure 2. Audio signal")

In the picture, you can see a sequence of words. Between the words, the signal is not zero: there is some noise.

In a real application, you don't wait for the entire signal to be received. The signal is continuous. The samples are processed as they are received. Processing can either be sample-based or block-based. For this learning path, the processing will be block-based.

Before you can move to the next step, this signal must be split into blocks. The processing will occur on small blocks of samples of a given duration.



```python
winDuration=30e-3/6
winOverlap=15e-3/6

winLength=int(np.floor(samplerate*winDuration))
winOverlap=int(np.floor(samplerate*winOverlap))
slices=sliding_window_view(data,winLength)[::winOverlap,:]
slices_q15=sliding_window_view(dataQ15,winLength)[::winOverlap,:]
```

Refer to the [NumPy documentation](https://numpy.org/doc/stable/reference/generated/numpy.lib.stride_tricks.sliding_window_view.html) for details about `sliding_window_view`. It's not the most efficient function, but it is sufficient for this tutorial.

The signal is split into overlapping blocks: each block reuses half of the samples from the previous block as defined by the `winOverlap` variable.

You are now ready to move on to the next step: you have an audio signal that has been split into overlapping blocks, and processing will occur on those blocks.

