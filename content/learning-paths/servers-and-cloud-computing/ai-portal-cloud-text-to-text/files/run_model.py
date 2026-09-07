#!/usr/bin/env python3

import argparse
import time

from adapter_contract import resolve_model_directory
from model_adapter import ModelAdapter


def main() -> None:
    parser = argparse.ArgumentParser()
    model_source = parser.add_mutually_exclusive_group(required=True)
    model_source.add_argument(
        "--model-id", help="Downloaded Hugging Face model repository ID"
    )
    model_source.add_argument("--model-dir", help="Downloaded model directory")
    parser.add_argument("--prompt-style", default="auto")
    parser.add_argument("--prompt", required=True)
    parser.add_argument("--max-new-tokens", type=int, default=128)
    parser.add_argument("--threads", type=int, default=4)
    parser.add_argument(
        "--enable-thinking", action="store_true", help="Enable supported thinking mode"
    )
    args = parser.parse_args()

    model_dir = resolve_model_directory(args.model_id, args.model_dir)
    print(f"Loading model from {model_dir.resolve()}")
    adapter = ModelAdapter(model_dir, args.prompt_style, args.threads)
    adapter.validate_model_directory()
    adapter.load()
    print(f"Runtime: {adapter.runtime_name}")
    print(f"Prompt style: {adapter.prompt_style}")
    print("\nOutput:\n", end="", flush=True)

    start = time.perf_counter()
    first_token_time = None
    generated_tokens = 0
    for chunk in adapter.stream(
        args.prompt,
        args.max_new_tokens,
        args.enable_thinking,
    ):
        if first_token_time is None and chunk.token_count > 0:
            first_token_time = time.perf_counter()
        generated_tokens += chunk.token_count
        print(chunk.text, end="", flush=True)

    finish = time.perf_counter()
    print("\n")
    print(f"Generated tokens: {generated_tokens}")
    if first_token_time is not None:
        print(f"Time to first token: {first_token_time - start:.2f} seconds")
        decode_time = finish - first_token_time
        decoded_tokens = max(generated_tokens - 1, 0)
        if decode_time > 0 and decoded_tokens > 0:
            print(
                f"Decode throughput: {decoded_tokens / decode_time:.2f} tokens/second"
            )


if __name__ == "__main__":
    main()
