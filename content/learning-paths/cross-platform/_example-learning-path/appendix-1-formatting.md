---
# User change
title: "Appendix: Format content"

weight: 7 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

Refer to this section when you are have questions on how to format your content correctly.

## Learning Path Formatting

Use the quick links below to jump to the appropriate section for each type of formatting. 

- [Markdown Syntax](#markdown-syntax)
- [Code Snippets](#code-snippets)
- [Images](#images)
- [Videos](#videos)
- [Notice Callout](#notice-callout)
- [Godbolt Compiler Explorer](#godbolt-compiler-explorer)


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
- Output lines

### Language highlighting
Add the specific language name at the start of the code snippet:

\`\`\`python \
print(hello world) \
\`\`\`
```python
print(hello world)
```

\`\`\`C \
int foo(void){ \
  return 0; \
} \
\`\`\`
```C
int foo(void){
  return 0;
}
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



### Output Lines

There are three ways you can specify command outputs in code:
1.    Standalone via marking the language as 'output'
2.    Alongside the 'command_line' functionality 
3.    Alongside any other language via the 'output_lines' shortcode

{{% notice Note %}}
In each of the three situations, code marked as 'output' will:
- Not be copied when clicking the 'copy' button
- Not be highlightable by a cursor
- Appear slightly darker
{{% /notice %}}

Keep reading to see an example of each.

#### Output - standalone block
Specify this case by making the language 'output'. An example in context:

```bash
echo 'hello world'
echo 'test'
```
The output from the above command is:
```output
hello world
test
```

#### Output - alongside "command_line" functionality
Use the following syntax by specifying the output lines after a pipe like so: { command_line="root@localhost | 2-6" }

Example in context:
```bash { command_line="root@localhost | 2-6" }
printf 'HelloWorld\n%.0s' {1..5}
HelloWorld
HelloWorld
HelloWorld
HelloWorld
HelloWorld
```

#### Output - alongside any language
To place output in the same code block as the generating command, use the shortcode `{ output_lines = "2-3, 5, 7-11" }` styling. Note that when hitting the `copy` button, only the commands are copied to the clipboard, not the specified output. Example:

```bash { output_lines = "2-3,5,7-11" }
echo 'hello world\nh'
hello world
h
echo 'one line output'
one line output
printf 'outputline\n%.0s' {1..5}
outputline
outputline
outputline
outputline
outputline
```




### Command line view
Add command line user context:

```bash { command_line="root@localhost" }
echo ‘hello world’
```

With output:

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
  {{< tab header="Python" language="python" output_lines="2">}}
print('hello world')
hello world
  {{< /tab >}}
  {{< tab header="Bash" language="bash">}}
echo 'hello world'
  {{< /tab >}}
{{< /tabpane >}}

&nbsp;  

{{< tabpane code=true >}}
  {{< tab header="Python" language="python" output_lines="2-4,6">}}
print('hello world')*3
hello world
hello world
hello world
print('another example')
another example
  {{< /tab >}}
  {{< tab header="Bash" language="bash" command_line="root@localhost | 2">}}
echo 'hello world'
hello world
  {{< /tab >}}
{{< /tabpane >}}

&nbsp;  


{{< tabpane code=true >}}
  {{< tab header="Ubuntu 22.04"  line_numbers="true">}}
sudo apt-get install jq minicom make cmake gdb-multiarch automake autoconf libtool libftdi-dev libusb-1.0-0-dev pkg-config clang-format -y
  {{< /tab >}}
  {{< tab header="Ubuntu 20.04"  line_numbers="true">}}
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

