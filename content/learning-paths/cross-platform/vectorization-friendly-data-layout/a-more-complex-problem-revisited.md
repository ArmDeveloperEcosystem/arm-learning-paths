---
title: A more complex problem, revisited
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

You've seen it mentioned already many times, that changing the data layout can improve performance.

But how you would actually perform such a change and why would it matter?

Consider this modified version of the program:

```C
#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <sys/time.h>
#include <unistd.h>

#include <arm_neon.h>

#define N           100000 // number of particles
#define SECONDS     100    // duration in seconds
#define STEPSPERSEC 1000   // steps per second or time resolution

// The object struct
typedef struct object {
  uint32_t id;
  float weight;
  void *model_data;
} object_t;

struct object_list {
  object_t o[N];
  float x[N];
  float y[N];
  float z[N];
  float vx[N];
  float vy[N];
  float vz[N];
};

// Helper function to return a random float number from 0.0f to a.
float randf(float a) {
  return ((float)rand()/(float)(RAND_MAX)) * a;
}

const float box_hi[4] = {  10.0f,  10.0f,  10.0f,  10.0f };

void init_objects(struct object_list *objects) {
  // Give initial speeds and positions
  for (size_t i=0; i < N; i++) {
    objects->o[i].id = i;
    objects->o[i].weight = randf(2.0f);
    // initial positions in box [-10, 10], velocity in [-1, 1]
    objects->x[i] = randf(2.0f * box_hi[0]) - box_hi[0];
    objects->y[i] = randf(2.0f * box_hi[1]) - box_hi[1];
    objects->z[i] = randf(2.0f * box_hi[2]) - box_hi[2];
    objects->vx[i] = randf(2.0) - 1.0f;
    //printf("vx[%ld] = %f\n", i, objects->vx[i]);
    objects->vy[i] = randf(2.0) - 1.0f;
    objects->vz[i] = randf(2.0) - 1.0f;
  }
}

void simulate_objects(struct object_list *objects, float duration, float step) {

  float current_time = 0.0f;
  //size_t iterations = 0;

  float32x4_t s = vdupq_n_f32(step);
  uint32x4_t one = vdupq_n_u32(1);
  // Collision counters are now per axis
  uint32x4_t ctr_x = vdupq_n_u32(0);
  uint32x4_t ctr_y = vdupq_n_u32(0);
  uint32x4_t ctr_z = vdupq_n_u32(0);

  float32x4_t box_hi_v = vld1q_f32(box_hi);
  float32x4_t box_lo_v = vnegq_f32(box_hi_v);

  while (current_time < duration) {
    // Move 4 objects in each iteration
    for (size_t i=0; i < N; i+= 4) {
      float32x4_t x_v, y_v, z_v, vx_v, vy_v, vz_v;

      // Load the x,y,z and vx, vy, vz coords for 4 objects
      x_v = vld1q_f32(&objects->x[i]);
      y_v = vld1q_f32(&objects->y[i]);
      z_v = vld1q_f32(&objects->z[i]);
      vx_v = vld1q_f32(&objects->vx[i]);
      vy_v = vld1q_f32(&objects->vy[i]);
      vz_v = vld1q_f32(&objects->vz[i]);

      // Move the 4 objects in each axis
	  x_v = vmlaq_f32(x_v, vx_v, s);
      y_v = vmlaq_f32(y_v, vy_v, s);
      z_v = vmlaq_f32(z_v, vz_v, s);
      vst1q_f32(&objects->x[i], x_v);
      vst1q_f32(&objects->y[i], y_v);
      vst1q_f32(&objects->z[i], z_v);

      // Calculate the gt/lt masks for each axis
      uint32x4_t gt_mask_x = vcgtq_f32(x_v, box_hi_v);
      uint32x4_t lt_mask_x = vcltq_f32(x_v, box_lo_v);
      uint32x4_t gt_mask_y = vcgtq_f32(y_v, box_hi_v);
      uint32x4_t lt_mask_y = vcltq_f32(y_v, box_lo_v);
      uint32x4_t gt_mask_z = vcgtq_f32(z_v, box_hi_v);
      uint32x4_t lt_mask_z = vcltq_f32(z_v, box_lo_v);

      // Similarly, calculate the collision masks for each axis
      uint32x4_t col_mask_x = vorrq_u32(gt_mask_x, lt_mask_x);
      uint32x4_t col_mask_y = vorrq_u32(gt_mask_y, lt_mask_y);
      uint32x4_t col_mask_z = vorrq_u32(gt_mask_z, lt_mask_z);

      // Calculate the negative velocities for each axis for the 4 objects
      float32x4_t neg_vx_v = vnegq_f32(vx_v);
      float32x4_t neg_vy_v = vnegq_f32(vy_v);
      float32x4_t neg_vz_v = vnegq_f32(vz_v);
      // Select the proper values of vx, vy, vz based on the collision masks
      vx_v = vbslq_f32(col_mask_x, neg_vx_v, vx_v);
      vy_v = vbslq_f32(col_mask_y, neg_vy_v, vy_v);
      vz_v = vbslq_f32(col_mask_z, neg_vz_v, vz_v);
      vst1q_f32(&objects->vx[i], vx_v);
      vst1q_f32(&objects->vy[i], vy_v);
      vst1q_f32(&objects->vz[i], vz_v);

      // Increase the collision counters per axis
      ctr_x = vaddq_u32(ctr_x, vandq_u32(col_mask_x, one));
      ctr_y = vaddq_u32(ctr_y, vandq_u32(col_mask_y, one));
      ctr_z = vaddq_u32(ctr_z, vandq_u32(col_mask_z, one));
    }
    current_time += step;
  }

  // The counters we calculated are in 4 elements for each axis
  // we need to do a horizontal addition to get the final result
  uint32_t collisions[3];
  collisions[0] = vaddvq_u32(ctr_x);
  collisions[1] = vaddvq_u32(ctr_y);
  collisions[2] = vaddvq_u32(ctr_z);
  printf("Total border collisions: x: %d, y: %d, z: %d\n", collisions[0], collisions[1], collisions[2]);
}
...
```

