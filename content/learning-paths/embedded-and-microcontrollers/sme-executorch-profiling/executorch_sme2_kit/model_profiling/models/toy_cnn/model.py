"""Toy CNN model implementation."""

from __future__ import annotations

import torch
from typing import Tuple

from ..model_base import EagerModelBase


class ToyCNNModel(EagerModelBase):
    """A small CV-ish model with convs and a classifier head."""

    def __init__(self):
        super().__init__()
        self.model = torch.nn.Sequential(
            torch.nn.Conv2d(3, 32, kernel_size=3, stride=2, padding=1),
            torch.nn.ReLU(),
            torch.nn.Conv2d(32, 64, kernel_size=3, stride=2, padding=1),
            torch.nn.ReLU(),
            torch.nn.Conv2d(64, 128, kernel_size=3, stride=2, padding=1),
            torch.nn.ReLU(),
            torch.nn.AdaptiveAvgPool2d((1, 1)),
            torch.nn.Flatten(),
            torch.nn.Linear(128, 1000),
        )

    def get_eager_model(self):
        return self.model.eval()

    def get_example_inputs(self) -> Tuple[torch.Tensor, ...]:
        return (torch.randn(1, 3, 96, 96),)
