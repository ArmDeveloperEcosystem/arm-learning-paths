---
# User change
title: "Modify Learning Path metadata"

weight: 5 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Modify Learning Path metadata

Each Learning Path contains metadata which is used to create the Learning Path pages. The metadata is used by the website so all Learning Paths have the same information and are consistent. 

This section explains how to add Learning Path metadata in two files:

1. Metadata and Tagging information in `_index.md`
2. Next Steps for readers in `_next-steps.md`

## Metadata and tagging 

The following metadata is defined in the `_index.md` file:

| Learning Path Metadata | Explanation |
|---------------|----------|
| title                 | Should start with a verb (learn, build), have no adjectives (amazing, cool), and be as concise as possible (limit one sentence).       |
| minutes_to_complete   | Time to perform the steps in the Learning Path (not just read it). |
| who_is_this_for       | One sentence indicating the target audience (developers using tools or software to accomplish tasks). |
| learning_objectives   | 2-5 bullet points, one sentence each, describing what a reader will learn. Should start with a verb (deploy, measure). |
| prerequisites         | Everything needed before this Learning Path can be started. Can include online service accounts, prior knowledge, previous Learning Paths, or specific tools and software. Offers explanatory links when possible. |
| author_primary      | The name of the person who wrote the Learning Path in case there are questions about the material. |

Look at other Learning Paths for inspiration about how to write a good title, learning objectives, and prerequisites. 

{{% notice Note%}}
To specify a prerequisite Learning Path, do so with an absolute path from the root of the website. For example:

- The Learning Path [Learn how to use Docker](/learning-paths/cross-platform/docker/) should be completed first 

Note the absolute path of `/learning-paths/cross-platform/docker/` 
{{% /notice %}}

### Author information

If you provide your name in the `author_primary` metadata it will be listed on the top of the Learning Path in the `Author` field.

Displaying your name on the content you contributed is a great way to promote your work. 

If you do not want your name to be displayed leave `author_primary` blank. 

You can share additional information about yourself by editing the file [`contributors.csv`](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/blob/main/assets/contributors.csv) at the top of the repository. This file collects your company name, GitHub username, LinkedIn profile, Twitter handle, and your website. All fields are optional, but any you add to `contributors.csv` will appear next to your name in the `Author` field.

## Tags
Tagging metadata is also expected to increase visibility through filtering. Some tags are closed (you must select from a pre-defined list) and some are open (enter anything). The tags are:

### skilllevels (closed)
Indicates the skill level needed as a developer to complete this Learning Path.

| Option | Explanation |
|--------------|--------------------|
| Introductory | Requires minimal experience in this field or previous knowledge about the tools/software involved |
| Advanced     | Requires experience with specific topics, tools, or software to properly understand this tutorial |

### subjects (closed)
Specifies the primary subject the Learning Path covers. Can only be one subject per Learning Path; if it spans multiple, pick the primary one. Select from the allowed list for each category, as defined here:

| Server and Cloud | Desktop and Laptop | Embedded | Mobile | Microcontroller |
|---------|---------|---------|---------|---------|
| CI-CD | CI-CD | CI-CD| CI-CD | CI-CD |
| Performance and Architecture | Performance and Architecture | Performance and Architecture | Performance and Architecture | Performance and Architecture |
| ML | Migration to Arm | ML | ML | ML |
| Containers and Virtualization | Containers and Virtualization | Containers and Virtualization | Gaming | Security |
| Storage | | Storage | AR-VR | Virtual Hardware |
| Databases | | Automotive | Graphics | RTOS  |
| Libraries | | Embedded Linux | | Libraries |
| Web | | | | |
| Networking | | | | |


### operatingsystems (closed)

Specifies the operating systems this Learning Path can run on. Select from this list:

| OS Options    |
|---------------|
| Linux         |
| Windows       |
| macOS         |
| ChromeOS      |
| iOS           |
| Android       |
| RTOS          |
| Baremetal     |


### tools_software_languages (open)

Specifies the tools, softwares, or languages this Learning Path uses. Please list out any key tools, software, or languages your Learning Path uses.

| Tag Type     | Examples |
|---------------|----------|
| Environments  | AWS EC2, GCP                      |
| Toolchains    | GCC, Arm Compiler for Embedded    |
| IDEs          | Arm Development Studio, VS Code   |
| Online Tools  | GitHub, Jenkins                   |
| Assorted      | cbuild, Docker                    |
| Stack         | tinyML, CMSIS             |
| Language      | Python, Java, Assembly    |
| Libraries     | zlib, snappy  |


### arm_ips (open)

Specifies the Arm IP this Learning Path involves, providing a quick link to IP information for developers interested in learning more. You can enter multiple specific or groups of IP. Note that this is not used for filtering content, but is clickable for readers to find more information about these IPs through searching automatically on developer.arm.com.

| Grouping Type | When to use | Examples |
|--------------|-----|-----|
| Specific IP | The Learning Path covers a specific board with one (or a few) Arm IP | Cortex-M4, Neoverse-N1, Mali-G57 |
| Group of IP | The Learning Path applies to a wider class of Arm IP | Cortex-M, Cortex-A, Cortex-R, Neoverse, Mali |


## Next Steps

This is where you provide a specific next step for a reader, and provide further reading resources to dive deeper into the topics covered. The following metadata is defined in the _next-steps.md file:

| Next Steps Metadata   | Explanation |
|-----------------------|-------------|
| next_step_guidance    | A 1-3 sentence description of how the reader can generally keep learning about these topics, and a specific explanation of why the next step is being recommended.   |
| recommended_path      | Link to the next learning path being recommended (For example, this could be [Learn How to Use Docker](/learning-paths/cross-platform/docker/)) |
| further_reading       | Links to references related to information covered |
| resource > title      | The displayed title of the provided further_reading resource |
| resource > link       | The website link to the specific resource |
| resource > type       | Helps the reader understand what type of resource is being suggested.  Can be either: (1) Manuals for a tool / software (type: documentation). (2) Blog about related topics (type: blog). (3) General online references (type: website). |