Save this file under `simulation4.c` and compile it like before:

```bash
gcc -O3 -Wall simulation4.c -o simulation4
```

And run it:

```bash
$ ./simulation4
Total border collisions: x: 250123, y: 249711, z: 249844
elapsed time: 16.655471
```

Just for comparison, `clang-15` produces this output:

```bash
 ./simulation4
Total border collisions: x: 250123, y: 249711, z: 249844
elapsed time: 13.530677
```

So, the first observation is that the number of collisions reported is the same, which is a good thing, performance optimization is useless is you get the wrong results!

You also see a very significant speed gain: the new version can be up to 2.25x faster than the original version and ~1.43x faster (for GCC 12) as the previous SIMD -even the hand-written version.

Apart from the small differences between the compilers, the important difference is due to the change in the data layout.

What was changed here? 

First, you will notice that the coordinates `x`,`y`,`z` are not anymore part of the original `object` structure, similarly for the velocity `vx`,`vy`,`vz`.

Instead there is now an array of `N` elements for each of those variables.

This will mean that you can now process 4 consecutive `x` elements in each iteration, 4 `y` elements, 4 `z` elements, etc, so 4 objects per iteration, thereby reducing the iterations to `N/4`.

There is no single `| x | y | z | (unused) |` vector that wastes 25% of storage per instruction.

What you have seen here is a demonstration of two paradigms used in data layout, the first one we used was an Array of Structs (AoS), while the second is called a Struct of Arrays (SoA).

The second one is more performant in SIMD operations in general.

A few points should be made here:

* There is no waste of storage compared to the previous implementation (only 3 of the 4 float elements were used for the 3D coordinates x, y, z)
* About 1/4 of the original `N` iterations are executed, which means 1/4 of the branches
* Many more calculations are done per iteration, which is good as it keeps the CPU pipeline full

These are essentially the rules for optimal performance with SIMD/vectorized code:

* Prefer fewer iterations with more calculations per iteration (keep the pipeline full with fewer branches)
* Data should be consecutive, eg prefer struct of arrays instead of arrays of structs
* Try to keep the data as packed as possible, no wasted elements in the vectors

