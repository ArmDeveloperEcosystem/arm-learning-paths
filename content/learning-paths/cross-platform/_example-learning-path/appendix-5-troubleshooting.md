---
title: "Troubleshooting"

weight: 12 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
## Hugo Server Issues

### Why doesn't Hugo show my changes when I'm editing my markdown files?

There could be multiple reasons for the Hugo server not detecting your content updates. 

Please try the following steps in order:

1. Check that you are running the server from the right directory

You might have multiple locations where you are updating and saving your content to and you could be starting the server from the wrong location/directory.

2. Confirm the port number

The first port number used is 1313. If you run a second `hugo server` command a new port will be chosen. Your browser may be connected to a different Hugo server than you expect.

3. Draft mode is activated 

Draft mode is used during content review and editing to avoid publishing Learning Paths before they are ready. 

If you see draft settings as shown below in an _index.md or at the top of an install guide it means draft mode is on.

```console
draft: true
cascade:
    draft: true
```

To see the content in the browser you have two options:

1. Remove the draft mode tags. 

2. Run Hugo with the draft flag. 

This tells Hugo to render the draft articles. 

```bash
hugo server --buildDrafts=true
``` 

or

```bash
hugo server -D
```