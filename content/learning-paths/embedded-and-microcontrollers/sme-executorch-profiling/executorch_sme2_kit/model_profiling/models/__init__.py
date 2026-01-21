"""Local model registry used for ExecuTorch exports."""

from __future__ import annotations

import sys
import types
from dataclasses import dataclass
from typing import Dict, Iterable, Optional, Type

from .model_base import EagerModelBase


@dataclass
class ModelRegistration:
    model_class: Type[EagerModelBase]
    xnnpack_quantization: Optional[str] = None
    xnnpack_delegation: bool = True


MODEL_REGISTRY: Dict[str, ModelRegistration] = {}


def register_model(
    name: str,
    model_class: Type[EagerModelBase],
    *,
    xnnpack_quantization: Optional[str] = None,
    xnnpack_delegation: bool = True,
) -> None:
    """Register a model for export and optional XNNPACK metadata."""

    if name in MODEL_REGISTRY:
        raise ValueError(f"Model '{name}' is already registered")
    MODEL_REGISTRY[name] = ModelRegistration(
        model_class=model_class,
        xnnpack_quantization=xnnpack_quantization,
        xnnpack_delegation=xnnpack_delegation,
    )


def available_models() -> Iterable[str]:
    return MODEL_REGISTRY.keys()


def patch_executorch_model_registry() -> None:
    """Inject our models into ExecuTorch's registry at runtime."""

    # Import lazily so we only touch ExecuTorch when needed.
    from executorch.examples import models as et_models
    from executorch.examples.xnnpack import MODEL_NAME_TO_OPTIONS, QuantType, XNNPACKOptions

    for name, registration in MODEL_REGISTRY.items():
        module_name = f"_model_profiling_{name}"
        full_module_name = f"executorch.examples.models.{module_name}"
        if full_module_name not in sys.modules:
            module = types.ModuleType(full_module_name)
            module.__dict__[registration.model_class.__name__] = registration.model_class
            module.__all__ = [registration.model_class.__name__]
            sys.modules[full_module_name] = module
            sys.modules[f"examples.models.{module_name}"] = module

        et_models.MODEL_NAME_TO_MODEL[name] = (module_name, registration.model_class.__name__)

        if registration.xnnpack_quantization:
            quant = QuantType[registration.xnnpack_quantization]
            MODEL_NAME_TO_OPTIONS[name] = XNNPACKOptions(
                quantization=quant,
                delegation=registration.xnnpack_delegation,
            )
        elif name not in MODEL_NAME_TO_OPTIONS:
            # Default to "no quant" but still allow delegation.
            MODEL_NAME_TO_OPTIONS[name] = XNNPACKOptions(
                quantization=QuantType.NONE,
                delegation=registration.xnnpack_delegation,
            )


# Import submodules so they self-register.
from . import toy_cnn  # noqa: E402,F401

# EdgeTAM is optional - only imported if user has onboarded it via agent skill 08
try:
    from . import edgetam  # noqa: E402,F401
except ImportError:
    pass  # EdgeTAM not onboarded yet
