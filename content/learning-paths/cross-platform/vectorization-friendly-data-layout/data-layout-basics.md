---
title: What exactly is data layout?
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Data layout basics

Data layout refers to the memory representation of the variables that belong to a data structure or an object. It describes the way the variables are stored in memory. 

For example, assume you are creating a 3D simulation program or a game where you want to model the movement of thousands of particles and you have the following data structures for the 3D objects:

```C
// Helper struct of a 3D vector with x, y, z, coordinates
typedef struct vec3 {
  float x, y, z;
} vec3_t;

// The object struct
typedef struct object {
  uint32_t id;
  float weight;
  vec3_t position;
  vec3_t velocity;
  void *model_data;
} object_t;
```

These are example data structures. Actual simulations have more information per object. Extra information may include additional identifiers, volume information, a pointer to a 3D model for display purposes, boundary information, or even representations of quantum wavefunctions. The details are beyond the scope of this Learning Path, but most software uses the same principle, regardless of whether it's a game or a molecular dynamics simulation.

The core of the program is the main `for` loop, which changes the positions and velocities of the objects in tiny amounts and updates them multiple times per second, thereby giving the notion of movement.

In this Learning Path, you will compile and run loops and measure performance. 

Use a text editor to copy the code below and save it in a file named `simulation1.c`

```C
#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <sys/time.h>
#include <unistd.h>

// Helper struct of a 3D vector with x, y, z, coordinates
typedef struct vec3 {
  float x, y, z;
} vec3_t;

// The object struct
typedef struct object {
  uint32_t id;
  float weight;
  vec3_t position;
  vec3_t velocity;
  void *model_data;
} object_t;

// Helper function to return a random float number from 0.0f to a.
float randf(float a) {
  return ((float)rand()/(float)(RAND_MAX)) * a;
}

#define N           100000 // number of particles
#define SECONDS     100    // duration in seconds
#define STEPSPERSEC 1000   // steps per second or time resolution

void init_objects(object_t *objects) {
  // Give initial speeds and positions
  for (size_t i=0; i < N; i++) {
    objects[i].id = i;
    objects[i].weight = randf(2.0f);
    // initial positions in box [-10, 10], velocity in [-1, 1]
    objects[i].position.x = randf(20.0) - 10.0f;
    objects[i].position.y = randf(20.0) - 10.0f;
    objects[i].position.z = randf(20.0) - 10.0f;
    objects[i].velocity.x = randf(2.0) - 1.0f;
    objects[i].velocity.y = randf(2.0) - 1.0f;
    objects[i].velocity.z = randf(2.0) - 1.0f;

  }
}

void simulate_objects(object_t *objects, float duration, float step) {

  float current_time = 0;
  while (current_time < duration) {
    // Move the object in steps
    for (size_t i=0; i < N; i++) {
      objects[i].position.x += objects[i].velocity.x * step;
      objects[i].position.y += objects[i].velocity.y * step;
      objects[i].position.z += objects[i].velocity.z * step;
    }
    current_time += step;
  }
}

int main() {
  object_t objects[N];

  init_objects(objects);

  const float duration = SECONDS;
  const float step = 1.0f/STEPSPERSEC;
  struct timeval th_time_start, th_time_end;

  gettimeofday(&th_time_start, NULL);
  simulate_objects(objects, duration, step);
  gettimeofday(&th_time_end, NULL);

  double elapsed;
  elapsed = (th_time_end.tv_sec - th_time_start.tv_sec); // sec
  elapsed += (th_time_end.tv_usec - th_time_start.tv_usec) / 1000000.0; // us to sec

  printf("elapsed time: %f\n", elapsed);
}
```

Compile the code with GCC:

```console
gcc -O3 simulation1.c -o simulation1
```

{{% notice Note %}}
Unless stated, the examples are compiled with gcc version 12. Your results may vary based on your exact compiler version.
{{% /notice %}}

Run the program: 

```console
./simulation1 
```

The `elapsed time` is printed. Depending on your hardware, the printed value may may be different.

```output
elapsed time: 14.605558
```

This is not a realistic simulation as there is no collision detection, no bounds checking, no gravity or other forces between the particles. But once you have finished reading it, you will be able to start learning how to change the data layout to help the compiler perform auto vectorization and increase the performance of a loop. 

Refer to [Learn about Autovectorization](/learning-paths/cross-platform/loop-reflowing/) for a good introduction to autovectorization.

Use `objdump` to view the assembly code for the program, look for the`simulate_objects()`

```console
objdump -S simulation1 | less
```

The disassembly for `simulate_objects()` is:

```output
0000000000000b54 <simulate_objects>:
 b54:   1e202018        fcmpe   s0, #0.0
 b58:   1e204006        fmov    s6, s0
 b5c:   1e204023        fmov    s3, s1
 b60:   0e040424        dup     v4.2s, v1.s[0]
 b64:   5400004c        b.gt    b6c <simulate_objects+0x18>
 b68:   d65f03c0        ret
 b6c:   914f4001        add     x1, x0, #0x3d0, lsl #12
 b70:   0f000405        movi    v5.2s, #0x0
 b74:   91002002        add     x2, x0, #0x8
 b78:   91242021        add     x1, x1, #0x908
 b7c:   aa0203e0        mov     x0, x2
 b80:   bd401402        ldr     s2, [x0, #20]
 b84:   9100a000        add     x0, x0, #0x28
 b88:   bc5e0000        ldur    s0, [x0, #-32]
 b8c:   fc5d8001        ldur    d1, [x0, #-40]
 b90:   1f030040        fmadd   s0, s2, s3, s0
 b94:   fc5e4002        ldur    d2, [x0, #-28]
 b98:   0e22cc81        fmla    v1.2s, v4.2s, v2.2s
 b9c:   fc1d8001        stur    d1, [x0, #-40]
 ba0:   bc1e0000        stur    s0, [x0, #-32]
 ba4:   eb00003f        cmp     x1, x0
 ba8:   54fffec1        b.ne    b80 <simulate_objects+0x2c>  // b.any
 bac:   1e2328a5        fadd    s5, s5, s3
 bb0:   1e2520d0        fcmpe   s6, s5
 bb4:   54fffe4c        b.gt    b7c <simulate_objects+0x28>
 bb8:   d65f03c0        ret
```

You may have spotted a few SIMD instructions (especially `fmla v1.2s, v4.2s, v2.2s`). This is better than no SIMD instructions, but it looks like the performance is not optimal. 

Continue to the next section to learn how to optimize the code. 
