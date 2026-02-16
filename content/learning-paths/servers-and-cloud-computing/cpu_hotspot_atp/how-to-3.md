---
title: Assess Baseline Performance
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Run CPU Cycle Hotspot Recipe

As the `main.cpp` file below shows, we simply create a 1920x1080 bitmap image of our fractal. To quickly see where the bottleneck, or hotspot, within our program is, we will run the recipe through Arm Total Performance (ATP). 

**Please Note**: You will need to replace the first string argument in the `myplot.draw()` function with the absolute path to the image folder and rebuild the application.

```cpp
#include "Mandelbrot.h"
#include <iostream>

using namespace std;

int main(){

    Mandelbrot::Mandelbrot myplot(1920, 1080);
    myplot.draw("./images/green.bmp", Mandelbrot::Mandelbrot::GREEN);

    return 0;
}
```

Open up ATP from the host machine. Click on the `CPU Cycle Hotspot` recipe. If this is the first time running the recipe you may need to click the install tools button.

![install-tools](./install-tools.jpg)

Next we will configure the recipe. We will choose to launch a new process, ATP will automatically start collecting metric when the program starts and stop when the program exits.

Provide an absolute path to the recently built binary, `mandelbrot`. 

Finally, we will use the default sampling rate of `Normal`. If your application is a short running program, you may want to consider a higher sample rate, this will be at the tradeoff of more data to store and process. 

![config](./hotspot-config.jpg)

## Analyse Results

A flame graph should be generated. The default colour mode is to label the 'hottest function', those which are sampled and utilizing CPU most frequently, in the darkest shade. Here we can see that the `__complex_abs__` function is being called during ~65% of samples. This is then calling the `__hypot` symbol in `libm.so`.

![single-thread-flameg](./single-thread-flame-graph.jpg)


To understand deeper, we can map the the lines of source code to the functions. To do this right clight on a specific function and select 'View Source Code'. At the time of writing (ATP Engine 0.44.0), you may need to copy the source code onto your host machine. 

![view-src-code](./view-with-source-code.jpg)

Finally, looking in our images directory we can see the bitmap fractal.

![mandelbrot](./plot-1-thread-MAX_ITERATIONS.jpg)

