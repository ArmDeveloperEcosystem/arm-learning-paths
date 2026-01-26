---
title: "Common questions"

weight: 11

layout: "learningpathall"
---

### Why is the search box missing on the home page?

The search index is not automatically generated, but you can add it to enable the search box. 

Refer to the information about the search box in the [Learning Path setup](/learning-paths/cross-platform/_example-learning-path/setup/#search) section.

### Why are my Learning Path pages in the wrong order?

Each markdown file has a value called weight.
 
The _index.md is always first (weight: 1). You should start your next page with weight: 2 and continue to increment the weight values on each new page. 

The weight values determine the page order.


### Why do I have multiple Back and Next buttons on my page?

If you see multiple buttons on a single page, it means you have 2 markdown files with the same weight. 

Modify the weight values to be unique and the extra buttons will disappear.

### Why aren't my changes showing up under Learning Paths? 

There are various reasons this can happen. One being that the top links on the page will take you to the external site. Make sure that you are still viewing the Hugo server on `localhost`.

