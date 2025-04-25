---
title: Convert the CMSIS-DSP Python to C
weight: 8

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Convert the CMSIS-DSP Python to C

Once the Python code is working, writing the C code should be straightforward, since the CMSIS-DSP Python wrapper’s API closely mirrors the C API.

### Rescaling
For example, let’s look at rescaling
#### Python version

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
#### C Version

```C
#include "dsp/basic_math_functions.h"
#include "dsp/statistics_functions.h"

arm_status rescale(q15_t *w, uint32_t nb,q15_t *the_max)
{
    uint32_t index;
    q15_t quotient = 0x7FFF;
    /* Default status value for signal is zero so can't be rescaled */
    arm_status status = ARM_MATH_SINGULAR;
    int16_t the_shift = 0;
    *the_max=0;

    arm_absmax_q15(w,nb,the_max,&index);
    if (*the_max != 0)
    {
       status = arm_divide_q15(0x7FFF,*the_max,&quotient,&the_shift);
       if (status == ARM_MATH_SUCCESS)
       {
         arm_scale_q15(w,quotient,(int8_t)the_shift,w,nb);
       }
    }

    return(status);
 
}

```

### Signal energy

#### Python version
```python
def signal_energy_q15(window):
    mean=dsp.arm_mean_q15(window)
    # If we subtract the mean, we won't get saturation.
    # So we use the CMSIS-DSP negate function on an array containing a single sample.
    neg_mean=dsp.arm_negate_q15([mean])[0]
    window=dsp.arm_offset_q15(window,neg_mean)
    energy=dsp.arm_power_q15(window)
    # Energy is not in Q15 (refer to CMSIS-DSP documentation).
    energy=dsp.ssat(energy>>20,16)
    dB=dsp.arm_vlog_q15([energy])
    # The output of the `vlog` is not in Q15
    # The multiplication by `10` is missing compared to the NumPy
    # reference implementation.
    # The result of this function is not equivalent to the float implementation due to the different
    # formats used in the intermediate computations.
    # As a consequence, a different threshold will have to be used
    # to compensate for these differences.
    return(dB[0])
```

#### C version
```C
#include "dsp/basic_math_functions.h"
#include "dsp/fast_math_functions.h"
#include "dsp/statistics_functions.h"

int16_t signal_energy_q15(q15_t *window,uint32_t nb)
{
    q15_t mean,neg_mean;
    arm_mean_q15(window,nb,&mean);
    
    arm_negate_q15(&mean,&neg_mean,1);

    arm_offset_q15(window,neg_mean,window,nb);

    q63_t energy_q63;
    q15_t energy;
    arm_power_q15(window,nb,&energy_q63);

    energy=(q15_t)__SSAT((q31_t)(energy_q63>>20),16);

    // Fixed point format of result is on 16 bit
    // but the specific format has not been identified
    // to make this tutorial easier.
    // We just know it is not q15
    int16_t dB; 

    arm_vlog_q15(&energy,&dB,1);

    return(dB);
}
```

A DSP function written in Python using CMSIS-DSP can be easily converted into a similar C function.
