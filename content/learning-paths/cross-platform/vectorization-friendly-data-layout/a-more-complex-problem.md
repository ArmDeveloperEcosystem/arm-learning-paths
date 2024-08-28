---
title: Increase complexity
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

What if you have more complex calculations to perform?

For example, you want to add a bounding box to your simulation so the particles bounce on the borders.

You can modify the previous code to check the boundaries.

Copy your `simulation1.c` to a new file named `simulation2.c` so you can continue modifications and save the original.

```console
cp simulation1.c simulation2.c
```

Edit `simulation2.c` and replace the `simulate_objects()` function with the one below. Also add the new `ctr4` struct and `box` constant below.

```C
typedef struct ctr4 {
  uint32_t x, y, z, t;
} ctr4_t;

const vec4_t box = { 10.0f, 10.0f, 10.0f, 10.0f };

void simulate_objects(object_t *objects, float duration, float step) {

  float current_time = 0;
  ctr4_t collisions = { 0, 0, 0, 0 };

  while (current_time < duration) {
    for (size_t i=0; i < N; i++) {
      objects[i].position.x += objects[i].velocity.x * step;
      objects[i].position.y += objects[i].velocity.y * step;
      objects[i].position.z += objects[i].velocity.z * step;
      objects[i].position.t += objects[i].velocity.t * step;

      // check the boundaries
      if (objects[i].position.x < -box.x || objects[i].position.x > box.x) {
        objects[i].velocity.x = -objects[i].velocity.x;
        collisions.x++;
      }
      if (objects[i].position.y < -box.y || objects[i].position.y > box.y) {
        objects[i].velocity.y = -objects[i].velocity.y;
        collisions.y++;
      }
      if (objects[i].position.z < -box.z || objects[i].position.z > box.z) {
        objects[i].velocity.z = -objects[i].velocity.z;
        collisions.z++;
      }
      if (objects[i].position.t < -box.t || objects[i].position.t > box.t) {
        objects[i].velocity.t = -objects[i].velocity.t;
        collisions.t++;
      }
    }
    current_time += step;
  }
  printf("Total border collisions: x: %d, y: %d, z: %d\n", collisions.x, collisions.y, collisions.z);
}
```

This is a scalar approach, but the code still uses the `vec4` struct and the boundary checking is even done on the fourth element. This is not a waste of cycles as the compiler can find an opportunity to autovectorize this, but you should be able to verify this for yourself.

First, compile the code with `-O2`:

```console
gcc -O2 -Wall simulation2.c -o simulation2
```

Run the new executable:

```console
 ./simulation2
```

The resulting output is:

```output
Total border collisions: x: 250123, y: 249711, z: 249844
elapsed time: 36.700929
```

Next, compile with `-O3`:

```console
gcc -O3 -Wall simulation2.c -o simulation2
```

Run again:

```console
./simulation2
```

Similar to last time, the output is:

```output
Total border collisions: x: 250123, y: 249711, z: 249844
elapsed time: 28.926221
```

Using `-O3` reduces the execution time by about 21%. This is good, but you might be expecting more. Checking the assembly output will tell you that it's not as good as you expected. 

Check the [assembly output for -O2](/learning-paths/cross-platform/vectorization-friendly-data-layout/simulate_objects_O2.s). It doesn't show any SIMD instructions, which is expected with `-O2`.

Now observe the [assembly output for -O3](/learning-paths/cross-platform/vectorization-friendly-data-layout/simulate_objects_O3.s) and in particular these lines:

```simulate2_objects_O3.s
     c48:       6ea0e4ea        fcmgt   v10.4s, v7.4s, v0.4s
     c4c:       6eb0e400        fcmgt   v0.4s, v0.4s, v16.4s
     c50:       6ea2e4e9        fcmgt   v9.4s, v7.4s, v2.4s
     c54:       6ea5e4eb        fcmgt   v11.4s, v7.4s, v5.4s
     c58:       6ea4e4ec        fcmgt   v12.4s, v7.4s, v4.4s
     c5c:       6eb0e442        fcmgt   v2.4s, v2.4s, v16.4s
     c60:       6eb0e4a5        fcmgt   v5.4s, v5.4s, v16.4s
     c64:       6eb0e484        fcmgt   v4.4s, v4.4s, v16.4s
     c68:       6ea1e4ed        fcmgt   v13.4s, v7.4s, v1.4s
     c6c:       6ea3e4ee        fcmgt   v14.4s, v7.4s, v3.4s
     c70:       6ea6e4ef        fcmgt   v15.4s, v7.4s, v6.4s
```

Even without looking at the rest of the code, this indicates something is wrong with this optimization. 

This code is one of the cases that the compilers cannot yet autovectorize. Neither GCC nor Clang can autovectorize this code to the quality that hand-written SIMD code can reach. 

You should not blame the compilers for failing to autovectorize a piece of code. This is an ongoing process and the compilers are already quite proficient at autovectorizing many loops. It's always worth the effort investigating what the compiler can do for you and only revert to hand-written code when you are not satisfied with the result.

In the next section you will see a manual optimization approach.
