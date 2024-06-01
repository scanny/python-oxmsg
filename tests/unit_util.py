"""Helper functions for use in tests."""

from __future__ import annotations

import pathlib


def test_file_path(name: str) -> str:
    """Return the absolute path to test file having *name*."""
    this_dir_path = pathlib.Path(__file__).parent.absolute()
    return str(this_dir_path / "test_files" / name)
