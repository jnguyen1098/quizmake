# !/usr/bin/env python3

"""
Execute unit tests.

Testing each component separately in isolation
"""

from quizmake import parser, quizmake


def test_nonempty_dir_assertions() -> None:
    """Test folder I/O reading."""
    # Existent tokens folder
    assert parser.assert_nonempty_dir("tests/test_data/tokens")
    # Existent questions folder
    assert parser.assert_nonempty_dir("tests/test_data/questions")
    # Nonexistent folder
    assert not parser.assert_nonempty_dir("kasjdfs")
    # Existent but empty folder
    assert not parser.assert_nonempty_dir("tests/unit_tests/empty")


def test_unit_1() -> None:
    """Execute placeholder test."""
    assert quizmake.return_string() == "string"


def test_unit_2() -> None:
    """Execute placeholder test."""
    assert quizmake.return_string() == "string"


def test_unit_3() -> None:
    """Execute placeholder test."""
    number: str = "10"
    assert number == "10"
