---
title: Convert the CMSIS-DSP Python to C
weight: 8

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Converting functions

Now that your Python prototype is verified, it's time to translate the key functions into C using the CMSIS-DSP library. Because the CMSIS-DSP Python API closely mirrors the C API, the conversion is generally straightforward. In this section, you will have a look at two examples to understand how the conversion works.

### Rescaling

Here's the original Python implementation of the rescaling operation, followed by its C equivalent. Notice that the function signatures and logic remain very similar, with minor differences to account for explicit memory management and types in C.

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

#### C version

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

As a second example, let's have a look at another critical function: computing the signal energy. This function is essential for tasks like Voice Activity Detection (VAD) and noise suppression.

Here’s the Python version of the signal energy function, followed by its corresponding C translation. As before, while the structure of the function stays the same, explicit buffer and saturation handling is more apparent in the C version.

#### Python version

```python
def signal_energy_q15(window):
    # Calculate window
    mean=dsp.arm_mean_q15(window)
    neg_mean=dsp.arm_negate_q15([mean])[0]
    window=dsp.arm_offset_q15(window,neg_mean)

    # Energy of the window
    energy=dsp.arm_power_q15(window)
    energy=dsp.ssat(energy>>20,16)
    dB=dsp.arm_vlog_q15([energy])

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

As you can see, a DSP function written in Python using the CMSIS-DSP Python wrappers can be directly mapped to a very similar C function with only minor adjustments. This makes it easy to prototype quickly in Python and then migrate to efficient, production-ready C code for embedded platforms.

In the final section, you will explore some additional resources to learn more and start using CMSIS-DSP in your applications.