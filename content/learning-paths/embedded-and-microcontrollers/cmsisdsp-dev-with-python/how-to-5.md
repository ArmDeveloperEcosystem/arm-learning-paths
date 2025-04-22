---
title: Write a noise suppression algorithm
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Write a noise suppression algorithm

### Overlapping windows

The blocks of audio samples you created in the previous steps will be multiplied by a Hanning window function, which looks like this:

```python
window=dsp.arm_hanning_f32(winLength)
plt.plot(window)
plt.show()
```

![hanning alt-text#center](hanning.png "Figure 4. Hanning Window")


The slices we created are overlapping. By applying a Hanning window function and summing the slices, you can reconstruct the original signal. 

Indeed, summing two Hanning windows shifted by half the width of the sample block gives:
![summed hanning alt-text#center](sumhanning.png "Figure 5. Summed Hanning Window")

As result, if you multiply the overlapping blocks of samples by Hanning windows and sum the result, you can reconstruct the original signal:


```python
offsets = range(0, len(data),winOverlap)
offsets=offsets[0:len(slices)]
res=np.zeros(len(data))
i=0
for n in offsets:
    res[n:n+winLength] += slices[i]*window
    i=i+1
plt.plot(res)
plt.show()
```

You can now listen to the recombined signal:
```python
audio2=Audio(data=res,rate=samplerate,autoplay=False)
audio2
```


This means you can process each slice independently and then recombine them at the end to produce the output signal.

### Principle of the noise reduction

The algorithm works in the spectral domain, so a FFT will be used.
When there is no speech (as detected with the VAD), the noise level in each frequency band is estimated.

When speech is detected, the noise estimate is used.

Noise filtering in each band uses a simplified Wiener filter.

A gain is applied to the signal, defined as follow:

$$H(f) = \frac{S(f)}{S(f) + N(f)}$$

- \(S(f)\) is the speech spectrum.
- \(N(f)\) is the noise spectrum.

$$H(f) = \frac{1}{1 + \frac{N(f)}{S(f)}}$$

For this tutorial, we assume a high SNR. The VAD relies on this assumption: the signal energy is sufficient to detect speech.
With a high signal-to-noise ratio, the transfer function can be approximated as:

$$H(f) \approx 1 - \frac{N(f)}{S(f)}$$

You don't have access to \(S(f)\), only to the measured \(S(f) + N(f)\) which will be used under the assumption that the noise is small, making the approximation acceptable:

$$H(f) \approx 1 - \frac{N(f)}{S(f) + N(f)}$$


with \(S(f) + N(f) = E(f)\)

- \(E(f)\) is the observed energy in a frequency band.

It can be rewritten as:

$$H(f) \approx \frac{E(f) - N(f)}{E(f)}$$

- \(N(f)\) is estimated when there is no speech.

In the Python code below, you’ll see this formula implemented as:

```python
scaling = (energy - self._noise)/energy
```

(Don’t evaluate this Python code in your Jupyter notebook—it will be run later as part of the full implementation.)

### NoiseSuppression and NoiseSuppressionReference classes

The entire algorithm will be packaged as a Python class.
The class functions are explained below using Python code that should not be evaluated in the Jupyter notebook.

You should only evaluate the full class definition in the Jupyter notebook—not the code snippets used for explanation.


#### NoiseSuppression constructor

`NoiseSuppression` is a shared class used by both the float reference implementation and the Q15 version.

```python
class NoiseSuppression():
    def __init__(self,slices):
            self._windowLength=len(slices[0])
            self._fftLen,self._fftShift=fft_length(self._windowLength)
            
            self._padding_left=(self._fftLen - self._windowLength)//2 
            self._padding_right=self._fftLen- self._windowLength-self._padding_left
             
            self._signal=[]
            self._slices=slices
            self._window=None
```

The constructor for `NoiseSuppression`:
- Uses the audio slices as input
- Computes the FFT length that can be used for each slice
- Computes the padding needed for the FFT

The FFT length must be a power of 2. The slice length is not necessarily a power of 2. The constructor computes the closest usable power of 2. The audio slices are padded with zeros on both sides to match the required FFT length.

#### NoiseSuppressionReference constructor

```python
class NoiseSuppressionReference(NoiseSuppression):
    def __init__(self,slices):
        # In a better version this could be computed from the signal length by taking the
        # smaller power of two greater than the signal length.
        NoiseSuppression.__init__(self,slices)
        
        # Compute the vad signal
        self._vad=clean_vad([signal_vad(w) for w in slices])
        self._noise=np.zeros(self._fftLen)
        # The Hann window
        self._window=dsp.arm_hanning_f32(self._windowLength)
```

The constructor for `NoiseSuppressionReference`:
- Uses the audio slices as input
- Call the constructor for `NoiseSuppression`
- Computes the VAD signal for the full audio signal
- Compute the Hanning window


#### subnoise
```python
def subnoise(self,v):
        # This is a Wiener estimate.
        energy = v * np.conj(v) + 1e-6
        
        scaling = (energy - self._noise)/energy
        scaling[scaling<0] = 0
        
        return(v * scaling)
```

This function computes the approximate Wiener gain.
If the gain is negative, it is set to 0.
A small value is added to the energy to avoid division by zero.
This function is applied to all frequency bands of the FFT. The `v` argument is a vector.

#### remove_noise
```python
def remove_noise(self,w):
        # We pad the signal with zeros. This assumes the padding is divisible by 2.
        # A more robust implementation would also handle the odd-length case.
        # The FFT length is greater than the window length and must be a power of 2.
        sig=self.window_and_pad(w)
        
        # FFT
        fft=np.fft.fft(sig)
        # Noise suppression
        fft = self.subnoise(fft)
        # IFFT
        res=np.fft.ifft(fft)
        # We assume the result should be real, so we ignore the imaginary part.
        res=np.real(res)
        # We remove the padding.
        res=self.remove_padding(res)
        return(res)
```

The function computes the FFT (with padding) and reduces noise in the frequency bands using the approximate Wiener gain.

#### estimate_noise
```python
 def estimate_noise(self,w):
        # Compute the padded signal.
        sig=self.window_and_pad(w)
        fft=np.fft.fft(sig)
        
        # Estimate the noise energy.
        self._noise = np.abs(fft)*np.abs(fft)
        
        # Remove the noise.
        fft = self.subnoise(fft)
        
        # Perform the IFFT, assuming the result is real, so we ignore the imaginary part.
        res=np.fft.ifft(fft)
        res=np.real(res)
        res=self.remove_padding(res)
        return(res)
```

This function is very similar to the previous one.
It's used when no speech detected.
It updates the noise estimate before reducing the noise.


#### nr

```python
def nr(self):
        for (w,v) in zip(self._slices,self._vad):
            result=None
            if v==1:
                # If voice is detected, we only remove the noise.
                result=self.remove_noise(w)
            else:
                # If no voice is detected, we update the noise estimate.
                result=self.estimate_noise(w)
            self._signal.append(result)
```

The main function: it removes noise from each slice.
If a slice does not contain speech, the noise estimate is updated before reducing noise in each frequency band.

#### overlap_and_add

The filtered slices are recombined:

```python
def overlap_and_add(self):
        offsets = range(0, len(self._signal)*winOverlap,winOverlap)
        offsets=offsets[0:len(self._signal)]
        res=np.zeros(len(data))
        i=0
        for n in offsets:
            res[n:n+winLength]+=self._signal[i]
            i=i+1
        return(res)
```

### The final code for the Python class

You can evaluate this code in your Jupyter notebook.

```python
def fft_length(length):
    result=2
    fft_shift=1
    while result < length:
        result = 2*result
        fft_shift = fft_shift + 1
    return(result,fft_shift)

class NoiseSuppression():
    def __init__(self,slices):
        self._windowLength=len(slices[0])
        self._fftLen,self._fftShift=fft_length(self._windowLength)
        
        self._padding_left=(self._fftLen - self._windowLength)//2 
        self._padding_right=self._fftLen- self._windowLength-self._padding_left
         
        self._signal=[]
        self._slices=slices
        self._window=None
        
    def window_and_pad(self,w):
        if w.dtype==np.int32:
            w=dsp.arm_mult_q31(w,self._window)
        elif w.dtype==np.int16:
            w=dsp.arm_mult_q15(w,self._window)
        else:
            w = w*self._window
        sig=np.hstack([np.zeros(self._padding_left,dtype=w.dtype),w,np.zeros(self._padding_right,dtype=w.dtype)])
        return(sig)
    
    def remove_padding(self,w):
        return(w[self._padding_left:self._padding_left+self._windowLength])

class NoiseSuppressionReference(NoiseSuppression):
    def __init__(self,slices):
        # In a better version this could be computed from the signal length by taking the
        # smaller power of two greater than the signal length.
        NoiseSuppression.__init__(self,slices)
        
        # Compute the vad signal
        self._vad=clean_vad([signal_vad(w) for w in slices])
        self._noise=np.zeros(self._fftLen)
        # The Hann window
        self._window=dsp.arm_hanning_f32(self._windowLength)
        
    # Subtract the noise
    def subnoise(self,v):
        # This is a Wiener estimate
        energy = v * np.conj(v) + 1e-6
        
        scaling = (energy - self._noise)/energy
        scaling[scaling<0] = 0
        
        return(v * scaling)
    
    def remove_noise(self,w):
        # We pad the signal with zero. It assumes that the padding can be divided by 2.
        # In a better implementation we would manage also the odd case.
        # The padding is required because the FFT has a length which is greater than the length of
        # the window
        sig=self.window_and_pad(w)
        
        # FFT
        fft=np.fft.fft(sig)
        # Noise suppression
        fft = self.subnoise(fft)
        # IFFT
        res=np.fft.ifft(fft)
        # We assume the result should be real so we just ignore the imaginary part
        res=np.real(res)
        # We remove the padding
        res=self.remove_padding(res)
        return(res)
    
   
    
    def estimate_noise(self,w):
        # Compute the padded signal
        sig=self.window_and_pad(w)
        fft=np.fft.fft(sig)
        
        # Estimate the noise energy
        self._noise = np.abs(fft)*np.abs(fft)
        
        # Remove the noise
        fft = self.subnoise(fft)
        
        # IFFT and we assume the result is real so we ignore imaginary part
        res=np.fft.ifft(fft)
        res=np.real(res)
        res=self.remove_padding(res)
        return(res)
        
    # Process all the windows using the VAD detection
    def nr(self):
        for (w,v) in zip(self._slices,self._vad):
            result=None
            if v==1:
                # If voice detected, we only remove the noise
                result=self.remove_noise(w)
            else:
                # If no voice detected, we update the noise estimate
                result=self.estimate_noise(w)
            self._signal.append(result)
        
    # Overlap and add to rebuild the signal
    def overlap_and_add(self):
        offsets = range(0, len(self._signal)*winOverlap,winOverlap)
        offsets=offsets[0:len(self._signal)]
        res=np.zeros(len(data))
        i=0
        for n in offsets:
            res[n:n+winLength]+=self._signal[i]
            i=i+1
        return(res)
```
You can now test this algorithm on the original signal:

```python
n=NoiseSuppressionReference(slices)
n.nr()
cleaned=n.overlap_and_add()
plt.plot(cleaned)
plt.show()
```

![cleaned alt-text#center](cleaned.png "Figure 6. Cleaned signal")

You can now listen to the result:

```python
audioRef=Audio(data=cleaned,rate=samplerate,autoplay=False)
audioRef
```