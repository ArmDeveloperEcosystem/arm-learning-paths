#!/usr/bin/env python3

from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path
from typing import Iterator


@dataclass(frozen=True)
class GenerationChunk:
    text: str
    token_count: int


class TextGenerationAdapter(ABC):
    def __init__(self, model_dir: Path, prompt_style: str, threads: int) -> None:
        self.model_dir = model_dir
        self.requested_prompt_style = prompt_style
        self.threads = threads

    @property
    @abstractmethod
    def runtime_name(self) -> str:
        pass

    @property
    @abstractmethod
    def interaction_mode(self) -> str:
        """Return chat or completion for the surrounding user interface."""

    @property
    @abstractmethod
    def prompt_style(self) -> str:
        pass

    @abstractmethod
    def validate_model_directory(self) -> None:
        pass

    @abstractmethod
    def load(self) -> None:
        pass

    @abstractmethod
    def stream(
        self,
        prompt: str,
        max_new_tokens: int,
        enable_thinking: bool,
    ) -> Iterator[GenerationChunk]:
        pass


def model_directory(model_id: str) -> Path:
    return Path("models") / model_id.replace("/", "__")


def resolve_model_directory(model_id: str | None, model_dir: str | None) -> Path:
    if bool(model_id) == bool(model_dir):
        raise ValueError("Provide exactly one of --model-id or --model-dir.")
    return model_directory(model_id) if model_id else Path(model_dir)
