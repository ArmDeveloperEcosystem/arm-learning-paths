# Project Overview

This project is a static website created using Hugo and markdown files. The purpose of the content is to explain how-to topics to software developers targeting various Arm platforms. 

Assume the audience is made up of Arm software developers. Bias information toward Arm platforms. For Linux, assume systems are aarch64 architecture and not x86. Readers also use macOS and Windows on Arm systems, and assume Arm architecture where relevant.

## Project structure

The key directories are:

### Top Level Structure

 /content - The main directory containing all Learning Paths and install guides as markdown files
 /themes - HTML templates and styling elements that render the content into the final website
 /tools - Python scripts for automated website integrity checking
 config.toml - High-level Hugo configuration settings

### Content Organization:

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

Read the files in the directory `content/learning-paths/cross-platform/_example-learning-path` for information about how Learning Path content should be created. Some additional help is listed below. 

### Content structure

Each Learning Path must have an _index.md file and a _next-steps.md file. The _index.md file contains the main content of the Learning Path. The _next-steps.md file contains links to related content and is included at the end of the Learning Path.

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


All Learning Paths should generally include:
Title: [Imperative verb] + [technology/tool] + [outcome]
Introduction paragraph: Context + user goal + value proposition
Prerequisites section with explicit requirements and links
Learning objectives: 3-4 bulleted, measurable outcomes with action verbs
Step-by-step sections with logical progression
Clear next steps/conclusion

For title formatting:
- MUST use imperative voice ("Deploy", "Configure", "Build", "Create")
- MUST include SEO keywords (technology names, tools)
- Examples: "Deploy applications on Arm servers", "Configure Arm processors for optimal performance"

Learning Path should always be capitalized.

### Writing style

Voice and Tone:
- Second person ("you", "your") - NEVER first person ("I", "we")
- Active voice - AVOID passive constructions
- Present tense for descriptions
- Imperative mood for commands
- Confident and developer-friendly tone
- Encouraging language for complex tasks

Sentence Structure:
- Average 15-20 words per sentence
- Split complex sentences for scalability
- Plain English - avoid jargon overload
- US spellings required (organize/optimize/realize, not organise/optimise/realise)
- "Arm" capitalization required (Arm processors/Neoverse, never ARM or arm; exceptions: "arm64" and "aarch64" are permitted in code, commands, and outputs)
- Define acronyms on first use
- Parallel structure in all lists

### Arm naming and architecture terms

- Use Arm for the brand in prose (for example, "Arm processors", "Arm servers").
- Use arm64 or aarch64 for the CPU architecture; these are acceptable and interchangeable labels. Prefer whichever term a tool, package, or OS uses natively.
- Do not use ARM in any context.
- ARM64 is used by Windows on Arm and Microsoft documentation, so it is acceptable to use ARM64 when specifically referring to Windows on Arm.
- In code blocks, CLI flags, package names, file paths, and outputs, keep the exact casing used by the tool (for example, --arch arm64, uname -m → aarch64).

### Heading guidelines

HEADING TYPES:
- Conceptual headings: When explaining technology/motivation ("What is containerization?")
- Imperative headings: When user takes action ("Configure the database")
- Interrogative headings: For FAQ content ("How does Arm differ from x86?")
- ALL headings: Use sentence case (first word capitalized, rest lowercase except proper nouns)

HIERARCHY:
H1: Page title (imperative + technology + outcome)
H2: Major workflow steps or conceptual sections
H3: Sub-procedures or detailed explanations
H4: Specific technical details or troubleshooting

### Code samples and formatting

CONTEXT-BEFORE-CODE RULE:
- ALWAYS provide explanation before code blocks
- Format: [What it does] → [Code] → [Expected outcome] → [Key parameters]

CODE FORMATTING:

Use markdown tags for programming languages like bash, python, yaml, json, etc.

Use console or bash for general commands. Try to use the same one throughout a Learning Path. 

Correct format:

Use the following command to install required packages:

```bash
sudo apt-get update && sudo apt-get install -y python3 nodejs
```

Use the output tag to show expected command output. 

```output
Reading package lists... Done
Building dependency tree... Done
```

FORMATTING STANDARDS:
- **Bold text**: UI elements (buttons, menu items, field names)
- **Italic text**: Emphasis and new terms
- **Code formatting**: Use for file names, commands, code elements

Use shortcodes for common pitfalls, warnings, important notes

{{% notice Note %}}
An example note to pay attention to.
{{% /notice %}}

{{% notice Warning %}}
A warning about a common pitfall.
{{% /notice %}}

## Avoid looking like AI-generated content

### Bullet List Management
WARNING SIGNS OF OVER-BULLETING:
- More than 3 consecutive sections using bullet lists
- Bullet points that could be combined into narrative paragraphs
- Lists where items don't have parallel structure
- Bullet points that are actually full sentences better suited for paragraphs

CONVERSION STRATEGY:

Use flowing narrative instead of excessive bullets.

For example, use this format instead of the list below it. 

Arm processors deliver improved performance while enhancing security through hardware-level protections. This architecture provides enhanced scalability for cloud workloads and reduces operational costs through energy efficiency.

Key benefits include:
• Improved performance
• Better security
• Enhanced scalability
• Reduced costs

### Natural Writing Patterns

HUMAN-LIKE TECHNIQUES:
- Vary sentence length: Mix short, medium, and complex sentences
- Use transitional phrases: "Additionally", "However", "As a result", "Furthermore"
- Include contextual explanations: Why something matters, not just what to do
- Add relevant examples: Real-world scenarios that illustrate concepts
- Connect ideas logically: Show relationships between concepts and steps

CONVERSATIONAL ELEMENTS:

Instead of: "Execute the following command:"
Use: "Now that you've configured the environment, run the following command to start the service:"

Instead of: "This provides benefits:"
Use: "You'll notice several advantages with this approach, particularly when working with..."

## Hyperlink guidelines

Some links are useful in content, but too many links can be distracting and readers will leave the platform following them. Try to put only necessary links in the content and put other links in the "Next Steps" section at the end of the content. Flag any page with too many links for review.

### Internal links

Use a relative path format for internal links that are on learn.arm.com. 
For example, use: descriptive link text pointing to a relative path like learning-paths/category/path-name/

Examples:
- learning-paths/servers-and-cloud-computing/csp/ (Arm-based instance)
- learning-paths/cross-platform/docker/ (Docker learning path)

### External links

Use the full URL for external links that are not on learn.arm.com, these open in a new tab.

This instruction set enables high-quality Arm Learning Paths content while maintaining consistency and technical accuracy.



