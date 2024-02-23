---
title: Write hand optimized SIMD code
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

If you think the compiler is not vectorizing as much as it could, you can convert your program to hand-written SIMD code.

Copy your `simulation2.c` to a new file named `simulation3.c` so you can continue modifications and save your originals.

```console
cp simulation2.c simulation3.c
```

Edit `simulation3.c` and replace everything above the `main()` function with the code below. 

```C
#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <sys/time.h>
#include <unistd.h>

#include <arm_neon.h>

// The object struct
typedef struct object {
  uint32_t id;
  float weight;
  float32x4_t position;
  float32x4_t velocity;
  void *model_data;
} object_t;

// Helper function to return a random float number from 0.0f to a.
float randf(float a) {
  return ((float)rand()/(float)(RAND_MAX)) * a;
}

const float box_hi[4] = {  10.0f,  10.0f,  10.0f,  10.0f };

#define N           100000 // number of particles
#define SECONDS     100    // duration in seconds
#define STEPSPERSEC 1000   // steps per second or time resolution

void init_objects(object_t *objects) {
  // Give initial speeds and positions
  for (size_t i=0; i < N; i++) {
    float o[4];
    objects[i].id = i;
    objects[i].weight = randf(2.0f);
    // initial positions in box [-10, 10], velocity in [-1, 1]
    o[0] = randf(2.0f * box_hi[0]) - box_hi[0];
    o[1] = randf(2.0f * box_hi[1]) - box_hi[1];
    o[2] = randf(2.0f * box_hi[2]) - box_hi[2];
    o[3] = 0.0f;
    objects[i].position = vld1q_f32(o);
    o[0] = randf(2.0) - 1.0f;
    o[1] = randf(2.0) - 1.0f;
    o[2] = randf(2.0) - 1.0f;
    o[3] = 0.0f;
    objects[i].velocity = vld1q_f32(o);
  }
}

void simulate_objects(object_t *objects, float duration, float step) {

  float current_time = 0.0f;

  float32x4_t dt = vdupq_n_f32(step);
  uint32x4_t one = vdupq_n_u32(1);
  uint32x4_t ctr = vdupq_n_u32(0);

  float32x4_t box_hi_v = vld1q_f32(box_hi);
  float32x4_t box_lo_v = vnegq_f32(box_hi_v);

  while (current_time < duration) {
    // Move the object in msec steps
    for (size_t i=0; i < N; i++) {
      objects[i].position = vfmaq_f32(objects[i].position, objects[i].velocity, dt);

      uint32x4_t gt_mask = vcgtq_f32(objects[i].position, box_hi_v);
      uint32x4_t lt_mask = vcltq_f32(objects[i].position, box_lo_v);
      uint32x4_t col_mask = vorrq_u32(gt_mask, lt_mask);

      float32x4_t neg_velocity = vnegq_f32(objects[i].velocity);
      objects[i].velocity = vbslq_f32(col_mask, neg_velocity, objects[i].velocity);

      ctr = vaddq_u32(ctr, vandq_u32(col_mask, one));
    }
    current_time += step;
  }
  uint32_t collisions[4];
  vst1q_u32((uint32_t *) &collisions, ctr);
  printf("Total border collisions: x: %d, y: %d, z: %d\n", collisions[0], collisions[1], collisions[2]);
}

... original main function below this ...

```

Before running it, look at the main loop of `simulate_objects()`, starting from the first statement:

```C
      objects[i].position = vfmaq_f32(objects[i].position, objects[i].velocity, dt);
```

This calculates the next position of the particle using the formula: `x += vx * dt` and similarly for the other axes. A single instruction can be used for that, the `FMLA`.

{{% notice Note %}}
There are 2 multiply-add instructions on Arm.

In the original AAarch32 and Neon SIMD units, only the unfused instruction exists, which used the `vmlaq_f32`.

AArch64 also provides a fused instruction which is used by the `vfmaq_f32` intrinsic.

The difference is the way the operation `a <- a + b x c` is done:

In an unfused multiply–add the product `b × c` is computed first, rounded to `N` significant bits, and the result is added back to `a` and rounded again to `N` significant bits.

A fused multiply–add computes the entire expression `a + (b × c)` to its full precision before rounding the final result down to `N` significant bits. 

