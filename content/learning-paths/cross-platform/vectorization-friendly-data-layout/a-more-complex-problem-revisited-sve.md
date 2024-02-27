---
title: Migrate to the Scalable Vector Extension (SVE)
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

You now know the logic behind the vectorization and should threfore be confident that you can understand the SVE code shown below:

```C
#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <sys/time.h>
#include <unistd.h>

#include <arm_sve.h>

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

  printf("SVE size (bytes)= %ld\n", svcntb());

  // Set up the relevant SVE variables and constants
  svfloat32_t s = svdup_n_f32(step);
  svuint32_t one = svdup_n_u32(1);
  svuint32_t ctr_x = svdup_n_u32(0);
  svuint32_t ctr_y = svdup_n_u32(0);
  svuint32_t ctr_z = svdup_n_u32(0);

  // Right now we use the x-axis boundary because they're all the same
  // Ideally we should cater for non-cubic boundaries
  svfloat32_t box_hi_v = svdup_n_f32(box_hi[0]);
  svfloat32_t box_lo_v = svneg_f32_x(svptrue_b32(), box_hi_v);

  while (current_time < duration) {
    // Move svcntw() objects in each iteration
    for (size_t i=0; i < N; i+= svcntw()) {
      svfloat32_t x_v, y_v, z_v, vx_v, vy_v, vz_v;

      // Use svld1_f32(), with full predicates mask to
      // load the object coordinates and velocity for each axis
      x_v = svld1_f32(svptrue_b32(), &objects->x[i]);
      y_v = svld1_f32(svptrue_b32(), &objects->y[i]);
      z_v = svld1_f32(svptrue_b32(), &objects->z[i]);
      vx_v = svld1_f32(svptrue_b32(), &objects->vx[i]);
      vy_v = svld1_f32(svptrue_b32(), &objects->vy[i]);
      vz_v = svld1_f32(svptrue_b32(), &objects->vz[i]);

      // Use SVE FMLA instruction, again full predicate masks
      // Store the coordinates results immediately
      x_v = svmla_f32_m(svptrue_b32(), x_v, vx_v, s);
      y_v = svmla_f32_m(svptrue_b32(), y_v, vy_v, s);
      z_v = svmla_f32_m(svptrue_b32(), z_v, vz_v, s);
      svst1_f32(svptrue_b32(), &objects->x[i], x_v);
      svst1_f32(svptrue_b32(), &objects->y[i], y_v);
      svst1_f32(svptrue_b32(), &objects->z[i], z_v);

      // Calculate the comparison masks 
      svbool_t gt_mask_x = svcmpgt_f32(svptrue_b32(), x_v, box_hi_v);
      svbool_t lt_mask_x = svcmplt_f32(svptrue_b32(), x_v, box_lo_v);
      svbool_t gt_mask_y = svcmpgt_f32(svptrue_b32(), y_v, box_hi_v);
      svbool_t lt_mask_y = svcmplt_f32(svptrue_b32(), y_v, box_lo_v);
      svbool_t gt_mask_z = svcmpgt_f32(svptrue_b32(), z_v, box_hi_v);
      svbool_t lt_mask_z = svcmplt_f32(svptrue_b32(), z_v, box_lo_v);

      // OR the comparison masks to produce the full collision masks
      svbool_t col_mask_x = svorr_b_z(svptrue_b32(), gt_mask_x, lt_mask_x);
      svbool_t col_mask_y = svorr_b_z(svptrue_b32(), gt_mask_y, lt_mask_y);
      svbool_t col_mask_z = svorr_b_z(svptrue_b32(), gt_mask_z, lt_mask_z);

      // Calculate the negative velocities for each axis
      svfloat32_t neg_vx_v = svneg_f32_x(svptrue_b32(), vx_v);
      svfloat32_t neg_vy_v = svneg_f32_x(svptrue_b32(), vy_v);
      svfloat32_t neg_vz_v = svneg_f32_x(svptrue_b32(), vz_v);

      // The new velocity is selected using the collision masks
      // Store the velocity values back
      vx_v = svsel_f32(col_mask_x, neg_vx_v, vx_v);
      vy_v = svsel_f32(col_mask_y, neg_vy_v, vy_v);
      vz_v = svsel_f32(col_mask_z, neg_vz_v, vz_v);
      svst1_f32(svptrue_b32(), &objects->vx[i], vx_v);
      svst1_f32(svptrue_b32(), &objects->vy[i], vy_v);
      svst1_f32(svptrue_b32(), &objects->vz[i], vz_v);

      // Increase the collision counters for each axis
      // Note that we don't need to use an extra AND in this case
      // The collision mask plays that role.
      ctr_x = svadd_u32_m(col_mask_x, ctr_x, one);
      ctr_y = svadd_u32_m(col_mask_y, ctr_y, one);
      ctr_z = svadd_u32_m(col_mask_z, ctr_z, one);
    }
    current_time += step;
  }

  // As before do the horizontal additions, not that svaddv_u32 returns a uint64_t.
  uint64_t collisions[3];
  collisions[0] = svaddv_u32(svptrue_b32(), ctr_x);
  collisions[1] = svaddv_u32(svptrue_b32(), ctr_y);
  collisions[2] = svaddv_u32(svptrue_b32(), ctr_z);
  printf("Total border collisions: x: %ld, y: %ld, z: %ld\n", collisions[0], collisions[1], collisions[2]);
}

int main() {
  struct object_list objects;

  init_objects(&objects);

  const float duration = SECONDS;
  const float step = 1.0f/STEPSPERSEC;
  struct timeval th_time_start, th_time_end;

  gettimeofday(&th_time_start, NULL);
  simulate_objects(&objects, duration, step);
  gettimeofday(&th_time_end, NULL);

  double elapsed;
  elapsed = (th_time_end.tv_sec - th_time_start.tv_sec); // sec
  elapsed += (th_time_end.tv_usec - th_time_start.tv_usec) / 1000000.0; // us to sec

  printf("elapsed time: %f\n", elapsed);
}
```

