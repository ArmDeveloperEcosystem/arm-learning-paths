---
title: Understand the runner scripts
description: Review how the shared terminal and browser interfaces call the supplied ONNX Runtime GenAI adapter.
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

{{% notice Note %}}
This page explains the supplied ONNX Runtime GenAI adapter. If you generated another adapter during setup, the shared contract, downloader, terminal application, browser application, and validator remain the same, but the runtime-specific loading, prompt handling, and generation code in `model_adapter.py` differs.
{{% /notice %}}

- [`adapter_contract.py`](/learning-paths/servers-and-cloud-computing/ai-portal-cloud-text-to-text/files/adapter_contract.py) defines the interface used by the terminal and browser applications.
- [`model_adapter.py`](/learning-paths/servers-and-cloud-computing/ai-portal-cloud-text-to-text/files/model_adapter.py) provides the ONNX Runtime GenAI implementation used in this Learning Path.
- [`run_model.py`](/learning-paths/servers-and-cloud-computing/ai-portal-cloud-text-to-text/files/run_model.py) provides the terminal interface and reports generation timing.
- [`genai_web.py`](/learning-paths/servers-and-cloud-computing/ai-portal-cloud-text-to-text/files/genai_web.py) provides the optional browser interface.
- [`download_model.py`](/learning-paths/servers-and-cloud-computing/ai-portal-cloud-text-to-text/files/download_model.py) downloads a complete model package without assuming its runtime format.
- [`validate_adapter.py`](/learning-paths/servers-and-cloud-computing/ai-portal-cloud-text-to-text/files/validate_adapter.py) checks the adapter contract and required package files.

## Resolve the model directory

The `adapter_contract.py` file maps each Hugging Face repository ID to a predictable local directory. Replacing `/` with `__` keeps the organization and repository name while producing one directory name:

```python
def model_directory(model_id: str) -> Path:
    return Path("models") / model_id.replace("/", "__")
```

The `download_model.py`, `run_model.py`, `genai_web.py`, and `validate_adapter.py` scripts use this same mapping. The downloader retrieves the complete repository; the ONNX adapter decides which files it needs.

## Understand the adapter contract

The `adapter_contract.py` file defines the operations used by the terminal and browser applications:

```python
class TextGenerationAdapter(ABC):
    @property
    @abstractmethod
    def interaction_mode(self) -> str:
        ...

    @abstractmethod
    def validate_model_directory(self) -> None:
        ...

    @abstractmethod
    def load(self) -> None:
        ...

    @abstractmethod
    def stream(
        self,
        prompt: str,
        max_new_tokens: int,
        enable_thinking: bool,
    ) -> Iterator[GenerationChunk]:
        ...
```

The adapter reports `chat` or `completion` to the surrounding application. Runtime-specific prompt names and model objects remain inside the adapter.

## Validate an ONNX Runtime GenAI package

The supplied `model_adapter.py` file checks for the files needed by ONNX Runtime GenAI:

```python
required_files = [
    "genai_config.json",
    "model.onnx",
    "tokenizer.json",
    "tokenizer_config.json",
]
```

`model.onnx` contains the model graph. Some models also use an external `model.onnx.data` weights file referenced by the graph. `genai_config.json` describes how ONNX Runtime GenAI should load and generate with the model.

The `validate_adapter.py` script constructs the active adapter and calls `validate_model_directory()`. This keeps package validation beside the runtime implementation rather than hard-coding ONNX filenames in the downloader.

## Detect base and instruction-tuned models

The `model_adapter.py` file detects three prompt-format cases:

```python
if (self.model_dir / "chat_template.jinja").is_file():
    return "chat", model_type
if (
    model_type == "qwen2"
    and self._token_text(tokenizer_config.get("eos_token")) == "<|im_end|>"
):
    return "qwen25", model_type
return "raw", model_type
```

The cases are:

- `chat` uses the `chat_template.jinja` included with an instruction-tuned model.
- `qwen25` supplies the equivalent Qwen2.5 ChatML template because that model bundle does not include a separate template file.
- `raw` sends unfinished text to a base model without wrapping it as a conversation.

This logic belongs in the adapter because base and instruction-tuned models require different tokenizer files and prompt handling. The terminal and browser applications only need to know whether they should present chat or text completion.

## Load ONNX Runtime GenAI

The `model_adapter.py` file imports ONNX Runtime GenAI and Transformers inside `load()`, after the model package has been validated.

The adapter creates a fast tokenizer from the downloaded `tokenizer.json` and reads the model's special tokens from `tokenizer_config.json`. It then configures the ONNX Runtime CPU provider and thread count:

```python
config = og.Config(str(self.model_dir))
config.clear_providers()
config.append_provider("CPU")
config.overlay(json.dumps({
    "model": {
        "decoder": {
            "session_options": {
                "intra_op_num_threads": self.threads,
            },
        },
    },
}))
```

Transformers performs tokenization and chat-template rendering only. ONNX Runtime GenAI loads the model and performs inference.

### ONNX Runtime uses KleidiAI kernels

[KleidiAI](https://github.com/ARM-software/kleidiai) is an open-source library of optimized microkernels for AI workloads on Arm CPUs. A microkernel implements a performance-critical part of an operator, such as quantized matrix multiplication, using Arm CPU features including DotProd, I8MM, SVE, and SME.

KleidiAI does not load the model or manage token generation. ONNX Runtime provides those functions and can use KleidiAI inside its CPU execution path for supported operators. The adapter does not need a separate KleidiAI API call: selecting the CPU provider allows ONNX Runtime to choose an applicable kernel from the installed runtime.

{{% notice Note %}}
KleidiAI dispatch depends on the installed runtime build, model operators, tensor shapes, quantization format, and CPU features. Do not assume that every model or Arm machine selects the same kernels.
{{% /notice %}}

## Format the prompt

The `model_adapter.py` file encodes base-model prompts directly. For instruction-tuned models, it applies the selected chat template:

```python
if self.prompt_style == "raw":
    return list(self.tokenizer.encode(prompt, add_special_tokens=True))

token_ids = self.tokenizer.apply_chat_template(
    [{"role": "user", "content": prompt}],
    tokenize=True,
    add_generation_prompt=True,
    **template_options,
)
```

`add_generation_prompt=True` adds the model-specific marker that indicates the assistant should begin responding. For Qwen3, the adapter also passes the `enable_thinking` option into its template.

## Stream generated text

The `model_adapter.py` file generates one token at a time and yields a `GenerationChunk` containing decoded text and its token count:

```python
yield GenerationChunk(
    text=token_stream.decode(token_id),
    token_count=1,
)
```

A new decoder stream is created for every generation request. This prevents decoding state from one terminal or web request from carrying into the next request.

## Terminal and browser applications

The `run_model.py` and `genai_web.py` files construct and load the same adapter:

```python
adapter = ModelAdapter(model_dir, args.prompt_style, args.threads)
adapter.validate_model_directory()
adapter.load()
```

Both applications consume the same stream:

```python
for chunk in adapter.stream(
    prompt,
    max_new_tokens,
    enable_thinking,
):
    generated_tokens += chunk.token_count
```

`run_model.py` writes each text fragment to the terminal. `genai_web.py` sends the fragments as newline-delimited JSON events. Both measure time to first token and decode throughput without importing ONNX Runtime GenAI directly.

## What you've learned

You have seen how the terminal and browser applications call the supplied adapter contract. The adapter validates an ONNX Runtime GenAI package, handles base and instruction-tuned prompts, configures CPU inference, allows supported operations to use KleidiAI, and streams decoded tokens.
