---
title: "Common questions"

weight: 10 

layout: "learningpathall"
---

### Why is the search box missing on the home page?

The search index is not automatically generated, but you can add it to enable the search box. 

Refer to the information about the search box in the [Learning Path setup](../setup/#search) section.

### Why are my Learning Path pages in the wrong order?

Each markdown file has a value called weight.
 
The _index.md is always first (weight: 1). You should start your next page with weight: 2 and continue to increment the weight values on each new page. 

The weight values determine the page order.


### Why do I have multiple Back and Next buttons on my page?

If you see multiple buttons on a single page, it means you have 2 markdown files with the same weight. 

Modify the weight values to be unique and the extra buttons will disappear.
