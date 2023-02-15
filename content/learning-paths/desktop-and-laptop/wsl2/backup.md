---
title: Backup a WSL filesystem

weight: 9
layout: learningpathall
---

## Backup WSL to a file

Use the export command to save the state of a WSL instance.

```bash
wsl --export Ubuntu-22.04 ubuntu-backup.tar
```

The tar file can be copied and imported on the same machine or on another machine.
