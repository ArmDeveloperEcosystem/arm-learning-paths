---
title: The plain (unoptimized) code
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---
Each version of the code has two main functions, one for character-wall collision detection and one for character-character collision detection.

## Unoptimized character-wall collision detection
The unoptimized character-wall collision implementation is in the function `DoWallsPlain()`. It is a simple nested loop through all of the characters and all of the walls.

For all characters we want a boolean result which is **true** when they have hit a wall. Note that in the code there is the assumption that a character can only hit up to two walls at once.

```
private void DoWallsPlain(int numChar)
{
  for (int c = 0; c < numChar; ++c)
  {
    for (int s = 0; s < numWalls; ++s)
    {
      staticCollisions[c * numWalls + s] =
          dynamicObjectsVstatic[c].Intersects(staticObjects[s]);
    }
  }
}
```

The `Intersects` function is a simple check for overlapping axis-aligned bounding boxes.

```
public bool Intersects(StaticCollisionObject other)
{
  return !(other.minPos.x > maxPos.x
        || other.maxPos.x < minPos.x
        || other.minPos.y > maxPos.y
        || other.maxPos.y < minPos.y);
}
```

## Unoptimized character-character collision detection
After the update calls `DoWallsPlain` to perform the character-wall collision detection, the equivalent for character-character collision is called. This is done in the function called `DoCharactersPlain`.

`DoCharactersPlain` contains another simple nested loop. For all characters, it checks if a character hits another character. Again, a boolean value is stored, **true** indicating that a collision has occurred.
```
private void DoCharactersPlain(int numChar)
{
  for (int c = 0; c < numChar; ++c)
  {
    for (int d = c + 1; d < numChar; ++d)
    {
      dynamicCollisions[c * numChar + d] = dynamicObjects[c].Intersects(dynamicObjects[d]);
    }
  }
}
```

Note, the inner loop only ever starts at the character index beyond the index of the outer loop (d = c +1). `dynamicCollisions` has size enough for all collision pairs.

You could think of this structure as a two-dimensional array: one triangular half contains boolean values for [c][d] and the other for [d][c].

There is no need to check collisions of the reverse (e.g., [d][c]) or a character against itself (i.e., the cases where d equals c).

The `Intersects` function is a simple radii check; characters have collided if the distance between their centers is less than the sum of their radii.

```
public bool Intersects(DynamicCollisionObject other)
{
  float distance = radius + other.radius;
  return math.lengthsq(other.position - position) < distance * distance;
}
```
