---
# User change
title: "Writing style guide"

weight: 8 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

Read this section to effectively write in a style consistent with other Learning Paths. 

Content that deviates significantly from these guidelines will need to be revised.

## Voice

Voice or tone describes the way something is expressed. This is different from describing the facts that you are writing about. The same idea can be described in a variety of voices, for example, formal or informal. 

Learning Paths should be written in a clear, simple, and informal voice. You should write in a voice that anticipates the needs of your reader and is not pedantic or formal. However, do not write in a verbal style, as that is too informal.  

If you write in a clear, simple, and informal voice, your content will be easy to understand.

{{% notice Examples%}}
Too formal:
- Hardware-based security is needed to protect FIDO from malicious attack.

Recommended:
- You need hardware-based security to help protect FIDO from malicious attack.
{{% /notice %}}

&nbsp;  
&nbsp;  

## Keep It Short and Simple (KISS Principle)

Use short words, sentences, paragraphs and sections. Avoid a long or complex word when a simpler, shorter word will make the same point. Conditional words are ambiguous. For example, instead of “could”, “would”, “should”, and “may”, use “can”, “will”, and “might”.

{{% notice Examples%}}
Too confusing:
- You can nest any combination of lists.

Recommended:
- You can nest one type of list inside another.
{{% /notice %}}

&nbsp;  
&nbsp;  

## Use active voice

Use active voice. Active voice is direct. The reader knows what the subject and object of a sentence is, and the subject appears first in a sentence 

**Active voice:** Software in external memory builds the MMU page table. 

**Passive voice:** The MMU page table is built by software in external memory.

{{% notice Examples%}}
Passive voice (bad):
- We will be focusing on three versions of HPCG.

Recommended:
- We focus on three versions of HPCG.
{{% /notice %}}

&nbsp;  
&nbsp;  

## Use present tense

Use present tense because it is concrete. It emphasizes what the user can do now. And it uses fewer words. 

{{% notice Examples%}}
Not recommended:
- If you’ve entered the correct data, your product should work.

Recommended:
- Enter the correct data and your product works.
{{% /notice %}}

&nbsp;
&nbsp;

## Avoid jargon

Avoid overuse of adjectives. Avoid jargon including Latin abbreviations. 
Make content user-focused. Arm is committed to making the language we use inclusive, meaningful, and respectful. 

{{% notice Examples%}}
Too many 'filler' words:
- There are numerous different versions of the Arm architecture, which are shown as ArmvX, in which X is the designated version number, e.g., Armv8-A denotes version 8 of the Arm A-profile architecture.

Recommended:
- There are different versions of the Arm architecture. These different versions are usually shown as ArmvX, in which X is the version number. For example, Armv8-A means version 8 of the Arm A-profile architecture.
{{% /notice %}}

&nbsp;  
&nbsp;  

## Hyperlinks

Linking data allows readers to access related content quickly and easily. However, too many links can make your writing difficult to read, so use links carefully.     

Create a hyperlink for the title of the item you are linking to. Make the hyperlinked text part of your sentence. 

If possible, include a verb that tells your reader what they will do when they click the hyperlink. Avoid embedding the link in an extra word like **here**.

{{% notice Examples%}}
Unclear:
- To learn about embedded voice assistants, read our white paper **here**.

Recommended:
- To learn about embedded voice assistants, read **The new voice of the embedded intelligent assistant**.
{{% /notice %}}

Sometimes, text should not be hyperlinked. For example, when you want the reader to see the URL. For these cases you can print the link and use a hyperlink. 

**Example:** To view your content open [http://localhost:1313](http://localhost:1313)

&nbsp;  
&nbsp;  

## Use second person point of view

Use second person to refer to your reader, and when writing user-oriented instructions. Second person uses, or implies, the pronoun you, and addresses your reader directly. 

Using second person helps your reader to engage, and helps to avoid the use of passive voice, because your reader is the subject of the sentence. 

If you have trouble starting a sentence, try starting with: **You can**

{{% notice Examples%}}
Too passive:
- An architecture can be thought of like a contract between the hardware and the software. 

Recommended:
- You can think of the architecture like a contract between the hardware and the software.  
- Think of an architecture like a contract between the hardware and the software.  
{{% /notice %}}

When writing user-oriented instructions or guidance, using you makes it clear that your reader, and not the item in discussion, is the agent who performs the action. In the following recommended example, it is clear that your reader is the agent using the flag to do the tracking, and that the flag is not doing the tracking automatically. 

{{% notice Examples%}}
Too passive:
- Use of the Access Flag (AF bit) tracks whether a region covered by the translation table entry has been accessed. 

Recommended:
- You can use the Access Flag (AF bit) to track whether a region covered by the translation table entry has been accessed. 
{{% /notice %}}

&nbsp;  
&nbsp;  


## Give only required details

Use short, crisp sentences. Avoid storytelling and excessive background. 


{{% notice Examples%}}
Too verbose:
- Due to the fact that we leveraged the CMSIS software library, issues with starting from scratch were avoided, and where you totally lacked the ability to implement optimized software before, you can now do so easily.

Recommended:
- The CMSIS library enables optimized software.
{{% /notice %}}

&nbsp;  
&nbsp;  

## Be specific

Use numbers and provide examples when possible. Avoid general statements try to be as specific.

{{% notice Examples%}}
Too nebulous:
- Using the library on almost always works.

Recommended:
- The library works on Linux and Windows 11.
{{% /notice %}}

&nbsp;
&nbsp;

## Be consistent

Be consistent because we like finding patterns and repetition. We understand content quicker if it is consistent. 
Make sure that you use the same words to describe the same things. For example, “This table/figure/example shows …” not depicts, lists, illustrates, defines. Use the same spelling, not “keywords” in one place and “key words” in another.


## Expected skills of your target audience

Learning Paths are intended for software developers with differing experience levels (Introductory and advanced). The intended audience is expected to have some domain specific knowledge, examples of which are listed below:

| Software Development Areas                 | Skills |
|-------------------------------------       |----------|
| Embedded and Microcontroller               | Understanding of programming languages such as C, C++ and assembly.  Basic awareness of Linux OS, RTOSes.  Fundamental knowledge of hardware and software architecture (not necessarily Arm) |
| Server and Cloud                           | <ul><li> Understanding of web services and Linux.</li><li> Basic awareness of containerization and orchestration technologies such as Docker and Kubernetes.</li><li> Proficient in programming languages such as Python and Java.</li></ul> | 
| Mobile				     | <ul> <li> Experience with software development on mobile platforms such as Android. </li> <li> Experience with mobile development and testing frameworks. </li> </ul> |
| Desktop and Laptop                         | <ul> <li> Experience with operating systems such as Windows and macOS. </li> <li> Experience with common development frameworks such as .NET and Electron. </li> Proficient in programming languages such as C++, Java and Python. </li> </ul> |
 




