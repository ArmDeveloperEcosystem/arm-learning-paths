"""Toy CNN model for smoke testing."""

from __future__ import annotations

from .model import ToyCNNModel
from .. import register_model

register_model("toy_cnn", ToyCNNModel)
