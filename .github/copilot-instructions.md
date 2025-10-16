# Project Overview

This project is a collection of "learning paths" (long-form tutorials) and "install guides" (shorter software installation guides), hosted on a static website using Hugo and markdown files. The content explains how to develop software on Arm for software developers targeting various Arm platforms.

Assume the audience is made up of Arm software developers. Bias all information toward Arm platforms. For Linux, assume systems are aarch64 architecture and not x86. Readers also use macOS and Windows on Arm systems, and assume Arm architecture where relevant.

## Project structure

The key directories are:

### Top level structure

/content - The main directory containing all Learning Paths and install guides as markdown files
/themes - HTML templates and styling elements that render the content into the final website
/tools - Python scripts for automated website integrity checking
config.toml - High-level Hugo configuration settings

### Content organization:

The /content directory is organized into:

- learning-paths/  Core learning content organized by categories:
  -- embedded-and-microcontrollers/  MCU, IoT, and embedded development topics
  -- servers-and-cloud-computing/  Server, cloud, and enterprise computing topics  
  -- mobile-graphics-and-gaming/  Mobile app development, graphics, and gaming
  -- cross-platform/  Cross-platform development and general programming topics, these appear in multiple categories on the website
  -- laptops-and-desktops/  Desktop application development, primarily Windows on Arm and macOS
  -- automotive/  Automotive and ADAS development
  -- iot/  IoT-specific Learning Paths

- install-guides/ - Tool installation guides with supporting subdirectories organized by tool categories like docker/, gcc/, license/, browsers/, plus an _images/ directory for screenshots and diagrams

These are special directories and not used for regular content creation:
 migration/ Migration guides and resources, this maps to https://learn.arm.com/migration
 lists/ Content listing and organization files, this maps to https://learn.arm.com/lists
 stats/ Website statistics and analytics, this maps to https://learn.arm.com/stats

The /content directory is the primary workspace where contributors add new Learning Paths as markdown files, organized into category-specific subdirectories that correspond to the different learning path topics available on the site at https://learn.arm.com/.

## Content requirements

Read the files in the directory `content/learning-paths/cross-platform/_example-learning-path` for information about how Learning Path content should be created. Also see the guidelines below.

### Content structure

Each Learning Path must have an _index.md file and a _next-steps.md file. The _index.md file contains the main content of the Learning Path. The _next-steps.md file contains links to related content and is included at the end of the Learning Path.

Additional resources and 'next steps' content should be placed in the `further_reading` section of `_index.md`, NOT in `_next-steps.md`. The `_next-steps.md` file should remain minimal and unmodified as indicated by "FIXED, DO NOT MODIFY" comments in the template.

The _index.md file should contain the following front matter and content sections:

Front Matter (YAML format):
- `title`: Imperative heading following the [verb] + [technology] + [outcome] format
- `weight`: Numerical ordering for display sequence, weight is 1 for _index.md and each page is ordered by weight, no markdown files should have the same weight in a directory
- `layout`: Template type (usually "learningpathall")
- `minutes_to_complete`: Realistic time estimate for completion
- `prerequisites`: List of required knowledge, tools, or prior learning paths
- `author_primary`: Main contributor's name, multiple authors can be listed separated using - on new lines
- `subjects`: Technology categories for filtering and search, this is a closed list and must match one of the subjects listed on https://learn.arm.com/learning-paths/cross-platform/_example-learning-path/write-2-metadata/
- `armips`: Relevant Arm IP, stick to Neoverse, Cortex-A, Cortex-M, etc. Don't list specific CPU models or Arm architecture versions
- `tools_software_languages`: Open category listing Programming languages, frameworks, and development tools used
- `skilllevels`: Skill levels allowed are only Introductory and Advanced
- `operatingsystems`: Operating systems used, must match the closed list on https://learn.arm.com/learning-paths/cross-platform/_example-learning-path/write-2-metadata/

### Further reading curation

