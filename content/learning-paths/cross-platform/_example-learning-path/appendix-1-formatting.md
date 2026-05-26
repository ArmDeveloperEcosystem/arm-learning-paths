---
# User change
title: "Format content"

weight: 7 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

Learning Paths are created using Markdown. You can use this section as a guide for how to format your content correctly.

To learn more about markdown formatting, you can also refer to other Markdown resources or view the source for [this page on GitHub](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/blob/main/content/learning-paths/cross-platform/_example-learning-path/appendix-1-formatting.md?plain=1).

## Learning Path formatting

Use the following quick links to jump to the appropriate section for each type of formatting. 

- [Markdown syntax](#markdown-syntax)
- [Code snippets](#code-snippets)
- [Images](#images)
- [Notice callout](#notice-callout)

## Markdown syntax

The most common Markdown syntax is in the following table.

| Element     | Syntax                   |
| ----------- | ----------- |
| Heading 1   | # Most Important Heading |
| Heading 2   | ## Second Level Heading  |
| Heading 3   | ### Third Level Heading  |
| **Bold text** | \*\*bold text\*\*   |
| *Italic text* | \*Italic text\*     |
| `Code font`   | \`code font\`       |

## Code snippets

You can add code snippets in the standard Markdown format. You can also add options to change how the code snippet is displayed.

Markdown source:

````markdown
```console
echo 'hello world'
```
````

The source is rendered as:

```console
echo 'hello world'
```

These are the available options for code snippets:
- Language highlighting
- Line numbers
- Line highlighting
- Command line view
- Code panes
- Output lines

### Language highlighting
Add the specific language name at the start of the code snippet.

Markdown source:

````markdown
```python
print('hello world')
```
````

The source is rendered as:

```python
print('hello world')
```

Markdown source:

````markdown
```c
int foo(void){
  return 0;
}
```
````

The source is rendered as:

```c
int foo(void){
  return 0;
}
```

### Line numbers

Specify that line_numbers are true in the following way.

Markdown source:

````markdown
```bash { line_numbers = "true" }
echo 'hello world'
echo 'I am line two'
```
````

The source is rendered as:

```bash { line_numbers = "true" }
echo 'hello world'
echo 'I am line two'
```

In some cases, the line numbering should not start from one but from another
value, for example if the code excerpt is extracted from a larger file. Use the
`line_start` attribute to achieve this.

Markdown source:

````markdown
```bash { line_numbers = "true" line_start = "10" }
echo 'hello world'
echo 'I am line eleven'
```
````

The source is rendered as:

```bash { line_numbers = "true" line_start = "10" }
echo 'hello world'
echo 'I am line eleven'
```

### Output lines

There are three ways you can specify command outputs in code:
- Standalone via marking the language as 'output'
- Alongside the 'command_line' functionality
- Alongside any other language via the 'output_lines' shortcode

{{% notice Note %}}
In each of the three situations, code marked as 'output' will:
- not be copied when clicking the 'copy' button
- not be highlighted by a cursor
- appear slightly darker
{{% /notice %}}

The following examples show the Markdown source and the rendered output for each approach.

#### Output - standalone block
Specify this case by making the language 'output'. An example in context.

Markdown source for a command:

````markdown
```bash
echo 'hello world'
echo 'test'
```
````

The source is rendered as:

```bash
echo 'hello world'
echo 'test'
```

Markdown source for output:

````markdown
```output
hello world
test
```
````

The source is rendered as:
```output
hello world
test
```

#### Output - alongside "command_line" functionality

Use the following syntax by specifying the output lines after a pipe as follows: { command_line="root@localhost | 2-6" }

Markdown source:

````markdown
```bash { command_line="root@localhost | 2-6" }
printf 'HelloWorld\n%.0s' {1..5}
HelloWorld
HelloWorld
HelloWorld
HelloWorld
HelloWorld
```
````

The source is rendered as:

```bash { command_line="root@localhost | 2-6" }
printf 'HelloWorld\n%.0s' {1..5}
HelloWorld
HelloWorld
HelloWorld
HelloWorld
HelloWorld
```

#### Output - alongside any language

To place output in the same code block as the generating command, use the shortcode `{ output_lines = "2-3, 5, 7-11" }` styling. Note that when hitting the `copy` button, only the commands are copied to the clipboard, not the specified output.

Markdown source:

````markdown
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
````

The source is rendered as:

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

Add user context to a command.

Markdown source:

````markdown
```bash { command_line="root@localhost" }
echo 'hello world'
```
````

The source is rendered as:

```bash { command_line="root@localhost" }
echo 'hello world'
```

Add user context to a command output.

Markdown source:

````markdown
```bash { command_line="root@localhost | 2-6" }
printf 'HelloWorld\n%.0s' {1..5}
HelloWorld
HelloWorld
HelloWorld
HelloWorld
HelloWorld
```
````

The source is rendered as:

```bash { command_line="root@localhost | 2-6" }
printf 'HelloWorld\n%.0s' {1..5}
HelloWorld
HelloWorld
HelloWorld
HelloWorld
HelloWorld
```


### Code panes  

Add a code pane for code dependent on OS or architecture. Code panes are incompatible with the other forms of code styling.

The following is a code pane example with a language selector.

Markdown source:

```markdown
{{</* tabpane code=true */>}}
  {{</* tab header="Python" language="python" output_lines="2" */>}}
print('hello world')
hello world
  {{</* /tab */>}}
  {{</* tab header="Bash" language="bash" */>}}
echo 'hello world'
  {{</* /tab */>}}
{{</* /tabpane */>}}
```

The source is rendered as:

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

Markdown source:

```markdown
{{</* tabpane code=true */>}}
  {{</* tab header="Python" language="python" output_lines="2-4,6" */>}}
print('hello world')*3
hello world
hello world
hello world
print('another example')
another example
  {{</* /tab */>}}
  {{</* tab header="Bash" language="bash" command_line="root@localhost | 2" */>}}
echo 'hello world'
hello world
  {{</* /tab */>}}
{{</* /tabpane */>}}
```

The source is rendered as:

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

Markdown source:

```markdown
{{</* tabpane code=true */>}}
  {{</* tab header="Ubuntu 22.04" line_numbers="true" */>}}
sudo apt-get install jq minicom make cmake gdb-multiarch automake autoconf libtool libftdi-dev libusb-1.0-0-dev pkg-config clang-format -y
  {{</* /tab */>}}
  {{</* tab header="Ubuntu 20.04" line_numbers="true" */>}}
sudo apt-get install jq minicom make cmake gdb-multiarch automake autoconf libtool libftdi-dev libusb-1.0-0-dev pkg-config clang-format -y
sudo snap install cmake --classic
  {{</* /tab */>}}
  {{</* tab header="Raspberry Pi OS" */>}}
Nothing more to install!
  {{</* /tab */>}}
{{</* /tabpane */>}}
```

The source is rendered as:

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

The Markdown used to add the picture is:

```console
![example image alt-text#center](arm-pic.png "Figure 1. Example image caption")
```

These are the options when adding an image:
- Hosting
    - Local
    - External
- Alignment
    - Left-aligned (default)
    - Center-aligned

### Image hosting (internal or external)

Internal hosting is straightforward. Add the picture (.png or .jpeg format) into the Learning Path directory alongside the *.md files, and refer to it by name. This example is using 'arm-pic.png' which you can find in this directory:

![Arm sample pic](arm-pic.png "Figure 2. Local hosting example")

External image referencing is also simple. Obtain the picture link and place that as the source. Example:

![Arm sample pic](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSuMSonKjWrTHvrR00sIUfPtOAxJ-RjUKmWUqCai5hMWC6MiHq8ZsUYBDWYDQ1WsjTb2e4&usqp=CAU "Figure 4. External hosting example")

### Image alignment (left or center) 

Left-alignment is the default image behavior. 
To center an image, add '#center' at the end of the alt-text and the image + subtitle will render in the center of the page.

Center aligned:
![alt-text #center](arm-pic.png "Figure 5. Centered example")

### Image sizing

Images are displayed in their specified size. To resize an image:
1. Download the image
2. Modify the size
3. Host the image locally.

## Notice callout

Use the following syntax to add a highlighted note or tip.

Markdown source:

```markdown
{{%/* notice */%}}  
Note that you can use `markdown` formatting in these notices as *well*
- Bullets
- Also
- Work
{{%/* /notice */%}}  
```

The source renders as:

{{% notice  %}}Note that you can use `markdown` formatting in these notices as *well*.
- Bullets
- Also
- Work
{{% /notice %}}

The default title for a note is `Tip`. You can add a custom title for a note.

Markdown source:

```markdown
{{%/* notice Important Note */%}}  
You can also give a custom title as specified here.
{{%/* /notice */%}}  
```
The source renders as:

{{% notice Important Note %}}
You can also give a custom title as specified here.
{{% /notice %}}
