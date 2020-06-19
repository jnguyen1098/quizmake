"""
Regression test cases

Tests to make sure the project doesn't reinstroduce any bugs
"""

from quizmake import quizmake


def test_regression_1() -> None:
    """
    Placeholder
    """
    assert quizmake.return_string() == "string"


def test_regression_2() -> None:
    """
    Placeholder
    """
    assert quizmake.return_string() == "string"


def test_regression_3() -> None:
    """
    Placeholder
    """
    number: str = "10"
    assert number == "10"
