# Project Overview

This project is a collection of "Learning Paths" (long-form tutorials) and "install guides" (shorter software installation guides), hosted on a static website using Hugo and markdown files. The content explains how to develop software on Arm for software developers targeting various Arm platforms.

Assume the audience is made up of Arm software developers. Bias all information toward Arm platforms. For Linux, assume systems are aarch64 architecture and not x86. Readers also use macOS and Windows on Arm systems, and assume Arm architecture where relevant.

## Highest priority rules

- Each Learning Path must own one clear developer task
- Install guides are for installation and verification only
- Every Learning Path `_index.md` must include a `description` field
- Use task-led titles, introductions, and metadata
- Do not use placeholder alt text such as `alt-txt`
- Prefer Arm-native solutions and Arm-specific framing
- Avoid hype, duplication, and vague summaries

## Project structure

The key directories are:

### Top-level structure

- `/content` - The main directory containing all Learning Paths and install guides as markdown files
- `/themes` - HTML templates and styling elements that render the content into the final website
- `/tools` - Python scripts for automated website integrity checking
- `config.toml` - High-level Hugo configuration settings

### Content organization

The `/content` directory is organized into:

- `learning-paths/` - Core learning content organized by categories:
  - `embedded-and-microcontrollers/` - MCU, IoT, and embedded development topics
  - `servers-and-cloud-computing/` - Server, cloud, and enterprise computing topics
  - `mobile-graphics-and-gaming/` - Mobile app development, graphics, and gaming
  - `cross-platform/` - Cross-platform development and general programming topics, these appear in multiple categories on the website
  - `laptops-and-desktops/` - Desktop application development, primarily Windows on Arm and macOS
  - `automotive/` - Automotive and ADAS development
  - `iot/` - IoT-specific Learning Paths

- `install-guides/` - Tool installation guides with supporting subdirectories organized by tool categories like `docker/`, `gcc/`, `license/`, `browsers/`, plus an `_images/` directory for screenshots and diagrams

These are special directories and not used for regular content creation:

- `migration/` - Migration guides and resources, this maps to https://learn.arm.com/migration
- `lists/` - Content listing and organization files, this maps to https://learn.arm.com/lists
- `stats/` - Website statistics and analytics, this maps to https://learn.arm.com/stats

The `/content` directory is the primary workspace where contributors add new Learning Paths as markdown files, organized into category-specific subdirectories that correspond to the different learning path topics available on the site at https://learn.arm.com/.

## Content requirements

Read the files in the directory `content/learning-paths/cross-platform/_example-learning-path` for information about how Learning Path content should be created. Also see the guidelines below.

- Learning Paths: use for end-to-end tasks (prepare → configure → use → validate). Must include `_index.md` and `_next-steps.md`
- Install guides: use for installation + verification only. Do not include workflow content or benchmarks

## Writing style

### Voice and tone

- Second person (`you`, `your`) — never first person (`I`, `we`)
- Active voice — avoid passive constructions
- Present tense for descriptions
- Imperative mood for commands
- Confident and developer-friendly tone
- Encouraging language for complex tasks
- Use inclusive language:
  - Use `primary/subordinate` instead of `master/slave`
  - Do not use gendered examples or assumptions
  - Be mindful of cultural references that might not translate globally
  - Focus on clear, accessible language for all developers

### Sentence structure and clarity

- Average 15–20 words per sentence
- Split complex sentences for clarity
- Use plain English and avoid jargon overload
- Use US spellings (`organize`, `optimize`, `realize`)
- Use `Arm` capitalization in prose (`Arm processors`, `Arm servers`, `Neoverse`)
- `arm64` and `aarch64` are permitted in code, commands, and outputs
- Define acronyms on first use
- Use parallel structure in all lists

### Readability and section flow

- Flag any section over 700 words and suggest natural split points
- Warn if more than 300 words appear between code examples
- Identify paragraphs with sentences averaging over 20 words
- Note sections introducing more than two new concepts
- Flag pages over 3500 words total
- Note sections that might benefit from encouragement or progress markers
- Identify missing celebration of progress or milestones
- Recap what learners have accomplished at section ends
- Provide check-your-understanding moments that are not intimidating
- Use visual breaks to prevent walls of text. Code blocks count as visual breaks
- If you explain three or more things in one section, split it into separate sections
- Each code block should be preceded by one to three sentences explaining what it does
- If a section is long because of code or output rather than explanation, do not treat length alone as a readability problem

### Word choice and style

Use these preferred terms and phrases for consistency:

- Numbers and units:
  - Spell out numbers one through five. After that, use numerals
  - Use proper spacing for units: `1 GB`, `23 MB/day`
  - Use `K` for thousands: `64K`
  - Use abbreviations for data rates: `Gbps`

- Common phrases:
  - `To [action]` instead of `Follow the steps below to [action]`
  - `for example` instead of `e.g.`
  - `that is` instead of `i.e.`
  - `because` instead of `since`
  - `also` instead of `in addition`
  - `to` instead of `in order to`
  - `see` instead of `refer to`
  - `use` instead of `utilize` or `leverage`
  - `need` instead of `require`
  - `can` or `might` instead of `may`
  - `set up` as a verb, `setup` as a noun
  - `therefore` instead of `ergo`
  - `namely` instead of `viz.`
  - `avoid` instead of `try not to`
  - `such as` instead of `like`
  - `after` instead of `once`

- Avoid condescending language:
  - Do not use `simply`, `just`, `obviously`, or `clearly`

- Avoid using directions when referring to content that's been referenced previously or will be referenced next:
- Do not use `above`, `below`, `left`, `right`, `top`, or `bottom`