Limit further_reading resources to four to six essential links. Prioritize:
- Direct relevance to the topic
- Arm-specific Learning Paths over generic external resources
- Foundation knowledge for target audience
- Required tools (install guides)
- Logical progression from basic to advanced

Avoid overwhelming readers with too many links, which can cause them to leave the platform.

All Learning Paths should generally include:
Title: [Imperative verb] + [technology/tool] + [outcome]
Introduction paragraph: Context + user goal + value proposition
Prerequisites section with explicit requirements and links
Learning objectives: three to four bulleted, measurable outcomes with action verbs
Step-by-step sections with logical progression
Clear next steps/conclusion

For title formatting:
- MUST use imperative voice ("Deploy", "Configure", "Build", "Create")
- MUST include SEO keywords (technology names, tools)
- Examples: "Deploy applications on Arm servers", "Configure Arm processors for optimal performance"

The term "Learning Path" should always be capitalized.

### Writing style

Voice and Tone:
- Second person ("you", "your") - NEVER first person ("I", "we")
- Active voice - AVOID passive constructions
- Present tense for descriptions
- Imperative mood for commands
- Confident and developer-friendly tone
- Encouraging language for complex tasks
- Use inclusive language: 
  - Use "primary/subordinate" instead of "master/slave" terminology
  - Don't use gendered examples or assumptions
  - Be mindful of cultural references that might not translate globally
  - Focus on clear, accessible language for all developers

### Sentence structure and clarity
- Average 15-20 words per sentence
- Split complex sentences for scalability
- Plain English - avoid jargon overload
- US spellings required (organize/optimize/realize, not organise/optimise/realise)
- "Arm" capitalization required (Arm processors/Neoverse, never ARM or arm; exceptions: "arm64" and "aarch64" are permitted in code, commands, and outputs)
- Define acronyms on first use
- Parallel structure in all lists

### Readability and section flow
- Flag any section over 700 words and suggest natural split points
- Warn if more than 300 words appear between code examples
- Identify paragraphs with sentences averaging over 20 words
- Note sections introducing more than 2 new concepts
- Flag pages over 3500 words total
- Note sections that might benefit from encouragement or progress markers
- Identify missing celebration of progress or milestones
- Recap what learners have accomplished at section ends
- Provide "check your understanding" moments that aren't intimidating
- Too much explanation is exhausting, too little is confusing
- Use visual breaks to prevent walls of text - code blocks count as visual breaks
- Walls of text cause people to bounce from the page
- If you're explaining 3+ things in one section, split it into separate sections
- Each code block should be preceded by one to three sentences explaining what it does.

### Word choice and style
- Use these preferred terms and phrases for consistency:
  - Numbers and units: Spell out numbers one through five (one, two, three, four, five), after this use numerals (6, 7, 8...). Use proper spacing for units: "1 GB", "23 MB/day" (not "1GB", "23MB/day"). Use "K" for thousands: "64K" (not "64k"). Use abbreviations for data rates: "Gbps" (not "Gb per second").
 - Common phrases: "To [action]" (not "Follow the steps below to [action]"), "for example" (not "e.g."), "that is" (not "i.e."), "because" (not "since"), "also" (not "in addition"), "to" (not "in order to"), "see" (not "refer to"), "use" (not "utilize" or "leverage"), "need" (not "require"), "can" or "might" (not "may"), "set up" as verb, "setup" as noun, "therefore" (not "ergo"), "namely" (not "viz."), "avoid" (not "try not to").
  - Avoid condescending language: Don't use "simply", "just", "obviously", "clearly" - what's simple to you might not be to the learner.
  - Acknowledge when something can be tricky: Use phrases like "this step can be confusing at first" to validate learner experience.
  - Normalize errors: Use phrases like "if you see this error, here's how to fix it" to reassure learners that errors are part of the learning process.
  - User interface terms: "select" or "tap" (not "click" for mobile/touch interfaces), "keyboard shortcut" (not "key combination"), "Ctrl key" (capitalized), "double-tap" (not "double-click" for touch interfaces).
  - Contractions and simplification: Use contractions such as: "don't", "isn't", "it's", "that's", "you're", "you'll". Remove unnecessary qualifiers: Remove "quite", "very", "massive" → "significant". "an LLM" (not "a LLM"). "easy-to-use" when used as adjective. "fixed-width" (not "fixed-length"). "read-to-write ratio" (not "read to write ratio").

