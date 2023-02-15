---
# User change
title: "2c) Add formatted content"

weight: 7 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
<!-- ![alt-text #center](2-contribution-process.PNG "Contribution process") -->

Refer to this section when you are have questions how to format your content correctly.

## Learning Path Formatting

Use the quick links below to jump to the appropriate section for each type of formatting. 

1. [Markdown Syntax](#markdown-syntax)
2. [Code Snippets](#code-snippets)
3. [Images](#images)
4. [Videos](#videos)
5. [Notice Callout](#notice-callout)
6. [Godbolt Compiler Explorer](#godbolt-compiler-explorer)


## Markdown Syntax
This site leverages core Markdown syntax. This picture converes 90% of common syntax needs:

![example image alt-text#center](arm-pic.png "Figure 1. Example image caption")




## Code Snippets
You can add images in the standard markdown format. Provide alternative text (displayed if the image cannot load) in brackets followed by the image source and subtitle in parenthesis. Simple example:

You can add code snippets in the standard markdown format, plus additional capabilities. A simple example:
```
echo ‘hello world’
```

These are the range of options to add an image:
- Language highlighting
- Line numbers
- Line highlighting
- Command line view
- Code panes

### Language highlighting
Add the specific language name at the start of the code snippet:

\`\`\`python \
print(hello world) \
\`\`\`
```python
print(hello world)
```

### Line numbers
Specify that line_numbers are true in the following way:

\`\`\`bash { line_numbers = "true" } \
echo 'hello world' \
echo ‘I am line two’ \
\`\`\` 

```bash { line_numbers = "true" } 
echo ‘hello world’ 
echo ‘I am line two’ 
``` 

### Line highlighting
One or multiple lines can be highlighted in different code areas:

\`\`\`bash { highlight_lines = 5 } \
echo ‘hello world’ \
echo ‘I am line two’ \
\`\`\` \

```bash { highlight_lines = 1 }
echo ‘hello world’
echo ‘I am line two’ 
```

\`\`\`bash { highlight_lines = "1-2, 4" } \
echo ‘hello world’ \
echo ‘I am line two’ \
echo ‘I am line three’ \ 
echo ‘I am line four’ \
\`\`\` \

```bash { highlight_lines = "1-2, 4"  }
echo ‘hello world’
echo ‘I am line two’
echo ‘I am line three’ 
echo ‘I am line four’ 
```

### Command line view
Add command line user context:

```bash { command_line="root@localhost" }
echo ‘hello world’
```

With output (note if a reader presses 'copy' the output will be copied as well):

```bash { command_line="root@localhost | 2-6" }
printf 'HelloWorld\n%.0s' {1..5}
HelloWorld
HelloWorld
HelloWorld
HelloWorld
HelloWorld
```

### Code Panes  

Adding a code pane, for code dependent on OS, architecture, or similar. Code panes are incompatible with the other forms of code styling.

Code pane example with language selector:

{{< tabpane code=true >}}
  {{< tab header="Python" lang="python">}}
print('hello world')
  {{< /tab >}}
  {{< tab header="Bash" lang="bash">}}
echo 'hello world'
  {{< /tab >}}
{{< /tabpane >}}

&nbsp;  

Example with line highlighting

{{< tabpane code=true >}}
  {{< tab header="Python" lang="python" highlight="2-3">}}
print('hello world')
print('higlight me')
print('and also me')
  {{< /tab >}}
  {{< tab header="Bash" lang="bash" highlight="2,4">}}
echo 'hello world'
echo 'highlight me'
echo 'not me'
echo 'but me'
  {{< /tab >}}
{{< /tabpane >}}

&nbsp;  


{{< tabpane code=true >}}
  {{< tab header="Ubuntu 22.04" >}}
sudo apt-get install jq minicom make cmake gdb-multiarch automake autoconf libtool libftdi-dev libusb-1.0-0-dev pkg-config clang-format -y
  {{< /tab >}}
  {{< tab header="Ubuntu 20.04" >}}
sudo apt-get install jq minicom make gdb-multiarch automake autoconf libtool libftdi-dev libusb-1.0-0-dev pkg-config clang-format -y
sudo snap install cmake --classic
  {{< /tab >}}
  {{< tab header="Raspberry Pi OS" >}}
Nothing more to install!
  {{< /tab >}}
{{< /tabpane >}}


## Images

You can add images in the standard markdown format. Provide alternative text (displayed if the image cannot load) in brackets followed by the image source and subtitle in parenthesis. Simple example:

![example image alt-text#center](arm-pic.png "Figure 1. Example image caption")

These are the range of options to add an image:
- Hosting
    - Local
    - External
- Alignment
    - Left-aligned (default)
    - Center-aligned

### Image Hosting (internal or external)
Internal hosting is straightforward. Add the picture (.png or .jpeg format) into the Learning Path directory alongside the *.md files, and refer to it by name. This example is using 'arm-pic.png' which you can find in this directory:

![Arm sample pic](arm-pic.png "Figure 2. Local hosting example")

External image referencing is also simple. Obtain the picture link and place that as the source. Example:

![Arm sample pic](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSuMSonKjWrTHvrR00sIUfPtOAxJ-RjUKmWUqCai5hMWC6MiHq8ZsUYBDWYDQ1WsjTb2e4&usqp=CAU "Figure 4. External hosting example")

### Image Alignment (center or left) 

Left-alignment is the default image behavior. 
To center an image, add '#center' at the end of the alt-text and the image + subtitle will center on the page.

Center aligned:
![alt-text #center](arm-pic.png "Figure 5. Centered example")

### Image Sizing
Images are displayed in their specified size. To shrink an image, download the image, modify the size, and host the image locally.

## Videos

You can add videos through a Hugo shortcode format. Only the video id is required. A simple example:

![example image alt-text#center](arm-pic.png "Figure 1. Example image caption")

Videos can be hosted in two ways:
    - YouTube
    - Vimeo

### YouTube Hosting
Use the following format (note that the 'nocookie' wording prevents YouTube from adding tracking cookies into this site via an embedded video):

{{</* youtube-nocookie *video_id* */>}}     

{{< youtube-nocookie 146022717 >}}


### Vimeo Hosting
Use the following format:
{{< vimeo 146022717 >}}


## Notice Callout
Use this format to add a note / tip for a reader in a highlighted way. The format is:   

{{%/* notice *optional_title* */%}}  
Text inside  
{{%/* /notice */%}}  

Simple example:

{{% notice  %}}Note that you can use `markdown` formatting in these notices as *well*.{{% /notice %}}

You can add a custom title as well if you desire as so:

{{% notice Important Note %}}
You can also give a custom title as specified here.
- Bullets
- Also
- Work
{{% /notice %}}

## Godbolt Compiler Explorer

To be written

