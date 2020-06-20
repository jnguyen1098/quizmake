# !/usr/bin/env python3

"""
Execute unit tests.

Testing each component separately in isolation
"""

import argparse
from typing import List

from quizmake import parser


def test_bad_args() -> None:
    """Test for invalid command-line args."""
    bad_args: List[List[str]] = [["arg1", "arg2", "arg3"], [], ["arg1"]]

    for bad_arg in bad_args:
        try:
            parser.verify_args(bad_arg)
            assert False
        except ValueError:
            pass


def test_valid_args() -> None:
    """Test for valid configurations of command-line args."""
    try:
        assert parser.verify_args(["arg1", "arg2"])
        assert parser.verify_args(["arg1", "arg2", "-v"])
        assert parser.verify_args(["arg1", "arg2", "--verbose"])
    except argparse.ArgumentError:
        assert False


def test_nonempty_dir_assertions() -> None:
    """Test folder I/O reading."""
    # Existent tokens folder
    assert parser.assert_nonempty_dir("tests/test_data/tokens")
    # Existent questions folder
    assert parser.assert_nonempty_dir("tests/test_data/questions")
    # Nonexistent folder
    assert not parser.assert_nonempty_dir("kasjdfs")
    # Existent but empty folder
    assert not parser.assert_nonempty_dir("tests/test_data/empty")
