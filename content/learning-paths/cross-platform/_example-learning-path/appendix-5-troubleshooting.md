---
# User change
title: "Troubleshooting"

weight: 12 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
## Hugo Server Issues

### Hugo server is not staging or detecting my content updates when I publish the server, How to fix it?

There could be multiple reasons for the Hugo server not detecting your content updates. Please try the following steps in order:

* Check that you are pusblishing the server from the right directorty where you are updating your learning path (You might have multiple locations where you are updating and saving your content to and you could be starting the server from the wrong location/directory).

* Your Browser might be caching the older version of your server/pages. Please clear your browser history or turn off cashing or simple open a new private tab/window and call your page from there.

* Draft mode is activated: sometimes when we return back your learning path after we review it for adjustments, we usually enable "Draft Mode" which will not stage any new content to be published. Once you pull back the learning path changes "Draft Mode" will be activated by default. To fix this issue you can try one of the following options:
1. Remove the "Draft Mode" tags. Ususally, you will find "draft: true" tag(s) on the main/first page of your learning path (it could also be in other pages). Simply comment out those tags or remove them till you are done with your updates and rerun the Hugo server again.
2. Rerun the server using the following options: 
```bash
hugo server --buildDrafts=false
``` 
or
```bash
hugo server -D
```