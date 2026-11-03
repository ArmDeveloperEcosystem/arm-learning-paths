---
title: Evaluate camera and object movement with NFRU
description: Compare matched previous, NFRU-generated intermediate, and current frames to inspect preserved detail during camera and object movement.
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Evaluate motion in Project Moku

Compare two Project Moku scenarios to inspect NFRU-generated frames during camera and object movement. Follow the lettering, corridor geometry, and robot detail to see what the intermediate frame preserves.

Compare the **previous rendered frame → NFRU intermediate frame → current rendered frame** in each image. The middle panel is the actual NFRU output generated from the previous and current rendered frames. Highlighted regions use identical crops and fixed dashed guides, so you can follow features as they move between the source positions.

## Fast camera movement

As the camera turns quickly through the corridor, the walls, doorway, and floor move across the view together. NFRU reconstructs the scene between the two rendered views while preserving the features that make the corridor recognizable. The three focus areas show the result on lettering, structural edges, and surface detail.

### A: Lettering stays readable

Follow the **03** marking to compare its position and numeral outlines across the three frames. In the generated frame, the numerals remain distinct at an intermediate position. The surrounding panel stays visible, keeping the lettering connected to the door.

![Matched previous rendered frame, NFRU intermediate frame, and current rendered frame during a camera turn, with tight identical crops and fixed cyan guides showing the 03 marking moving through an intermediate position#center](./images/motion_cases_20261029/camera_movement_intermediate_details.webp "Camera movement: locate regions A, B, and C; inspect lettering in A")

### B: Door geometry retains its shape

Look at the boundary between the bright panel and the dark door frame, then follow the small light beside it. NFRU places these features between their source positions while keeping the panel, frame, and light distinguishable. The door remains a coherent structure as the camera turns.

![Region B compares identical door-frame crops from the previous, NFRU intermediate, and current frames, with a fixed guide beside the panel edge and small light#center](./images/motion_cases_20261029/camera_movement_geometry_details.webp "B: door-frame and panel shapes during camera rotation")

### C: Floor lines remain continuous

The diagonal floor rail provides a different edge direction from the doorway. In the generated frame, its parallel lines remain continuous and retain their alignment with the corridor. The lighter and darker floor areas below the rail also remain recognizable, preserving the broad appearance of the surface.

The enlarged texture is soft, but the rail and surrounding floor still read as a connected part of the scene. This helps the intermediate view maintain the corridor's structure across a wider area.

![Region C compares the diagonal floor rail and adjacent surface pattern across previous, NFRU intermediate, and current frames using identical crops and a fixed guide#center](./images/motion_cases_20261029/camera_movement_floor_details.webp "C: continuous floor rail and recognizable surface pattern")

## Moving object against a fixed background

With the camera stationary, the robot moves across the corridor. This separates the character's movement from the background and makes the generated pose easier to inspect. NFRU preserves the robot's recognizable appearance at an intermediate position, including its bright center, body panels, and protruding silhouette.

### A: Body detail remains recognizable

Follow the bright circular center and the dark rim around it. The generated frame retains their circular appearance and contrast while moving them between the source positions. Nearby panel divisions remain visible, giving the body a readable structure around the bright center.

![Matched previous rendered frame, NFRU intermediate frame, and current rendered frame of a moving robot, with tight identical crops and fixed cyan guides showing the bright center and panel divisions moving through an intermediate position#center](./images/motion_cases_20261029/moving_object_intermediate_details.webp "Object movement: locate regions A, B, and C; inspect body detail in A")

### B: The silhouette stays readable

The rounded upper protrusion tests how well NFRU preserves an object outline against a detailed background. Its outer shape and inner panel remain recognizable in the intermediate frame, and the dark border continues to separate it from the corridor.

The overall silhouette is preserved, although the enlarged crop reveals some edge softness and small boundary irregularities.

![Region B compares the robot's rounded upper protrusion and inner panel against the corridor in previous, NFRU intermediate, and current frames with identical crops and a fixed guide#center](./images/motion_cases_20261029/moving_object_silhouette_details.webp "B: readable upper silhouette against the corridor")

### C: The moving panel remains distinct from the corridor

Look at the side panel and the floor visible beside it. The generated frame places the panel between its source positions while keeping its shape distinguishable from the background. The nearby corridor detail remains recognizable as the character covers and reveals different areas.

This region shows both the benefit and the remaining limitation: NFRU preserves the readable moving part, while small irregularities remain along portions of the boundary.

![Region C compares the moving robot side panel and nearby corridor floor across previous, NFRU intermediate, and current frames, highlighting the object-background boundary with a fixed guide#center](./images/motion_cases_20261029/moving_object_boundary_details.webp "C: moving panel boundary and nearby background detail")

## What these examples demonstrate

In these examples, NFRU generates an intermediate view with readable lettering, continuous floor rails, and recognizable robot panels. Follow these features between the rendered inputs to assess detail preservation during motion. Inspect object boundaries separately for the local softness and irregularities visible in the enlarged crops.

Next, examine occlusion in more detail, focusing on object boundaries and newly revealed background regions.
