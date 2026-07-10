# Staleness signals

Use this reference to interpret stale-content scan results for Arm Learning Paths and install guides.

## Review posture

- Be conservative and transparent.
- Prefer flagging over fixing.
- Treat the report as a conversation starter for the content owner.
- Do not invent new commands, tools, workflows, benchmark numbers, product names, or version guidance.
- Suggest minimal follow-up only when the risk is clear.

## Useful review summary

For each high-priority guide or page, provide:

- A short summary of what the content helps the learner do.
- The platforms, environments, tools, SDKs, frameworks, services, models, repositories, and commands it depends on.
- A short list of flags or questions for a human reviewer.

## Signals to flag

### Temporal language

Flag wording that may become stale, including:

- `currently`
- `latest`
- `recently`
- `newly`
- `preview`
- `beta`
- `at the time of writing`
- `as of`
- `currently supports`

These words are not always wrong. They tell the reviewer to check whether the claim still holds.

### Mutable installs and downloads

Flag commands or links that depend on moving targets:

- `curl` or `wget` install scripts
- `latest` release URLs
- Package manager installs without an explicit version when exact reproducibility matters
- Container images tagged `latest`
- GitHub default branch clones or raw file downloads
- Nightly, preview, beta, or experimental packages

### Version-specific dependencies

Flag version-specific references that may need periodic verification:

- OS versions and distro versions
- Runtime and compiler versions
- SDK, framework, and toolchain versions
- Cloud VM sizes, instance families, and processor names
- Model names, model IDs, container tags, and benchmark output

### Screenshots and UI flows

Screenshots are high maintenance risk when they show:

- Cloud consoles
- Web dashboards
- IDEs or extensions
- Vendor portals
- Menus, dialogs, forms, buttons, tabs, or settings pages

Use the image audit skill for detailed alt text, caption, and `#center` syntax review. Use this skill to decide whether the screenshot itself should be rechecked.

### External dependencies

Flag external links when they point to:

- Official documentation with moving versioned content
- Release pages
- Download pages
- Pricing pages
- Support matrices
- GitHub repositories or examples
- Model repositories or hosted services

External links are often valid; the review question is whether the linked target still supports the content's claim.

### Dates and generated output

Flag old dates, generated output timestamps, benchmark reports, and command output that may have been captured from an older environment. These are often acceptable examples, but they should be checked when they support a technical claim.

## Prioritization

Prioritize content for human review when several signals appear together, such as:

- Screenshot-heavy UI instructions plus cloud-console steps.
- `latest` wording plus command output with a specific old version.
- External release links plus unpinned install commands.
- Product or VM names plus provider-specific setup steps.
- Old dates plus benchmark, support, or compatibility claims.
