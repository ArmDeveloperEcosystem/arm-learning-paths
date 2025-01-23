---
title: Appendix
weight: 11

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## The Neon intrinsics we used
Here is a breakdown of some of the Neon intrinsics that were used to optimize the AABB collision detection in the function called `NeonAABBObjCollisionDetectionUnrolled`. It can be found at line **718** in _CollisionCalculationScript.cs_.

`NeonAABBObjCollisionDetectionUnrolled` performs the collision detection between the characters and the walls. The outer loop iterates through all of the characters, while the inner loop iterates through the walls. The result is an array of boolean values (**true** denotes a collision has occured) which tells us which characters have collided with which walls.

### `Unity.Burst.Intrinsics.v64` (loading data into a vector register)
```
Line 721: var tblindex1 = new Unity.Burst.Intrinsics.v64((byte)0, 4, 8, 12, 255, 255, 255, 255)
```
Create a 64-bit vector with 8 8-bit elements with values (0, 4, 8, 12, 255, 255, 255, 255). This is used as a lookup table on _line 741_.

### `vdupq_n_f32`
```
Line 728: charMaxXs = vdupq_n_f32(*(characters + c))
```
Duplicate floating point values into all 4 lanes of the 128-bit returned vector. The returned vector will contain 4 copies of a single _Max X_ value (of character bounds).

### `vld1q_f32`
```
Line 736: wallMinXs = vld1q_f32(walls + w)
```
Load multiple floating point values from memory into a single vector register. The returned vector will contain _Min X_ values from 4 different walls.

### `vcgeq_f32`
```
Line 741: vcgeq_f32(wallMinXs, charMaxXs)
```
Floating point comparisons (greater-than or equal). It compares 4 walls at once with a character’s _Max X_. Each of the four results will either be all ones (true) or all zeros (false).

### `vorrq_u32`
```
Line 741: vorrq_u32(vcgeq_f32(wallMinXs, charMaxXs), vcgeq_f32(wallMinYs, charMaxYs))
```
Bitwise inclusive OR. The nested calls to `vcgeq\_f32` are comparing the walls (Min X and Min Y) against the characters' Max X and Max Y. The four comparison results are combined with a bitwise OR. 

### `vqtbl1_u8`
```
Line 741: results = vqtbl1_u8(_result of ORs_, tblindex1)
```
Table lookup function that selects elements from an array based on the indices provided. The result of the OR operations will be treated as an array of 8-bit values. The values from _tblindex1_ (0, 4, 8 and 12) ensure that we select the most significant bytes from each u32 OR result. So 4 character-wall comparisons are being merged into one 128-bit vector along with 4 dummies (because of the _out of range_ values in tblindex1) that will be replaced later with the 64-bit value of the next 4 wall comparisons (from _wmvn_u8_).

### `vqtbx1_u8`
```
Line 751: vqtbx1_u8(results, …)
```
Table lookup function except when an index is out of range as it leaves the existing data alone. This has the effect of selecting 4 bytes (using indices from _tblindex2_) from the results of the last 4 comparisons and combines them with the previous 4 results. _results_ will now contain the results of 8 wall-character comparisons.

### `vmvn_u8`
```
Line 751: results = vmvn_u8(...)
```
Bitwise NOT operation. This negates each of the 8 character-wall comparisons. It is effectively the _!_ (NOT) in our [AABB intersection function](/learning-paths/mobile-graphics-and-gaming/using-neon-intrinsics-to-optimize-unity-on-android/5-the-optimizations#the-aabb-intersection-function) except that it is working on 8 results instead of 1.

### `Unity.Burst.Intrinsics.v64` (storing to memory)
```
Line 755: *(Unity.Burst.Intrinsics.v64*)(collisions + (c * numWalls + w - 4)) = results;
```
This is a vectorized form of writing out the 8 results to memory all at once. At the time of writing, Burst doesn’t include the _VSTR_ Neon intrinsic that would do this so this is the most efficient Burst way to get data out of Neon registers.
