# Structured component patterns

Use these patterns when adding or editing structured Markdown and Hugo components.

## Notices

Use notice shortcodes for information that needs visual emphasis.

```md
{{% notice Note %}}
The following commands use version 1.2.3. The same commands work with other versions.
{{% /notice %}}
```

Common labels include `Note`, `Tip`, `Warning`, `Important`, `Troubleshooting`, and short contextual labels such as `Network security`.

Rules:

- Keep opening and closing shortcodes on separate lines for multi-sentence content.
- Keep the label concise and descriptive.
- Don't use notices for ordinary transitions or filler.
- Don't nest notices inside lists unless the surrounding file already uses that pattern and indentation is correct.
- Preserve shortcode spacing: `{{% notice Note %}}` and `{{% /notice %}}`.

## Tables

Use Markdown tables for compact comparisons and lookup information.

```md
| Tool | Purpose | Verification command |
|------|---------|----------------------|
| `skopeo` | Inspect and copy container images | `skopeo --help` |
| `perf` | Collect Linux performance data | `perf --help` |
```

Rules:

- Use a header row and separator row.
- Keep headers short and descriptive.
- Keep each row parallel.
- Use code formatting for commands, file names, flags, package names, and variables.
- Avoid long prose in cells. If a cell needs multiple sentences, use a paragraph or list instead.
- Avoid tables for ordered procedures.

## Code tab panes

Use `tabpane code=true` for platform-specific commands or code alternatives.

```md
{{< tabpane code=true >}}
  {{< tab header="Ubuntu" language="bash">}}
sudo apt update
sudo apt install -y example
  {{< /tab >}}
  {{< tab header="macOS" language="bash">}}
brew install example
  {{< /tab >}}
{{< /tabpane >}}
```

Rules:

- Use clear tab labels such as `Ubuntu`, `Fedora`, `macOS`, or `Windows PowerShell`.
- Use `language` when the surrounding examples use it.
- Keep alternatives parallel.
- Use the code sample review skill for command accuracy, output, code panes, and code fence integrity.

## Non-code tab panes

Use `tabpane-normal` or `tabpane code=false` for non-code alternatives.

```md
{{< tabpane-normal >}}
  {{< tab header="Podman" >}}
Use Podman when you need a daemonless container runtime.
  {{< /tab >}}
  {{< tab header="Finch" >}}
Use Finch when you need a lightweight container runtime on macOS.
  {{< /tab >}}
{{< /tabpane-normal >}}
```

Rules:

- Use non-code tabs only when the alternatives are mutually exclusive.
- Keep each tab roughly comparable in length and detail.
- Avoid hiding critical sequential instructions inside tabs unless the user chooses one path.


