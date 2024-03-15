---
title: Analyze frame construction
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---
The render graph in Frame Advisor shows a visualization of the rendering operations that make up the frame. It shows how data flows between render passes as well as how resources such as textures are produced and consumed. Use the render graph to find render passes, input or output attachments that are not used in the final output, and which could be removed.

Render passes flow from left to right. The render pass that outputs to the swapchain is the final render pass that outputs to the screen.

![The Render Graph view in Frame Advisor alt-text#center](FA_render_graph_1.1.gif "Figure 1. The Render Graph view")

1. Here, we can see some output attachments that are not used in a future render pass.

    ![Redundant output attachments alt-text#center](Render_graph_egypt_redundant_attachments.png "Figure 3. Redundant output attachments")

    You should clear or invalidate input and output attachments that are not used to avoid unnecessary memory accesses. If clear or invalidate calls are present within a render pass, they are shown in the `Frame Hierarchy` view.  

1. In this example, we can see that some render passes have no consumers at all and that they do not contribute to the final rendered output.

    ![Redundant render passes in Frame Advisor's Render Graph alt-text#center](Render_graph_egypt_redundant_rps.png "Figure 4. Redundant render passes")

    These render passes could therefore be removed, without affecting the output, saving processing power and bandwidth.
