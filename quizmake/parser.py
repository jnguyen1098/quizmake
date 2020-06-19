# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Common helper functions.

This will represent the bread and butter of the application.
"""

import os


def assert_nonempty_dir(folder: str) -> bool:
    """Assert that a directory is not empty and has files."""
    if not os.path.isdir(folder) or not os.listdir(folder):
        return False
    return True


def assert_question_file(question: str) -> bool:
    """Check if a question file has correct structure."""
    return bool(question)


def assert_token_file(token: str) -> bool:
    """Check if a token file has correct structure."""
    return bool(token)