## Content structure and consistency

### Cross-file and quality assurance
- Use the same technical terms consistently throughout all sections
- Apply the word choice and style guidelines uniformly across all files
- Maintain consistent capitalization of product names, technologies, and concepts
- Use the same abbreviations and acronyms throughout (define once, use consistently)
- Maintain the same voice and tone across all sections
- Ensure consistent use of second person ("you", "your") throughout
- Apply the same level of formality and technical depth across sections
- Keep instructional style consistent (imperative mood for actions)
- Follow consistent heading hierarchy throughout the Learning Path
- Use parallel structure in similar sections across different files
- Maintain consistent section organization and flow
- Apply uniform formatting for code blocks, lists, and callouts
- Ensure appropriate skill level consistency (Introductory or Advanced)
- Maintain consistent technical detail appropriate for the target audience
- Balance complexity appropriately across all sections
- Provide consistent prerequisite assumptions throughout
- Flag inconsistent terminology usage across sections
- Identify missing error handling or troubleshooting guidance
- Suggest where visual aids (diagrams, screenshots) would improve understanding
- Recommend splitting overly complex sections
- Verify that code examples follow established patterns in the repository

## Formatting and code samples

### Heading guidelines
- Use sentence case for all headings (first word capitalized, rest lowercase except proper nouns)
- Heading types:
  - Conceptual headings: When explaining technology/motivation ("What is containerization?")
  - Imperative headings: When user takes action ("Configure the database")
  - Interrogative headings: For FAQ content ("How does Arm differ from x86?")
- Hierarchy:
  - H1: Page title (imperative + technology + outcome)
  - H2: Major workflow steps or conceptual sections
  - H3: Sub-procedures or detailed explanations
  - H4: Specific technical details or troubleshooting

### Code samples and formatting
- ALWAYS provide explanation before code blocks
- Format: [What it does] → [Code] → [Expected outcome] → [Key parameters]
- Use markdown tags for programming languages like bash, python, yaml, json, etc.
- Use console or bash for general commands. Try to use the same one throughout a Learning Path.
- Use the output tag to show expected command output.
- Output descriptions: Use "The output is similar to:" or "The expected output is:" (not "The output will look like:"). Use "builds" (not "will build") and "gives" (not "would give") for present tense descriptions.
- Formatting standards: **Bold text** for UI elements (buttons, menu items, field names), *Italic text* for emphasis and new terms, `Code formatting` for file names, commands, code elements.
- Use shortcodes for common pitfalls, warnings, important notes.

## Arm naming and architecture terms
- Use Arm for the brand in prose (for example, "Arm processors", "Arm servers").
- Use arm64 or aarch64 for the CPU architecture; these are acceptable and interchangeable labels. Prefer whichever term a tool, package, or OS uses natively.
- Always use "Arm" (not "ARM") in all contexts except when referring to specific technical terms that require the original casing.
- ARM64 is used by Windows on Arm and Microsoft documentation, so it is acceptable to use ARM64 when specifically referring to Windows on Arm.
- In code blocks, CLI flags, package names, file paths, and outputs, keep the exact casing used by the tool (for example, --arch arm64, uname -m → aarch64).

## Hyperlink guidelines
- Use the full path format for internal links: `/learning-paths/category/path-name/` (e.g., `/learning-paths/cross-platform/docker/`). Do NOT use relative paths like `../path-name/`.
- Use the full URL for external links that are not on learn.arm.com, these open in a new tab.
- When creating Learning Path content:
  - Verify internal links exist before adding them
  - Use semantic search or website browsing to confirm Learning Path availability
  - Prefer verified external authoritative sources over speculative internal links
  - Test link formats against existing Learning Path examples
  - Never assume Learning Paths exist without verification
