### Maintenance checks for Learning Paths and Install Guides
 
Please review the content in the specified content path and support my manual review by:
 
1. **Summarizing what this guide does**
   - What the end goal is
   - What platform(s) and environments it targets
   - Any key assumptions the reader must meet
 
2. **Identifying dependencies and moving parts**
   - OS, architecture, toolchains, frameworks, SDKs
   - External repositories, models, downloads, or services
   - Commands or workflows that are central to the guide
 
3. **Flagging potential risk areas**
   - References to old OS versions, runtimes, or toolchains
   - Dependencies that may be stale, deprecated, or fragile
   - Links or resources that might require checking
   - Steps that rely heavily on UI flows or screenshots
 
4. **Calling out anything that may need a closer human look**
   - Ambiguous or unclear instructions
   - Areas where “latest” or unpinned versions are used
   - Places where ecosystem changes could affect correctness
 
---
 
### How to behave
 
- Be conservative and transparent — if something is uncertain, say so.
- Prefer **flagging** over **fixing**.
- Do not invent new commands, tools, or workflows.
- If suggesting changes, keep them minimal and clearly optional.
- Treat this as a *conversation starter* for the reviewer, not a final verdict.
 
---
 
### Output format (keep it lightweight)
 
Please respond with:
- A short summary of the guide
- A bulleted list of dependencies
- A bulleted list of review flags or questions to consider
 
No code changes are required unless I explicitly ask for them.