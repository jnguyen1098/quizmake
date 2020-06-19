# !/usr/bin/env python3

"""
Execute regression test cases.

Tests to make sure the project doesn't reinstroduce any bugs
"""

from quizmake import quizmake


def test_regression_1() -> None:
    """Execute placeholder test."""
    assert quizmake.return_string() == "string"


def test_regression_2() -> None:
    """Execute placeholder tests."""
    assert quizmake.return_string() == "string"


def test_regression_3() -> None:
    """Execute placeholder tests."""
    number: str = "10"
    assert number == "10"
