# Call search through the Chrome DevTools CLI

The CLI bridges an agent to the page's native WebMCP tool:

```text
Agent → Chrome DevTools CLI → Chrome → search_arm_content → browser search worker
```

Requires Chrome, Node.js, and npm. No WebMCP Inspector extension or Gemini API key is needed.

## Start the browser

Start the site from the repository root:

```sh
hugo server --bind 127.0.0.1 --port 1313
```

In another terminal, define the CLI shortcut and launch an isolated browser. The first invocation may download the pinned npm package.

```sh
devtools() {
  npx --yes --package=chrome-devtools-mcp@1.12.0 chrome-devtools "$@"
}

devtools start --isolated --headless \
  --categoryExperimentalWebmcp \
  --chromeArg=--enable-features=WebMCP \
  --no-usage-statistics --no-performance-crux

devtools new_page http://localhost:1313/search/
```

## Discover and call the tool

Replace `PAGE_ID` with the ID returned by `new_page`:

```sh
devtools list_webmcp_tools PAGE_ID

devtools execute_webmcp_tool PAGE_ID search_arm_content \
  --input '{"query":"Jason Andrews","type":"learning-path","sort":"updated","limit":5}'
```

Discovery lists the tool and its input schema. Execution returns matching content with source URLs and metadata. The example searches author names and indexed text; it is not an exact author-only filter.

If discovery returns no tools, check the URL, allow the page to initialize, and confirm both experimental options were supplied to `devtools start`. These options apply to the isolated browser session and leave your everyday Chrome profile unchanged. Other agents need their own WebMCP bridge.

Stop the browser when finished:

```sh
devtools stop
```

References: [Chrome WebMCP automation and agents](https://developer.chrome.com/docs/devtools/application/webmcp#automation-and-agents), [Chrome DevTools CLI documentation](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/cli.md).
