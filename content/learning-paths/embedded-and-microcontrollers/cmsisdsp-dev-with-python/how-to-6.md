---
title: Write the CMSIS-DSP Q15 implementation
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Write the CMSIS-DSP Q15 implementation

In this section, you will update the code to run with the CMSIS-DSP Python library. The CMSIS-DSP implementation is similar to the reference implementation you just tested, but some things will be different.

### Slicing

Since the Q15 representation is less accurate than float and can saturate, it's a good idea to verify the recombination step. This helps ensure the Q15 windowing and recombination logic is sound before plugging it into the full Q15 noise suppression pipeline. With the following code, you'll check that recombining the windowed block samples works correctly.

The Hanning window is converted to Q15 format. Then, the slices are multiplied by the Q15 Hanning window and summed. The final result is converted to float.

```python
offsets = range(0, len(data),winOverlap)
offsets=offsets[0:len(slices_q15)]
res=np.zeros(len(data))
window_q15=fix.toQ15(window)
i=0
for n in offsets:
    w = dsp.arm_mult_q15(slices_q15[i],window_q15)
    res[n:n+winLength] = dsp.arm_add_q15(res[n:n+winLength],w)
    i=i+1
res_q15=fix.Q15toF32(res)
plt.plot(res_q15)
plt.show()
```
You can now listen to the audio to check the result.

```python
audioRecombine=Audio(data=res_q15,rate=samplerate,autoplay=False)
audioRecombine
```
### Utilities

CMSIS-DSP does not have a complex data type. Complex numbers are represented as a float array with alternating real and imaginary parts: `[real, imaginary, real, imaginary, ...]`.

You'll need functions to convert to and from NumPy complex arrays. Define these by pasting into a cell in the notebook and evaluating it.

```python
def imToReal1D(a):
    ar=np.zeros(np.array(a.shape) * 2)
    ar[0::2]=a.real
    ar[1::2]=a.imag
    return(ar)

def realToIm1D(ar):
    return(ar[0::2] + 1j * ar[1::2])
```

## Differences with the reference implementation

In this section, you will walk through the updates needed to transition from float to Q15 implementation. To avoid duplication, the final code to be run is available in the final step on this page. Therefore, you should not copy and evaluate the following code snippets.

### Constructor

The constructor for `NoiseSuppressionQ15` is similar and uses Q15 instead of float. The Hanning window is converted to Q15, and Q15 versions of the CFFT objects are created.

### subnoise

The noise reduction function is more complex:

1. Q15 is not accurate enough for the energy computation, meaning many values would be evaluated to zero. Q31 is used instead. In the code, this can look like:
```python
vq31 = dsp.arm_q15_to_q31(v)
energy = dsp.arm_cmplx_mag_squared_q31(vq31)
```

2. For maximum accuracy, the signal is rescaled before calling this function. Since energy is not a linear function, the scaling factor must be compensated when computing the Wiener gain. The argument `status` is zero when the scaling has been applied. A similar scaling factor is applied to the noise:
```python
if status==0:
    the_max_q31=dsp.arm_q15_to_q31([the_max])[0]
    energy=dsp.arm_scale_q31(energy,the_max_q31,0)
    energy=dsp.arm_scale_q31(energy,the_max_q31,0)
```

3. CMSIS-DSP fixed-point division represents 1 exactly. So in Q31, instead of using `0x7FFFFFFF`, `1` is represented as `0x40000000` with a shift of `1`. This behavior is handled in the algorithm when converting the scaling factor to an approximate Q31 value.

Several safeguards are applied:
* The Wiener gain is capped at 1 to prevent overflow.
* If the energy is zero, the gain is also set to 1 to avoid divide-by-zero errors.
* When energy == noise, the result should be exactly 1. In this case, `arm_divide_q31` will return a quotient of `0x40000000` and shiftVal of 1. The algorithm detects this specific representation and overrides it, setting quotient = `0x7FFFFFFF` and shiftVal = 0, which is a closer approximation to full-scale gain in Q31 without the need for additional shifts.

```python
quotient=0x7FFFFFFF
shiftVal=0
if b!=0 and a!=b:
    # Compute the quotient
    status,quotient,shiftVal = dsp.arm_divide_q31(a,b)
    if shiftVal > 0:
        quotient=0x7FFFFFFF
        shiftVal = 0

```

4. The final scaling is performed using a Q31 multiplication, and the result is converted back to Q15:
```python
res = dsp.arm_cmplx_mult_real_q31(vq31,scalingQ31)
resQ15 = dsp.arm_q31_to_q15(res)
```

### rescale

To achieve maximum accuracy in Q15, the signal (and noise) is rescaled before computing the energy.
This rescaling function did not exist in the float implementation. The signal is divided by its maximum value to bring it to full scale::

```python
def rescale(self,w):
        the_max,index=dsp.arm_absmax_q15(w)

        quotient=0x7FFF
        the_shift=0
        status = -1
        if the_max != 0:
            status,quotient,the_shift = dsp.arm_divide_q15(0x7FFF,the_max)
            if status == 0:
                w=dsp.arm_scale_q15(w,quotient,the_shift)
        return(w,status,the_max)
```

