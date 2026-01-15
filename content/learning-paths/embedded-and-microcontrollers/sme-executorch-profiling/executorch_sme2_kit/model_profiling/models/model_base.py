"""Common interface for ExecuTorch-compatible eager models."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Tuple


class EagerModelBase(ABC):
    """Subset of the ExecuTorch model interface we rely on for exports."""

    @abstractmethod
    def get_eager_model(self):
        """Return the instantiated eager PyTorch module ready for export."""

    @abstractmethod
    def get_example_inputs(self) -> Tuple[Any, ...]:
        """Return positional example inputs used for tracing/export."""

    def get_example_kwarg_inputs(self) -> dict:
        """Optional keyword inputs; override when the model needs them."""

        return {}

    def get_dynamic_shapes(self):
        """Optional dynamic shape info; override if needed."""

        return None
