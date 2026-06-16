# Code sample guidance

## Code samples and formatting

- Always provide explanation before code blocks.
- Use this flow when practical: `[What it does] -> [Code] -> [Expected outcome] -> [Key parameters]`.
- Use Markdown language tags such as `bash`, `python`, `yaml`, `json`, or `output`.
- Use `console` or `bash` for general commands. Try to use the same one throughout a Learning Path or install guide.
- Use the `output` tag to show expected command output.
- Use shortcodes for common pitfalls, warnings, and important notes.

## Output descriptions

- Use `The output is similar to:` or `The expected output is:` before output blocks.
- Use present tense descriptions such as `builds` and `gives`.
- Make sure output examples correspond to the command immediately before them.
- Avoid oversized terminal output unless the full output has instructional value.

## Readability and flow

- Warn if more than 300 words appear between code examples in task-led sections.
- Use visual breaks to prevent walls of text. Code blocks count as visual breaks.
- If a section is long because of code or output rather than explanation, do not treat length alone as a readability problem.
- Flag token-heavy content only when it adds cost without improving learning value, such as oversized terminal output, repeated setup, duplicated examples, unexplained code blocks, or repeated boilerplate.

## Formatting standards

- Use **bold** for UI elements.
- Use *italics* for emphasis and new terms.
- Use `code formatting` for file names, commands, code elements, package names, flags, paths, and environment variables.
- In code blocks, CLI flags, package names, file paths, outputs, and tool messages, keep the exact casing used by the tool.

## Code fence integrity

- Every fenced code block opened with triple backticks must be explicitly closed with matching triple backticks before non-code content resumes.
- Never generate unterminated or partial code fences.
- Do not rely on implicit closure, indentation, or surrounding formatting to end a code block.

## Technical review

- Verify commands match the stated operating system, shell, tool version, and Arm platform.
- Check that install commands use a specific version when required by install guide guidance.
- Check that validation commands prove the intended outcome.
- Do not invent commands, outputs, benchmark numbers, or tool behavior.
- If a command or output cannot be verified, state the limitation instead of guessing.
