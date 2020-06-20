# !/usr/bin/env python3

"""
Execute integration test cases.

Tests the union of multiple components
"""

import os

from quizmake import core


def test_nonexistent_tokens_folder() -> None:
    """Ensure program fails on nonexistent tokens folder."""
    args = ["prog", "dskfgjafkgj", "tests/test_data/questions"]
    assert core.main(args) == os.EX_USAGE


def test_nonexistent_questions_folder() -> None:
    """Ensure program fails on nonexistent questions folder."""
    args = ["prog", "tests/test_data/tokens", "209fu09wfe"]
    assert core.main(args) == os.EX_USAGE


def test_empty_tokens_folder() -> None:
    """Ensure program fails on empty tokens folder."""
    args = ["prog", "tests/test_data/empty/", "tests/test_data/questions"]
    assert core.main(args) == os.EX_USAGE


def test_empty_questions_folder() -> None:
    """Ensure program fails on empty tokens folder."""
    args = ["prog", "tests/test_data/tokens", "tests/test_data/empty"]
    assert core.main(args) == os.EX_USAGE
