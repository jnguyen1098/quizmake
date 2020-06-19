# !/usr/bin/env python3

"""
Execute end-to-end test cases.

Tests that go from the very beginning to the very end
"""

from quizmake import quizmake


def test_e2e_1() -> None:
    """Execute random test."""
    assert quizmake.return_string() == "string"


def test_e2e_2() -> None:
    """Execute random test."""
    assert quizmake.return_string() == "string"


def test_e2e_3() -> None:
    """Execute random test."""
    number: str = "10"
    assert number == "10"
