---
name: writing-style-review
description: Review and improve writing style, voice, tone, readability, inclusive language, Arm terminology, heading style, word choice, and AI-sounding prose in Arm Learning Paths and install guides. Use when asked to polish prose, make content less AI-generated, improve clarity, or align with Arm editorial style.
---

# Writing style review

Use this skill for granular prose, voice, readability, terminology, and style reviews. Keep edits focused and preserve technical meaning.

## Workflow

1. Identify the target file, section, or selected text.
2. Read surrounding context so style edits preserve the author's intent and the technical flow.
3. Review the target against the guidelines defined in this skill.
4. Depending on request type, do the following:
  - For review requests, report high-impact style issues by file and line when possible. 
  - For edit requests, make focused rewrites, then re-open changed sections to check Markdown, shortcodes, links, and code fences.

## Voice and tone

- Use second person: `you` and `your` for Learning Path summaries, Learning Path content, install guide content, answers to FAQs, and metadata descriptions. Avoid first person for these content types.
- Use first person: `I` and `we` for FAQs.
- Use active voice.
- Use present tense for descriptions.
- Use imperative mood for commands.
- Keep the tone confident, developer-friendly, and natural.
- Encourage readers through complex tasks without generic praise or hype.

## Inclusive language

- Use `primary/subordinate` instead of `master/slave`.
- Do not use gendered examples or assumptions.
- Be mindful of cultural references that might not translate globally.
- Avoid assumptions about a reader's physical capabilities or setup.

## Sentence structure and readability

- Aim for an average of 15 to 20 words per sentence.
- Split complex sentences for clarity.
- Use plain English and avoid jargon overload.
- Define acronyms on first use.
- Use parallel structure in lists.
- Flag sections over 700 words and suggest natural split points.
- Identify paragraphs with sentences averaging over 20 words.
- Note sections that introduce more than two new concepts.
- Flag pages over 3500 words total when prose density hurts review or learning.
- Use visual breaks to prevent walls of text. Code blocks count as visual breaks.
- If a section explains three or more things, suggest splitting it.

## Arm framing and technical depth

- Default to Arm-native solutions, Arm terminology, and Arm platform assumptions.
- Flag x86 assumptions and suggest Arm alternatives when available.
- Match technical depth to the stated audience, prerequisites, and skill level.
- Keep the level of formality and technical detail consistent across related sections.
- Avoid generic advice that could apply to any architecture when the page needs Arm-specific guidance.
- Keep content accessible for screen readers with clear wording and descriptive references.

## Word choice

- Spell out numbers one through five. After that, use numerals.
- Use proper spacing for units: `1 GB`, `23 MB/day`.
- Use `K` for thousands and data-rate abbreviations such as `Gbps`.
- Use `To [action]` instead of `Follow the steps below to [action]`.
- Use `for example` instead of `e.g.`.
- Use `that is` instead of `i.e.`.
- Use `because` instead of `since`.
- Use `also` instead of `in addition`.
- Use `to` instead of `in order to`.
- Use `see` instead of `refer to`.
- Use `use` instead of `utilize` or `leverage`.
- Use `need` instead of `require`.
- Use `can` or `might` instead of `may`.
- Use `set up` as a verb and `setup` as a noun.
- Use `avoid` instead of `try not to`.
- Use `such as` instead of `like`.
- Use `after` or `when` instead of `once`.

## Tone cleanup

- Avoid `simply`, `just`, `obviously`, and `clearly`.
- Avoid `above`, `below`, `left`, `right`, `top`, and `bottom` when referring to content.
- Acknowledge difficulty naturally, such as `this step can be confusing at first`.
- Normalize errors, such as `if you see this error, here's how to fix it`.
- Use contractions such as `don't`, `isn't`, `it's`, `that's`, `you're`, and `you'll`.
- Remove unnecessary qualifiers such as `quite`, `very`, and `massive`.
- Use `an LLM`, not `a LLM`.
- Use `easy-to-use` as an adjective.
- Use `fixed-width`, not `fixed-length`.
- Use `read-to-write ratio`, not `read to write ratio`.

## UI and formatting terms

- Use `select` or `tap` instead of `click` for touch interfaces.
- Use `keyboard shortcut` instead of `key combination`.
- Use `Ctrl key`.
- Use `double-tap` instead of `double-click` for touch interfaces.
- Use **bold** for UI elements.
- Use *italics* for emphasis and new terms.
- Use `code formatting` for file names, commands, package names, flags, paths, and environment variables.

## Headings and terminology

- Use sentence case for headings and subheadings.
- Capitalize only the first word and proper nouns in headings.
- Keep heading wording consistent across related files.
- Prefer headings that signal the user task or concept.
- Ensure heading hierarchy has no skipped levels unless the template requires it.
- Each Markdown file should begin with a section heading in body content.
- Use `Arm` for the brand in prose.
- Use `arm64` or `aarch64` for CPU architecture based on tool, package, or OS convention.
- Use `ARM64` only when referring to Windows on Arm or Microsoft documentation.
- Capitalize `Learning Path`.
- Use `Azure Cobalt`, `Google Axion`, and `AWS Graviton` as processor names, not VM names. `Graviton-based instances`, not `Graviton instances`, for example.
- Do not use bold or italics for product names such as LiteRT, XNNPACK, KleidiAI, and SME2 unless they are headings or UI labels.

## Avoid AI-sounding prose

- Avoid more than three consecutive sections using bullet lists.
- Avoid bullets that would read more naturally as narrative paragraphs.
- Make list items parallel.
- Use flowing narrative where it improves readability.
- Vary sentence length.
- Use transitional phrases and relevant examples.
- Connect ideas logically.
- Avoid robotic encouragement such as `Great job - let's get started!`.
- Avoid multiple consecutive sentences starting with `This`.

## Response format

For reviews, lead with findings ordered by severity and include file and line references. Then add open questions or assumptions, followed by a short summary.

For edits, summarize the style changes and note any checks performed.
