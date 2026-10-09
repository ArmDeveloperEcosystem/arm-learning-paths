#!/usr/bin/env python3

import argparse
import json
import time
from threading import Lock

import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, StreamingResponse
from pydantic import BaseModel

from adapter_contract import resolve_model_directory
from model_adapter import ModelAdapter


HTML_PAGE = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>__PAGE_TITLE__</title>
  <style>
    :root {
      color-scheme: light;
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      color: #172033;
      background: #f3f6f9;
    }
    * { box-sizing: border-box; }
    body { margin: 0; min-height: 100vh; background: linear-gradient(180deg, #f8fafc 0%, #eef3f7 100%); }
    main { width: min(960px, calc(100% - 2rem)); margin: 0 auto; padding: 2.5rem 0; }
    header { display: flex; align-items: center; justify-content: space-between; gap: 1rem; margin-bottom: 1.25rem; }
    h1 { margin: 0; font-size: clamp(1.8rem, 4vw, 2.5rem); line-height: 1.1; letter-spacing: -0.035em; }
    .subtitle { margin: 0.4rem 0 0; color: #596579; font-size: 1rem; }
    .status { display: inline-flex; align-items: center; gap: 0.5rem; min-width: 7rem; justify-content: center; padding: 0.55rem 1rem; border: 1px solid #a9dfc0; border-radius: 999px; color: #17643a; background: #eaf8f0; font-weight: 700; }
    .status::before { width: 0.55rem; height: 0.55rem; border-radius: 50%; background: currentColor; content: ""; }
    .status[data-state="working"] { border-color: #c4b5fd; color: #5b21b6; background: #f3efff; }
    .status[data-state="error"] { border-color: #f3b4b4; color: #a61b1b; background: #fff0f0; }
    .panel { padding: clamp(1.25rem, 3vw, 2rem); border: 1px solid #d6dee8; border-radius: 0.8rem; background: #fff; box-shadow: 0 1rem 2.5rem rgb(43 57 78 / 10%); }
    label { display: block; margin-bottom: 0.55rem; color: #465267; font-weight: 700; }
    textarea { width: 100%; min-height: 9rem; resize: vertical; padding: 1rem; border: 1px solid #c9d3df; border-radius: 0.5rem; color: inherit; background: #fff; font: inherit; line-height: 1.5; }
    textarea:focus { border-color: #246bfd; outline: 3px solid rgb(36 107 253 / 15%); }
    .actions { display: flex; align-items: center; justify-content: space-between; gap: 1rem; margin: 1rem 0; }
    button { min-width: 5.5rem; padding: 0.7rem 1.2rem; border: 0; border-radius: 0.45rem; color: #fff; background: #246bfd; font: inherit; font-weight: 750; cursor: pointer; }
    button:hover { background: #1858d5; }
    button:focus-visible { outline: 3px solid rgb(36 107 253 / 30%); outline-offset: 2px; }
    button:disabled { cursor: progress; opacity: 0.65; }
    .metrics { margin: 0; color: #596579; font-variant-numeric: tabular-nums; text-align: right; }
    .response-label { margin: 0 0 0.55rem; color: #465267; font-size: 1rem; font-weight: 700; }
    pre { min-height: 10rem; margin: 0; padding: 1rem; overflow-wrap: anywhere; border: 1px solid #d6dee8; border-radius: 0.5rem; color: #172033; background: #f8fafc; font: inherit; line-height: 1.55; white-space: pre-wrap; }
    pre:empty::before { color: #8792a5; content: attr(data-placeholder); }
    @media (max-width: 640px) {
      main { padding: 1.25rem 0; }
      header, .actions { align-items: flex-start; flex-direction: column; }
      .status { min-width: 0; }
      .metrics { text-align: left; }
    }
  </style>
</head>
<body>
  <main>
    <header>
      <div>
        <h1>__PAGE_TITLE__</h1>
        <p class="subtitle">__PAGE_SUBTITLE__</p>
      </div>
      <div class="status" id="status" data-state="ready" role="status">Ready</div>
    </header>
    <section class="panel" aria-labelledby="prompt-label">
      <label id="prompt-label" for="prompt">__INPUT_LABEL__</label>
      <textarea id="prompt">__DEFAULT_INPUT__</textarea>
      <div class="actions">
        <button id="send" type="button" data-idle-label="__BUTTON_LABEL__">__BUTTON_LABEL__</button>
        <p class="metrics" id="metrics" aria-live="polite">__READY_TEXT__</p>
      </div>
      <p class="response-label">__OUTPUT_LABEL__</p>
      <pre id="response" data-placeholder="__OUTPUT_PLACEHOLDER__"></pre>
    </section>
  </main>
  <script>
    const button = document.querySelector('#send');
    const prompt = document.querySelector('#prompt');
    const response = document.querySelector('#response');
    const status = document.querySelector('#status');
    const metrics = document.querySelector('#metrics');

    function setStatus(text, state) {
      status.textContent = text;
      status.dataset.state = state;
    }

    button.addEventListener('click', async () => {
      if (!prompt.value.trim()) {
        setStatus('__REQUIRED_MESSAGE__', 'error');
        prompt.focus();
        return;
      }

      button.disabled = true;
      button.textContent = 'Generating…';
      response.textContent = '';
      metrics.textContent = 'Waiting for the first token…';
      setStatus('Generating', 'working');
      try {
        const result = await fetch('/generate', {
          method: 'POST',
          headers: {'Content-Type': 'application/json'},
          body: JSON.stringify({prompt: prompt.value}),
        });
        if (!result.ok) throw new Error(await result.text());
        const reader = result.body.getReader();
        const decoder = new TextDecoder();
        let buffer = '';
        while (true) {
          const {value, done} = await reader.read();
          if (done) break;
          buffer += decoder.decode(value, {stream: true});
          const lines = buffer.split('\\n');
          buffer = lines.pop();
          for (const line of lines) {
            if (!line) continue;
            const event = JSON.parse(line);
            if (event.type === 'token') response.textContent += event.text;
            if (event.type === 'metrics') {
              metrics.textContent = `${event.tokens} tokens · ${event.tokens_per_second.toFixed(2)} tokens/s · ${event.time_to_first_token.toFixed(2)}s TTFT`;
            }
          }
        }
        setStatus('Ready', 'ready');
      } catch (error) {
        response.textContent = `Request failed: ${error.message}`;
        metrics.textContent = 'Generation failed';
        setStatus('Error', 'error');
      } finally {
        button.disabled = false;
        button.textContent = button.dataset.idleLabel;
      }
    });
  </script>
</body>
</html>
"""


class GenerationRequest(BaseModel):
    prompt: str


def render_page(interaction_mode: str, runtime_name: str) -> str:
    if interaction_mode == "completion":
        values = {
            "__PAGE_TITLE__": f"{runtime_name} Text Completion",
            "__PAGE_SUBTITLE__": "Base-model text continuation on an Arm64 CPU",
            "__INPUT_LABEL__": "Text to continue",
            "__DEFAULT_INPUT__": "Title: Why Arm64 is reshaping cloud infrastructure\n\nArm64 is becoming a preferred architecture for modern cloud workloads because",
            "__BUTTON_LABEL__": "Continue",
            "__READY_TEXT__": "Ready to continue text",
            "__OUTPUT_LABEL__": "Continuation",
            "__OUTPUT_PLACEHOLDER__": "The generated continuation will appear here.",
            "__REQUIRED_MESSAGE__": "Enter text to continue",
        }
    else:
        values = {
            "__PAGE_TITLE__": f"{runtime_name} Chatbot",
            "__PAGE_SUBTITLE__": "Instruction-tuned inference on an Arm64 CPU",
            "__INPUT_LABEL__": "Prompt",
            "__DEFAULT_INPUT__": "Write a concise technical briefing for a cloud architect explaining why Arm64 CPUs are well suited to AI inference. Cover performance per watt, deployment scale, and software portability.",
            "__BUTTON_LABEL__": "Send",
            "__READY_TEXT__": "Ready for a prompt",
            "__OUTPUT_LABEL__": "Response",
            "__OUTPUT_PLACEHOLDER__": "The generated response will appear here.",
            "__REQUIRED_MESSAGE__": "Enter a prompt",
        }

    page = HTML_PAGE
    for marker, value in values.items():
        page = page.replace(marker, value)
    return page


def create_app(adapter, max_new_tokens: int, enable_thinking: bool) -> FastAPI:
    app = FastAPI()
    generation_lock = Lock()
    page = render_page(adapter.interaction_mode, adapter.runtime_name)

    @app.get("/", response_class=HTMLResponse)
    def index() -> str:
        return page

    @app.post("/generate")
    def generate(request: GenerationRequest) -> StreamingResponse:
        def response_stream():
            with generation_lock:
                start = time.perf_counter()
                first_token_time = None
                generated_tokens = 0

                for chunk in adapter.stream(
                    request.prompt,
                    max_new_tokens,
                    enable_thinking,
                ):
                    if first_token_time is None and chunk.token_count > 0:
                        first_token_time = time.perf_counter()
                    generated_tokens += chunk.token_count
                    yield json.dumps({
                        "type": "token",
                        "text": chunk.text,
                    }) + "\n"

                finish = time.perf_counter()
                decode_time = finish - first_token_time if first_token_time is not None else 0
                decoded_tokens = max(generated_tokens - 1, 0)
                yield json.dumps({
                    "type": "metrics",
                    "tokens": generated_tokens,
                    "time_to_first_token": first_token_time - start if first_token_time is not None else 0,
                    "tokens_per_second": decoded_tokens / decode_time if decode_time > 0 else 0,
                }) + "\n"

        return StreamingResponse(response_stream(), media_type="application/x-ndjson")

    return app


def main() -> None:
    parser = argparse.ArgumentParser()
    model_source = parser.add_mutually_exclusive_group(required=True)
    model_source.add_argument("--model-id", help="Downloaded Hugging Face model repository ID")
    model_source.add_argument("--model-dir", help="Downloaded model directory")
    parser.add_argument("--prompt-style", default="auto")
    parser.add_argument("--max-new-tokens", type=int, default=256)
    parser.add_argument("--threads", type=int, default=4)
    parser.add_argument("--enable-thinking", action="store_true", help="Enable Qwen3 thinking mode")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()

    model_dir = resolve_model_directory(args.model_id, args.model_dir)
    adapter = ModelAdapter(model_dir, args.prompt_style, args.threads)
    adapter.validate_model_directory()
    adapter.load()

    app = create_app(adapter, args.max_new_tokens, args.enable_thinking)
    uvicorn.run(app, host=args.host, port=args.port)


if __name__ == "__main__":
    main()