The scaling must be reversed after the Inverse FFT (IFFT) to allow recombining the slices and reconstructing the signal:

```python
def undo_scale(self,w,the_max):
    w=dsp.arm_scale_q15(w,the_max,0)
    return(w)
```

### noise suppression

The algorithm closely follows the float implementation. However, there is a small difference because CMSIS-DSP can be built for Cortex-A and Cortex-M. On Cortex-A, there are small differences in the FFT API, as it uses a different implementation.

If the Python package has been built with Neon acceleration, it will use the new API that requires an additional temporary buffer.

If this temporary buffer is not provided, the Python package will allocate it automatically. While you can use the same API, this is less efficient. It is better to detect whether the package has been compiled with Neon acceleration, allocate a temporary buffer and use it in the FFT calls. This approach is closer to how the C API is used.

```python
if dsp.has_neon():
    resultR = dsp.arm_cfft_q15(self._cfftQ15,signalR,0,tmp=self._tmp)
else:
    resultR = dsp.arm_cfft_q15(self._cfftQ15,signalR,0,1)
```

In the Neon version, the FFT's bit-reversal flag is no longer available. It's not possible to disable bit reversal in the Neon version.

A scaling factor must be applied to the IFFT output:

```python
res = dsp.arm_shift_q15(res,self._fftShift)
```

This scaling is unrelated to the signal and noise scaling used for improved accuracy. The output of the Q15 IFFT is not in Q15 format and must be converted. This is typical of fixed-point FFTs, and the same applies to Q31 FFTs.

Finally, the accuracy-related scaling factor is removed at the end of the function:

```python
if status == 0:
   res=self.undo_scale(res,the_max)
```

### noise estimation

The noise estimation function performs both noise estimation and noise suppression. Noise energy is computed in Q31 for higher accuracy. The FFT functions detect whether the package was built with Neon support.

### donothing

`donothing` is a debug function. You can disable noise reduction and test only slicing, overlap-add, and the FFT/IFFT in between. This function applies scaling and performs the FFT/IFFT. It's a good way to check for saturation issues (which are common with fixed-point arithmetic) and to ensure proper scaling compensation.

## The final Q15 implementation

Try the final implementation:

