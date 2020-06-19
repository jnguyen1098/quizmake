# !/usr/bin/env python3

"""
Execute integration test cases.

Tests the union of multiple components
"""

from quizmake import quizmake


def test_integration_1() -> None:
    """Execute placeholder test."""
    assert quizmake.return_string() == "string"


def test_integration_2() -> None:
    """Execute placeholder test."""
    assert quizmake.return_string() == "string"


def test_integration_3() -> None:
    """Execute placeholder test."""
    number: str = "10"
    assert number == "10"
