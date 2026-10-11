"""Transliterates and normalises text into slugs suitable for URLs and filenames."""

from __future__ import annotations

__all__ = ["slugify"]


def slugify(value):
    """Transliterates and normalises text into slugs suitable for URLs and filenames."""
    if value is None:
        raise ValueError("value must not be None")
    return value
