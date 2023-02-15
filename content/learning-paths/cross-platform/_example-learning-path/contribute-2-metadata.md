---
# User change
title: "2b) Modify Metadata"

weight: 6 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
<!-- ![alt-text #center](2-contribution-process.PNG "Contribution process") -->
## Learning Path Metadata

Each Learning Path contains metadata which is used to create the Learning Path pages. The metadata is used by the website so all Learning Paths have the same information and look the same. 

This section explains how to add Learning Path metadata in three files:

1. Metadata and Tagging information in `_index.md`
2. Review Questions for comprehension provided in `_review.md`
3. Next Steps for readers in `_next-steps.md`

## Metadata and Tagging 

The following metadata is defined in the `_index.md` file:

| Learning Path Metadata | Explanation |
|---------------|----------|
| title                 | Should start with a verb (learn, build), have no adjectives (amazing, cool), and be as concise as possible (limit one sentence).       |
| description           | One sentence summary of the Learning Path. |
| minutes_to_complete   | Time to perform the steps in the Learning Path (not just read it). |
| who_is_this_for       | One sentence indicating the target audience (developers using tools or software to accomplish tasks). |
| learning_objectives   | 2-5 bullet points, one sentence each, describing what a reader will learn. Should start with a verb (deploy, measure). |
| prerequisites         | Details anything needed before this Learning Path can be started. Can include online service accounts, prior knowledge, previous Learning Paths, or specific tools and software. Offers explanatory links when possible. |
| author_primary      | The name of the person who wrote the Learning Path in case there are questions about the material. |

{{% notice Note%}}
To specify a prerequisite Learning Path, do so with a relative path. An example:
- *The Learning Path on [Getting Started with Docker](../../docker) should be completed first.* was specified with this link: (../../docker) 
{{% /notice %}}

## Tags
Tagging metadata is also expected to increase visibility via filtering. Some tags are closed (you must select from a pre-defined list) and some are open (enter anything). The tags are:

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
| MacOS         |
| ChromeOS      |
| iOS           |
| Android       |
| RTOS          |
| Baremetal     |


### tools_software_languages (open)
Specifies the tools, softwares, or languages this Learning Path uses. Please list out any key tools, software, or languages your learning path uses.

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
Specifies the Arm IP this Learning Path involves, providing a quick link to IP information for developers interested in learning more. You can enter multiple specific or groups of IP. Note that this is not used for filtering content, but is clickable for readers to find more information about these IPs through seaching automatically on developer.arm.com.

| Grouping Type | When to use | Examples |
|--------------|-----|-----|
| Specific IP | The Learning Path covers a specific board with one (or a few) Arm IP | Cortex-M4, Neoverse-N1, Mali-G57 |
| Group of IP | The Learning Path applies to a wider class of Arm IP | Cortex-M, Cortex-A, Cortex-R, Neoverse, Mali |



## Review Questions 

Review questions both validate comprehension and re-enforce specific learning ideas. At least two questions should be provided; three questions is ideal. Each question is multiple choice. They are specified in the _review.md file as follows:

| Review Metadata | Explanation |
|---------------|----------|
| question          | A one sentence question to the reader       |
| answers           | The multiple choice answers  |
| correct_answer    | An integer indicating what answer is correct (1 for the first listed, etc.)  |
| explanation       | A short, 1-2 sentence explanation of why the question has that answer.  |

For a great simple example of this concept see the [MongoDB Learning Path review](../../../server-and-cloud/mongodb/_review).

{{% notice %}}
The explanation is displayed whether or not the reader selects the correct answer. Avoid phrases like "Correct! *This* is because..." and opt for phrasing like "*this* is correct because..."
{{% /notice %}}

## Next Steps

This is where you provide a specific next step for a reader, and provide further reading resources to dive deeper into the topics covered. The following metadata is defined in the _next-steps.md file:

| Next Steps Metadata   | Explanation |
|-----------------------|-------------|
| next_step_guidance    | A 1-3 sentence description of how the reader can generally keep learning about these topics, and a specific explanation of why the next step is being recommended.   |
| recommended_path      | Link to the next learning path being recommended (For example, this could be [Learn How to Use Docker](../../docker)) |
| further_reading       | Links to references related to information covered |
| resource > title      | The displayed title of the provided further_reading resource |
| resource > link       | The website link to the specific resource |
| resource > type       | Helps the reader understand what type of resource is being suggested.  Can be either: (1) Manuals for a tool / software (type: documentation). (2) Blog about related topics (type: blog). (3) General online references (type: website). |