- Acknowledge difficulty naturally:
  - Use phrases like `this step can be confusing at first`

- Normalize errors:
  - Use phrases like `if you see this error, here's how to fix it`

- User interface terms:
  - `select` or `tap` instead of `click` for touch interfaces
  - `keyboard shortcut` instead of `key combination`
  - `Ctrl key` capitalized
  - `double-tap` instead of `double-click` for touch interfaces

- Contractions and simplification:
  - Use contractions such as `don't`, `isn't`, `it's`, `that's`, `you're`, `you'll`
  - Remove unnecessary qualifiers such as `quite`, `very`, or `massive`
  - Use `an LLM`, not `a LLM`
  - Use `easy-to-use` as an adjective
  - Use `fixed-width`, not `fixed-length`
  - Use `read-to-write ratio`, not `read to write ratio`

- The term "Learning Path" should always be capitalized.

## Content structure and consistency

### Cross-file and quality assurance

- Keep terminology, capitalization, abbreviations, voice, tone, formatting, and technical depth consistent across related files.
- Match content complexity to the stated audience, prerequisites, and skill level.
- Use consistent heading hierarchy, section flow, code block formatting, lists, and callouts.
- Flag inconsistent terminology, missing troubleshooting, unclear prerequisites, overly complex sections, and places where visuals would improve understanding.
- Verify code examples follow established repository patterns.
- Add or improve metadata descriptions when editing related content.

## Formatting and code samples

### Heading guidelines

- Use sentence case for all headings
- Heading types:
  - Conceptual headings: when explaining technology or motivation
  - Imperative headings: when the user takes action
  - Interrogative headings: for FAQ content

- Hierarchy:
  - H1: Page title
  - H2: Major workflow steps or conceptual sections
  - H3: Sub-procedures or detailed explanations
  - H4: Specific technical details or troubleshooting within a workflow

### Heading hierarchy and section openings

- Check heading hierarchy across all files before finalizing content
- Ensure headings follow a logical structure with no skipped levels unless the template requires it
- Each markdown file should begin with a section heading in the body content
- Do not leave a file starting with body text, an image, or a code block without a heading
- Use sentence case for all headings and subheadings
- Capitalize only the first word and proper nouns in headings
- Keep heading wording consistent across related files in the same Learning Path
- Prefer headings that clearly signal the user task or concept in that section

Correct examples:
- `## Set up the environment`
- `## Run the benchmark`
- `### Check the output`
- `## What you've accomplished and what's next`

Avoid:
- `## Set Up The Environment`
- `## RUN THE BENCHMARK`
- starting a file with plain paragraph text and no heading

### Code samples and formatting

- Always provide explanation before code blocks
- Format: `[What it does] → [Code] → [Expected outcome] → [Key parameters]`
- Use markdown tags for languages like `bash`, `python`, `yaml`, `json`
- Use `console` or `bash` for general commands. Try to use the same one throughout a Learning Path or Install Guide
- Use the `output` tag to show expected command output
- Output descriptions:
  - Use `The output is similar to:` or `The expected output is:`
  - Use present tense descriptions such as `builds` and `gives`
- Formatting standards:
  - **Bold** for UI elements
  - *Italics* for emphasis and new terms
  - `Code formatting` for file names, commands, and code elements
- Use shortcodes for common pitfalls, warnings, and important notes

### Code fence integrity

- Every fenced code block opened with triple backticks must be explicitly closed with matching triple backticks before any non-code content resumes
- Never generate unterminated or partial code fences
- Do not rely on implicit closure, indentation, or surrounding formatting to end a code block

## Arm naming and architecture terms

- Use `Arm` for the brand in prose
- Use `arm64` or `aarch64` for the CPU architecture. Prefer whichever term a tool, package, or OS uses natively
- Always use `Arm` rather than `ARM` in prose unless a technical term requires the original casing
- `ARM64` is acceptable when specifically referring to Windows on Arm or Microsoft documentation
- In code blocks, CLI flags, package names, file paths, and outputs, keep the exact casing used by the tool

## Product name emphasis

- Product names and technologies such as LiteRT, XNNPACK, KleidiAI, and SME2 should appear in regular text
- Avoid using italics or bold to emphasize product or technology names unless they are part of a heading or a UI label

## Hyperlink guidelines

- Use the full path format for internal links: `/learning-paths/category/path-name/`
- Do not use relative paths like `../path-name/`
- Use the full URL for external links that are not on `learn.arm.com`
- Include only necessary links in content. 

## Avoid looking like AI-generated content

- Warning signs of over-bulleting:
  - More than three consecutive sections using bullet lists
  - Bullet points that could be combined into narrative paragraphs
  - Lists where items do not have parallel structure
  - Bullet points that are actually full sentences better suited for paragraphs

- Use flowing narrative instead of excessive bullets
- Use natural writing patterns:
  - Vary sentence length
  - Use transitional phrases
  - Include contextual explanations
  - Add relevant examples
  - Connect ideas logically

- Use conversational elements naturally:
  - Instead of `Execute the following command:`, use `Now that you've configured the environment, run the following command to start the service:`
  - Instead of `This provides benefits:`, use `You'll notice several advantages with this approach, particularly when working with...`

### Language smoothing

Avoid robotic or generic encouragement phrases such as:
- `Great job — let’s get started!`
- `Great job — your environment is ready!`

Use calm, natural transitions that focus on what happens next.

Also avoid multiple consecutive sentences starting with `This`. Vary sentence structure to maintain natural flow.

For additional instructions related to images, Learning Paths, Install Guides, and content quality, see [instructions](./instructions/).