# !/usr/bin/env python3

"""
Execute unit tests.

Testing each component separately in isolation
"""

from quizmake import quizmake


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