```python
class NoiseSuppressionQ15(NoiseSuppression):
    def __init__(self,slices):
        NoiseSuppression.__init__(self,slices)

        # VAD signal.
        self._vad= clean_vad(np.array([signal_vad_q15(w) for w in slices]))
        self._noise=np.zeros(self._fftLen,dtype=np.int32)
        # Q15 version of the Hanning window.
        self._window=fix.toQ15(dsp.arm_hanning_f32(self._windowLength))
        # CFFT Q15 instance.
        self._cfftQ15=dsp.arm_cfft_instance_q15()
        status=dsp.arm_cfft_init_q15(self._cfftQ15,self._fftLen)

        self._noise_status = -1
        self._noise_max = 0x7FFF


    # Subtract the noise.
    def subnoise(self,v,status,the_max):

        vq31 = dsp.arm_q15_to_q31(v)
        energy = dsp.arm_cmplx_mag_squared_q31(vq31)

        # `status == 0` means the signal has been rescaled.
        if status==0:
            the_max_q31=dsp.arm_q15_to_q31([the_max])[0]
            energy=dsp.arm_scale_q31(energy,the_max_q31,0)
            energy=dsp.arm_scale_q31(energy,the_max_q31,0)

        noise = self._noise
        # `status == 0` means the noise has been rescaled.
        if self._noise_status==0:
            the_max_q31=dsp.arm_q15_to_q31([self._noise_max])[0]
            noise=dsp.arm_scale_q31(noise,the_max_q31,0)
            noise=dsp.arm_scale_q31(noise,the_max_q31,0)


        temp = dsp.arm_sub_q31(energy , noise)
        temp[temp<0]=0

        scalingQ31 = np.zeros(len(temp),dtype=np.int32)
        shift = np.zeros(len(temp),dtype=np.int32)

        # The scaling factor (energy - noise) / energy is computed.
        k=0
        for a,b in zip(temp,energy):
            quotient=0x7FFFFFFF
            shiftVal=0
            if b!=0 and a!=b:
                # We compute the quotient.
                status,quotient,shiftVal = dsp.arm_divide_q31(a,b)
                if shiftVal > 0:
                    quotient=0x7FFFFFFF
                    shiftVal = 0

            scalingQ31[k] = quotient
            shift[k] = shiftVal

            k = k + 1

        res=dsp.arm_cmplx_mult_real_q31(vq31,scalingQ31)
        resQ15 = dsp.arm_q31_to_q15(res)

        return(resQ15)

    # The signal is rescaled before computing the FFT
    def rescale(self,w):
        the_max,index=dsp.arm_absmax_q15(w)

        quotient=0x7FFF
        the_shift=0
        status = -1
        if the_max != 0:
            status,quotient,the_shift = dsp.arm_divide_q15(0x7FFF,the_max)
            if status == 0:
                w=dsp.arm_scale_q15(w,quotient,the_shift)
        return(w,status,the_max)

    # The scaling is removed after the IFFT is computed
    def undo_scale(self,w,the_max):
        w=dsp.arm_scale_q15(w,the_max,0)
        return(w)

    def remove_noise(self,w):
        w,status,the_max = self.rescale(w)
        sig=self.window_and_pad(w)

        # Convert to complex
        signalR=np.zeros(len(sig) * 2,dtype=np.int16)
        signalR[0::2]=sig

        if dsp.has_neon():
           resultR = dsp.arm_cfft_q15(self._cfftQ15,signalR,0,tmp=self._tmp)
        else:
           resultR = dsp.arm_cfft_q15(self._cfftQ15,signalR,0,1)

        resultR = self.subnoise(resultR,status,the_max)

        if dsp.has_neon():
           res = dsp.arm_cfft_q15(self._cfftQ15,resultR,1,tmp=self._tmp)
        else:
           res = dsp.arm_cfft_q15(self._cfftQ15,resultR,1,1)

        res = dsp.arm_shift_q15(res,self._fftShift)
        res=res[0::2]
        res=self.remove_padding(res)

        if status == 0:
            res=self.undo_scale(res,the_max)
        return(res)

    def estimate_noise(self,w):
        w,status,the_max = self.rescale(w)
        self._noise_status = status
        self._noise_max = the_max

        sig=self.window_and_pad(w)

        signalR=np.zeros(len(sig) * 2)
        signalR[0::2]=sig

        if dsp.has_neon():
           resultR = dsp.arm_cfft_q15(self._cfftQ15,signalR,0,tmp=self._tmp)
        else:
           resultR = dsp.arm_cfft_q15(self._cfftQ15,signalR,0,1)

        resultRQ31 = dsp.arm_q15_to_q31(resultR)
        self._noise = dsp.arm_cmplx_mag_squared_q31(resultRQ31)
        resultR = np.zeros(len(resultR),dtype=np.int16)

        if dsp.has_neon():
           res = dsp.arm_cfft_q15(self._cfftQ15,resultR,1,tmp=self._tmp)
        else:
           res = dsp.arm_cfft_q15(self._cfftQ15,resultR,1,1)

        res = dsp.arm_shift_q15(res,self._fftShift)
        res=res[0::2]
        res=self.remove_padding(res)

        if status == 0:
            res=self.undo_scale(res,the_max)

        return(res)

    def do_nothing(self,w):
        w,status,the_max = self.rescale(w)
        sig=self.window_and_pad(w)

        # Convert to complex.
        signalR=np.zeros(len(sig) * 2,dtype=np.int16)
        signalR[0::2]=sig

        if dsp.has_neon():
           resultR = dsp.arm_cfft_q15(self._cfftQ15,signalR,0,tmp=self._tmp)
           res = dsp.arm_cfft_q15(self._cfftQ15,resultR,1,tmp=self._tmp)
        else:
           resultR = dsp.arm_cfft_q15(self._cfftQ15,signalR,0,1)
           res = dsp.arm_cfft_q15(self._cfftQ15,resultR,1,1)
        res = dsp.arm_shift_q15(res,self._fftShift)

        res=res[0::2]

        res=self.remove_padding(res)

        if status == 0:
            res=self.undo_scale(res,the_max)

        return(res)

    def remove_noise_from_slices(self,nonr=False):
        if dsp.has_neon():
             tmp_nb = dsp.arm_cfft_tmp_buffer_size(dt.Q15,self._fftLen,1)
             self._tmp = np.zeros(tmp_nb,dtype=np.int16)
        for (w,v) in zip(self._slices,self._vad):
            result=None
            if nonr:
                result = self.do_nothing(w)
            else:
                if v==1:
                    result=self.remove_noise(w)
                else:
                    result=self.estimate_noise(w)
            self._signal.append(result)

    def overlap_and_add(self):
        nbSamples = len(self._signal)*winOverlap
        offsets = range(0, nbSamples,winOverlap)
        offsets=offsets[0:len(self._signal)]
        res=np.zeros(nbSamples,dtype=np.int16)
        i=0
        for n in offsets:
            res[n:n+winLength] = dsp.arm_add_q15(res[n:n+winLength],self._signal[i])
            i=i+1
        return(res)
```

Verify that the Q15 algorithm is working:

```python
n=NoiseSuppressionQ15(slices_q15)
n.remove_noise_from_slices()
cleaned_q15=n.overlap_and_add()
plt.plot(fix.Q15toF32(cleaned_q15))
plt.show()
```

You can now listen to the result:

```python
audioQ15=Audio(data=fix.Q15toF32(cleaned_q15),rate=samplerate,autoplay=False)
audioQ15
```

You’ve now built a working noise suppression pipeline using the CMSIS-DSP Python package - and seen how fixed-point DSP algorithms are structured in real-world applications.