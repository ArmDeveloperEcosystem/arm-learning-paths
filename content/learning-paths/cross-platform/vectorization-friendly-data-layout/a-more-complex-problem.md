---
title: A more complex problem
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

What if you have some more complicated calculations to perform?

For example, let's say you want to add a bounding box to your simulation so the particles bounce on the borders.

Let's modify the previous code to look like this and save the resulting file as `simulation2.c`:

```C
typedef struct ctr4 {
  uint32_t x, y, z, t;
} ctr4_t;

const vec4_t box = { 10.0f, 10.0f, 10.0f, 10.0f };

void simulate_objects(object_t *objects, float duration, float step) {

  float current_time = 0;
  size_t iterations = 0;
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

This is a scalar approach, but the code still uses the `vec4` struct and even the boundaries checking is done on the fourth element, isn't this a waste of cycles? Not really, because the compiler can find an opportunity to autovectorize this, but you should be able to verify this for yourself.

Compile this file first with `-O2`:

```bash
gcc -O2 -Wall simulation2.c -o simulation2
```

Running this should give the following:

```bash
$ ./simulation2
Total border collisions: x: 250123, y: 249711, z: 249844
elapsed time: 36.700929
```

And now with `-O3`:

```bash
gcc -O3 -Wall simulation2.c -o simulation2
```

And similarly you should get the following result:

```bash
$ ./simulation2
Total border collisions: x: 250123, y: 249711, z: 249844
elapsed time: 28.926221
```

So a reduction in execution time of ~21%. This is decent, but you might probably be expecting more. Checking the assembly output will tell you that it's not as good as you expected. 

Check the [output of `objdump -S` for `-O2`](../simulate_objects_O2.s). It doesn't show any SIMD instructions, which is expected with `-O2`.

Now observe the [assembly output for `-O3`](../simulate_objects_O3.s) and in particular these lines:

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

Even without looking the rest of the code, this tells us that there is something amiss with this optimization. Unfortunately you have just found one of the cases that the compilers cannot -yet- autovectorize. Neither GCC nor Clang can autovectorize this code to the quality that hand-written SIMD code can reach. But you should not blame the compilers for failing to autovectorize a piece of code, this is an ongoing process and already the compilers are quite proficient at autovectorizing many loops. It's always worth the effort investigating what the compiler can do for you and only revert to hand-written code when you are not satisfied with the result.

In the next section you will see the manual optimization approach.