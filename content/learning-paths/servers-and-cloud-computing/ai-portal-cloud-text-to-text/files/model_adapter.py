#!/usr/bin/env python3

import json
import os
from pathlib import Path
from typing import Any, Iterator

from adapter_contract import GenerationChunk, TextGenerationAdapter


QWEN25_CHAT_TEMPLATE = """{% for message in messages %}{{ '<|im_start|>' + message['role'] + '\n' + message['content'] + '<|im_end|>\n' }}{% endfor %}{% if add_generation_prompt %}{{ '<|im_start|>assistant\n' }}{% endif %}"""


class ModelAdapter(TextGenerationAdapter):
    def __init__(self, model_dir: Path, prompt_style: str, threads: int) -> None:
        super().__init__(model_dir, prompt_style, threads)
        self.model: Any = None
        self.tokenizer: Any = None
        self.onnx_tokenizer: Any = None
        self.model_type = ""
        self.selected_prompt_style = ""

    @property
    def runtime_name(self) -> str:
        return "ONNX Runtime GenAI"

    @property
    def interaction_mode(self) -> str:
        return "completion" if self.prompt_style == "raw" else "chat"

    @property
    def prompt_style(self) -> str:
        if not self.selected_prompt_style:
            self.selected_prompt_style, self.model_type = self._select_prompt_style()
        return self.selected_prompt_style

    def validate_model_directory(self) -> None:
        required_files = [
            "genai_config.json",
            "model.onnx",
            "tokenizer.json",
            "tokenizer_config.json",
        ]
        missing_files = [
            name for name in required_files if not (self.model_dir / name).is_file()
        ]
        if missing_files:
            missing = ", ".join(missing_files)
            raise FileNotFoundError(
                f"The model directory is missing required files: {missing}"
            )
        self.selected_prompt_style, self.model_type = self._select_prompt_style()

    def load(self) -> None:
        self.validate_model_directory()
        os.environ.setdefault("TRANSFORMERS_VERBOSITY", "error")

        import onnxruntime_genai as og
        from transformers import PreTrainedTokenizerFast

        tokenizer_config = self._read_json(self.model_dir / "tokenizer_config.json")
        special_tokens = {}
        for name in ("bos_token", "eos_token", "pad_token", "unk_token"):
            value = self._token_text(tokenizer_config.get(name))
            if value is not None:
                special_tokens[name] = value

        self.tokenizer = PreTrainedTokenizerFast(
            tokenizer_file=str(self.model_dir / "tokenizer.json"),
            **special_tokens,
        )
        if self.prompt_style == "chat":
            template_path = self.model_dir / "chat_template.jinja"
            if not template_path.is_file():
                raise ValueError(
                    "The selected chat prompt style requires chat_template.jinja."
                )
            self.tokenizer.chat_template = template_path.read_text(encoding="utf-8")
        elif self.prompt_style == "qwen25":
            self.tokenizer.chat_template = QWEN25_CHAT_TEMPLATE

        config = og.Config(str(self.model_dir))
        config.clear_providers()
        config.append_provider("CPU")
        config.overlay(
            json.dumps(
                {
                    "model": {
                        "decoder": {
                            "session_options": {
                                "intra_op_num_threads": self.threads,
                            },
                        },
                    },
                }
            )
        )
        self.model = og.Model(config)
        self.onnx_tokenizer = og.Tokenizer(self.model)

    def stream(
        self,
        prompt: str,
        max_new_tokens: int,
        enable_thinking: bool,
    ) -> Iterator[GenerationChunk]:
        if self.model is None or self.tokenizer is None or self.onnx_tokenizer is None:
            raise RuntimeError("Call load() before generating text.")

        import onnxruntime_genai as og

        input_tokens = self._encode_prompt(prompt, enable_thinking)
        params = og.GeneratorParams(self.model)
        params.set_search_options(
            max_length=len(input_tokens) + max_new_tokens,
            do_sample=False,
        )
        generator = og.Generator(self.model, params)
        generator.append_tokens(input_tokens)
        token_stream = self.onnx_tokenizer.create_stream()
        generated_tokens = 0

        while not generator.is_done() and generated_tokens < max_new_tokens:
            generator.generate_next_token()
            token_id = int(generator.get_next_tokens()[0])
            generated_tokens += 1
            yield GenerationChunk(text=token_stream.decode(token_id), token_count=1)

    def _encode_prompt(self, prompt: str, enable_thinking: bool) -> list[int]:
        if self.prompt_style == "raw":
            return list(self.tokenizer.encode(prompt, add_special_tokens=True))

        template_options = {}
        if self.model_type == "qwen3":
            template_options["enable_thinking"] = enable_thinking

        token_ids = self.tokenizer.apply_chat_template(
            [{"role": "user", "content": prompt}],
            tokenize=True,
            add_generation_prompt=True,
            **template_options,
        )
        return list(token_ids)

    def _select_prompt_style(self) -> tuple[str, str]:
        detected_style, model_type = self._detect_prompt_style()
        selected_style = (
            detected_style
            if self.requested_prompt_style == "auto"
            else self.requested_prompt_style
        )
        if selected_style not in {"raw", "chat", "qwen25"}:
            raise ValueError(
                "The ONNX adapter supports prompt styles: auto, raw, chat, qwen25."
            )
        return selected_style, model_type

    def _detect_prompt_style(self) -> tuple[str, str]:
        genai_config = self._read_json(self.model_dir / "genai_config.json")
        tokenizer_config = self._read_json(self.model_dir / "tokenizer_config.json")
        model_type = str(genai_config.get("model", {}).get("type", ""))

        if (self.model_dir / "chat_template.jinja").is_file():
            return "chat", model_type
        if (
            model_type == "qwen2"
            and self._token_text(tokenizer_config.get("eos_token")) == "<|im_end|>"
        ):
            return "qwen25", model_type
        return "raw", model_type

    @staticmethod
    def _read_json(path: Path) -> dict[str, Any]:
        with path.open(encoding="utf-8") as file:
            return json.load(file)

    @staticmethod
    def _token_text(value: Any) -> Any:
        if isinstance(value, dict):
            return value.get("content")
        return value
