# !/usr/bin/env python3

"""
Execute integration test cases.

Tests the union of multiple components
"""

import os

from quizmake import core

ROOT_TOKENS_FOLDER = "tests/test_data/questions/"
ROOT_QUESTIONS_FOLDER = "tests/test_data/tokens/"

VALID_TOKENS_FOLDER = "tests/test_data/tokens/valid_tokens/"
VALID_QUESTIONS_FOLDER = "tests/test_data/tokens/valid_questions/"

EMPTY_FOLDER = "tests/test_data/empty/"
NONEXISTENT_FOLDER = "AAAAAAAAAAAAAAAAAAAAA"


def test_nonexistent_tokens_folder() -> None:
    """Ensure program fails on nonexistent tokens folder."""
    args = ["prog", NONEXISTENT_FOLDER, VALID_QUESTIONS_FOLDER]
    assert core.main(args) == os.EX_USAGE


def test_nonexistent_questions_folder() -> None:
    """Ensure program fails on nonexistent questions folder."""
    args = ["prog", VALID_TOKENS_FOLDER, NONEXISTENT_FOLDER]
    assert core.main(args) == os.EX_USAGE


def test_empty_tokens_folder() -> None:
    """Ensure program fails on empty tokens folder."""
    args = ["prog", EMPTY_FOLDER, VALID_QUESTIONS_FOLDER]
    assert core.main(args) == os.EX_USAGE


def test_empty_questions_folder() -> None:
    """Ensure program fails on empty tokens folder."""
    args = ["prog", VALID_TOKENS_FOLDER, EMPTY_FOLDER]
    assert core.main(args) == os.EX_USAGE


def test_tokens_folder_file_assertion() -> None:
    """Catch failure from tokens folder that only has folders"""
    args = ["prog", ROOT_TOKENS_FOLDER, VALID_QUESTIONS_FOLDER]
    assert core.main(args) == os.EX_USAGE


def test_questions_folder_file_assertion() -> None:
    """Catch failure from questions folder that only has folders"""
    args = ["prog", VALID_TOKENS_FOLDER, ROOT_QUESTIONS_FOLDER]
    assert core.main(args) == os.EX_USAGE
