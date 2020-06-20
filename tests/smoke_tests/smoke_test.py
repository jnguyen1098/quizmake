# !/usr/bin/env python3

"""
Execute smoke test cases.

Testing to see if the system works
"""

from quizmake import core


def test_sanity() -> None:
    """Test bad command line arguments."""
    args = ["prog", "tests/test_data/tokens", "tests/test_data/questions"]
    assert core.main(args) == 0