If you use `vmlaq_f32` will you get the unfused instruction? Not always, because compilers do not agree. Clang uses the fused instruction, while GCC retains the unfused instruction.
{{% /notice %}}

Next, look at the comparisons:

```C
      uint32x4_t gt_mask = vcgtq_f32(objects[i].position, box_hi_v);
      uint32x4_t lt_mask = vcltq_f32(objects[i].position, box_lo_v);
      uint32x4_t col_mask = vorrq_u32(gt_mask, lt_mask);
```

The first two instructions are comparisons: first, check if a particle's position has moved outside the boundaries of the x, y, and z axes, by first checking if it's greater than the limits set by `box_hi` and secondly if it's less than its lower bound.

You are using SIMD vectors with 4 elements, but ignoring the 4th element.

After the comparison masks `gt_mask`, `lt_mask` are computed, an `OR` operation is performed to get the final mask.

The reason for doing this is that for each particle there is only one case of being outside the boundary box dimensions, it is either less than `box_lo.x` or greater than `box_hi.x`. Similarly for the other axes. 

Here is an example of the contents of these vectors for a particle, namely the position and velocity vectors, right before the collision:

```output
position(pre) : 0.000000 9.999886 -9.360616 1.039884 
velocity(pre) : 0.000000 0.210884 0.251256 -0.733221 
```

After the `vfmaq_f32()` instruction, the position will be the following:

```output
position(post): 0.000000 10.000096 -9.360365 1.039151 
```

So, apparently your particle has exceeded the boundary box in the `z` axis (3rd element in the vector, counting from the right for Little Endian).

{{% notice Note %}}
The representation is in Little Endian mode, to correspond with memory layout, so element order is: 3, 2, 1, 0)
{{% /notice %}}

You should expect the masks to show that accordingly:

```
gt_mask : 00000000 ffffffff 00000000 00000000
lt_mask : 00000000 00000000 00000000 00000000
col_mask: 00000000 ffffffff 00000000 00000000
```

As expected, the `gt_mask` has one match and that propagates into `col_mask` with the `OR` operation.

The next operations use the mask that was just computed to change the velocity in that axis, to simulate a bounce of that particle against that wall.

One of the methods would be to multiply the velocity vector with `-1.0f` only for that element (a result of the operation `AND` with the `col_mask` and a vector `{ -1.0, -1.0, -1.0, -1.0 }`).

But there is a simpler method on Arm that saves you a multiply instruction. You can use the `FNEG` instruction, which has the `vnegq_f32` intrinsic and negates all elements in a vector:

```C
      float32x4_t neg_velocity = vnegq_f32(objects[i].velocity);
```

So the negative velocity vector is:

```output
    -velocity(pre) : -0.000000 -0.210884 -0.251256 0.733221
```

Now you have both vectors, velocity and its negative, and you can use the negative value.

This is a very common paradigm with SIMD. It's faster to calculate both values and select the right one using a mask than use a branch instruction like you would do in normal scalar code.

The `BSL` instruction is the one that is used and `vbslq_f32()` its corresponding intrinsic:

```C
      objects[i].velocity = vbslq_f32(col_mask, neg_velocity, objects[i].velocity);
```

Here are the resulting values: 

```
    velocity(post): 0.000000 -0.210884 0.251256 -0.733221 
```

You see that the velocity in the z-axis has become negative, which would happen if the particle would hit the wall of the boundary box.

The collision needs to be counted for that axis, by adding 1 to the respective counter (using `AND` with the `col_mask`):

```C
      ctr = vaddq_u32(ctr, vandq_u32(col_mask, one));
```

After the operation, the values of the `ctr` vector variable are:

```output
    ctr: 00000000 00000001 00000000 00000000
```

which is what you expected, a collision is counted in the z-axis.

Now you can run the program, by compiling it with the same command:

```bash
gcc -O3 simulation3.c -o simulation3
```

Run again:

```console
./simulation3 
```

The output is similar to:

```output
Total border collisions: x: 250123, y: 249711, z: 249844
elapsed time: 22.987934
```

This is a reduction of about 20% from the autovectorized version and about 40% from the original C version. 

Performance can be improved further by changing the data layout of your program. Continue to the next section to learn how. 