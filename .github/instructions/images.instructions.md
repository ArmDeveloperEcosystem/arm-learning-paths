---
name: Image guidance
description: Use when the task involves adding, editing, reviewing, or fixing Markdown images in Arm Learning Paths or install guides, including image syntax, `#center` alignment, alt text, captions, screenshots, diagrams, terminal-output images, hardware photos, or placeholder alt text.
---

### Image formatting, alt text, and captions

In this repository, the text before `#center` in an image tag is the alt text.

Use this format:

```md
![Descriptive alt text#center](image.png "Optional caption")
```

Rules:
- Do not use placeholder values such as `alt-txt`, `alt text`, or similar
- Do not wrap alt text in extra quotation marks inside `[]`
- Keep `#center` attached directly to the alt text with no extra space before it
- The caption is optional and should be short, descriptive, and natural
- Avoid outdated figure numbering such as `Figure 1:` unless the content genuinely depends on numbered cross-references

Correct:

```md
![Diagram showing the WebGPU rendering flow for drawing a triangle#center](images/webgpu-draw-high-level.svg "WebGPU rendering flow for drawing a triangle")
```

Incorrect:

```md
!["Triangle using WebGPU" #center](images/webgpu-draw-high-level.svg "Figure 8: Triangle using WebGPU")
```

Incorrect:

```md
![alt-txt#center](images/webgpu-draw-high-level.svg "Figure 8: Triangle using WebGPU")
```

### Alt text requirements for tutorials

Learning Paths and install guides are instructional content. Images are usually not decorative. Alt text must help the learner understand what they would otherwise miss.

For every image, alt text should explain:
- What is shown
- What the learner should notice
- Why it matters in the current step

For screenshots:
- Name the screen, tool, or interface shown
- Mention the relevant UI element, tab, field, button, or output
- Explain what the learner should look for in the screenshot
- Connect the image to the current step or expected result

For diagrams:
- Describe the components and relationships shown
- Explain the purpose of the diagram in the current task
- Focus on the workflow, architecture, or sequence the learner needs to understand

For terminal or output images:
- State what command result or status is shown
- Highlight the important confirmation, value, or error message
- Explain why that output matters

For hardware images:
- Describe the device or setup only if it helps the learner complete the task
- Avoid purely decorative descriptions

### Alt text quality rules

- Write meaningful alt text, not placeholders
- Keep it concise but complete. One to three sentences is usually enough
- Prefer instructional value over visual detail
- Include visible text only when the learner needs that text
- Do not use captions as a substitute for alt text
- Do not encode alignment instructions inside the caption

### Caption guidance

- Use short, descriptive captions when needed
- Captions should add context for all readers
- Avoid `Figure X` numbering unless explicit image cross-references are required

Preferred example:

```md
![Screenshot of the Arm Performance Studio timeline showing CPU activity spikes during Mandelbrot rendering. The Timeline tab is selected and the spike region is highlighted so the learner can identify where CPU activity increases during the run.#center](images/timeline-spike.png "Arm Performance Studio timeline showing CPU activity during Mandelbrot rendering")
```

### Image cleanup workflow

- Replace all placeholder alt text such as `alt-txt` with meaningful descriptions
- Keep the repository-specific `#center` syntax when fixing alt text
- Do not remove valid alignment syntax during cleanup
- For bulk cleanup, update the guidance first, then fix content by category or directory in manageable batches