To run the SVE application, you will need a computer with SVE support. To determine if SVE is available on your processor, run:

```console
lscpu | grep sve
```

If SVE is available, the Flags will be printed: 

```output
Flags: fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma lrcpc dcpop sha3 sm3 sm4 asimddp sha512 sve asimdfhm dit uscat ilrcpc flagm ssbs paca pacg dcpodp svei8mm svebf16 i8mm bf16 dgh rng
```

If no SVE is present, there will be no output. 

Save the new code in a file named `simulation4_sve.c` and compile it with `-march=armv8-a+sve` to target SVE:

```bash
gcc -O3 -Wall simulation4_sve.c -o simulation4_sve -march=armv8-a+sve
```

Run the SVE application:

```bash
./simulation4_sve
```

The output is:

```output
Total border collisions: x: 250123, y: 249711, z: 249844
elapsed time: 11.682421
```

Recompiling with Clang yields similar results.

Rewriting the algorithm using SVE provides a performance increase of about 45% between compilers or 15% if you take the better result from Clang. 

A few notes about the SVE implementation:

* The most important note is that the number of loops changes based on the SVE vector size. Since the type in the vector here is a 32-bit value (float), we can use the intrinsic `svcntw()` (similarly there exist for other types `svcntb()`, `svcnth()`, `svcntd()`). This can sometimes be a problem when you need to know such a quantity at compile time, but there are ways around this, which can be explained in another Learning Path. 
* Predicates are extremely powerful concepts, they can simplify some loops by avoiding special handling for the edges of the loop. Especially since they are passed as arguments in all SVE intrinsics, they can provide significant reduction of code.
* Some intrinsics have suffixes `_z`, `_m`, `_x`. These denote the values that the uninitialized values in the predicate masks will have after the operation. `_z` will zero these values, `_m` will merge from the first operand, `_x` will leave undefined -on purpose. The last one might have undesirable effects like leaking data, so should be used with care.