- Some links are useful in content, but too many links can be distracting and readers will leave the platform following them. Include only necessary links in the content; place others in the "Next Steps" section at the end. Flag any page with too many links for review.

## Avoid looking like AI-generated content
- Warning signs of over-bulleting: More than 3 consecutive sections using bullet lists, bullet points that could be combined into narrative paragraphs, lists where items don't have parallel structure, bullet points that are actually full sentences better suited for paragraphs.
- Use flowing narrative instead of excessive bullets.
- Use natural writing patterns: Vary sentence length, use transitional phrases, include contextual explanations, add relevant examples, connect ideas logically.
- Use conversational elements: Instead of "Execute the following command:", use "Now that you've configured the environment, run the following command to start the service:". Instead of "This provides benefits:", use "You'll notice several advantages with this approach, particularly when working with...".

## AI-specific guidelines for content creation and editing

### Context awareness
- Consider the learner's likely environment (development vs. production, local vs. cloud)
- Recognize when content assumes x86 defaults and suggest Arm alternatives
- Flag when third-party tools may have limited Arm support
- Suggest Arm-native alternatives when available (e.g., Arm compilers, optimized libraries)

### Technical depth consistency
- Maintain appropriate complexity level throughout the Learning Path
- Avoid oversimplifying for Advanced skill level content
- Don't assume prior knowledge beyond stated prerequisites
- Balance theoretical explanation with practical implementation

### Platform-specific considerations
- Default to Arm-optimized solutions and configurations
- Mention x86 alternatives only when Arm solutions don't exist
- Consider performance implications specific to Arm architectures
- Address common Arm migration challenges when relevant

### Quality assurance
- Flag inconsistent terminology usage across sections
- Identify missing error handling or troubleshooting guidance
- Suggest where visual aids (diagrams, screenshots) would improve understanding
- Recommend splitting overly complex sections
- Verify that code examples follow established patterns in the repository

### Accessibility and inclusivity
- Ensure content is screen reader compatible
- Provide descriptive alt text for images and diagrams
- Use clear, descriptive link text (not "click here" or "read more")
- Avoid assumptions about user's physical capabilities or setup

### SEO and discoverability
- Use Arm-specific keywords naturally throughout content
- Include relevant technical terms that developers search for
- Optimize titles and headings for search engines
- Use semantic HTML structure in markdown when possible
- Consider how content will appear in search results

### Cross-reference validation
- Verify all internal links point to existing content
- Check that referenced Learning Paths and install guides are current
- Ensure cross-references between sections remain accurate after edits
- Flag broken or outdated external links
- Maintain consistency in how related content is referenced

### Performance testing guidance
- Include benchmarks when comparing Arm vs. x86 performance
- Suggest performance testing steps for resource-intensive applications
- Recommend profiling tools that work well on Arm platforms
- Include guidance on measuring and optimizing for Arm-specific performance characteristics
- Mention when performance improvements are architecture-specific

### AI optimization (AIO) guidance
- Structure content with clear, semantic headings that AI can parse and understand
- Use descriptive, standalone sentences that make sense without surrounding context
- Include explicit problem statements and clear solutions for AI to reference
- Format code examples with proper language tags and clear explanations
- Use consistent terminology that AI systems can reliably associate with Arm development
- Include complete, self-contained examples rather than partial snippets
- Write FAQ-style sections that directly answer common developer questions
- Use bullet points and numbered lists for AI to easily extract key information
- Include explicit "what you'll learn" and "prerequisites" sections for AI context
- Structure troubleshooting sections with clear problem-solution pairs
- Use standard markdown formatting that AI crawlers can parse effectively
- Include relevant technical keywords naturally throughout the content
- Write comprehensive summaries that AI can use as content overviews
- Ensure each section can stand alone as a coherent piece of information
- Use clear, declarative statements rather than implied or contextual references

Your Azure Cobalt 100 Arm64 virtual machine is now ready. Continue to the next step to install and configure MySQL.