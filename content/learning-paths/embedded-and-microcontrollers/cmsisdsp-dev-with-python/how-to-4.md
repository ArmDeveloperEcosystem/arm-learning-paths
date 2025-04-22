---
title: Write a simple VAD
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Write a simple voice activity detection

To remove the noise between speech segments, you need to detect when voice is present.

Voice activity detection can be complex, but for this learning path, you'll implement a very simple and naive approach based on energy. The idea is that if the environment isn't too noisy, speech should have more energy than the noise.

The detection will rely on a comparison with a threshold that must be manually tuned.

You'll first implement a version of the voice activity detection (VAD) with NumPy, which will serve as a reference.

Then you'll implement the same version using CMSIS-DSP with the Q15 fixed-point format.

### NumPy VAD

First, you need to compute the energy of the signal within a block of samples. You'll ignore any constant component and focus only on the varying part of the signal:

```python
# Energy of the window
def signal_energy(window):
    w = window - np.mean(window)
    return(10*np.log10(np.sum(window * window)))
```
Then, compare the energy to a threshold to determine whether the block of audio is speech or noise:

```python
def signal_vad(window):
    if signal_energy(window)>-11:
        return(1)
    else:
        return(0)
```

The threshold is hard-coded. It's not a very clean solution, but it's sufficient for a tutorial.

When using such a detector, you'll quickly find that it is not sufficient. You'll need another pass to clean up the detection signal.

```python
def clean_vad(v):
    v = np.hstack([[0],v,[0]])
    # Remove isolated peak
    vmin=[np.min(l) for l in sliding_window_view(v,3)]
    vmin = np.hstack([[0,0],vmin,[0]])
    # Remove isolated hole
    vmax=[np.max(l) for l in sliding_window_view(vmin,4)]
    return(vmax)
```

Now you can apply this algorithm to the audio signal and plot the VAD detection over it to see if it's working:

```python
_,ax=plt.subplots(1,1)
cleaned=clean_vad([signal_vad(w) for w in slices])
vad = np.array([[w]*(winLength-winOverlap) for w in cleaned]).flatten()
ax.plot(data)
ax.plot(vad)
```
The reference implementation works. You can now implement the same version using CMSIS-DSP.

![vad alt-text#center](vad.png "Figure 3. VAD")


### CMSIS-DSP Q15 VAD

First, you need to compute the signal energy from audio in Q15 format using CMSIS-DSP. 

If you look at the CMSIS-DSP documentation, you'll see that the power and log functions don't produce results in Q15 format. Tracking the fixed-point format throughout all lines of an algorithm can be challenging. 

For this tutorial, instead of trying to determine the exact fixed-point format of the output and applying the necessary shift to adjust the output's fixed-point format, we'll simply tune the threshold of the detection function.

```python
def signal_energy_q15(window):
    mean=dsp.arm_mean_q15(window)
    # Subtracting the mean won't cause saturation
    # So we use the CMSIS-DSP negate function on an array containing a single sample.
    neg_mean=dsp.arm_negate_q15([mean])[0]
    window=dsp.arm_offset_q15(window,neg_mean)
    energy=dsp.arm_power_q15(window)
    # Energy is not in Q15 format (refer to the CMSIS-DSP documentation).
    energy=dsp.ssat(energy>>20,16)
    dB=dsp.arm_vlog_q15([energy])
    # The output of the `vlog` is not in q15
    # The multiplication by 10 is missing compared to the NumPy
    # reference implementation.
    # The result of this function is not equivalent to the float implementation due to different 
    # formats used in intermediate computations.
    # As a consequence, a different threshold must be used to compensate for these differences.
    return(dB[0])
```

The comparison function is very similar to the NumPy reference, but the threshold is different:

```python
def signal_vad_q15(window):
    # The threshold is not directly comparable to the float implementation
    # due to the different intermediate formats used in the fixed-point implementation.
    if signal_energy_q15(window)>fix.toQ15(-0.38):
        return(1)
    else:
        return(0)
```

Note that in a C code, you would use the output of `fix.toQ15(-0.38)`.

`fix.toQ15` is a utility of the Python package to convert float to fixed-point. It is not available in the CMSIS-DSP C implementation.
CMSIS-DSP C has functions like `arm_float_to_q15` which work on arrays and are meant to be used at runtime. If you need a precomputed constant, you can use a utility function like `fix.toQ15` and use the resulting value in the code.

The clean VAD function is the same for both the NumPy and Q15 versions. 

Now you can check whether the Q15 version is working by plotting the signal and the output of the Q15 VAD algorithm.

```python
_,ax=plt.subplots(1,1)
cleaned=clean_vad([signal_vad_q15(w) for w in slices_q15])
vad_q15 = np.array([[w]*winOverlap for w in cleaned]).flatten()
ax.plot(data)
ax.plot(vad_q15)

```