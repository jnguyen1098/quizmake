# !/usr/bin/env python3

"""
Execute smoke test cases.

Testing to see if the system works
"""

from quizmake import core


def test_sanity() -> None:
    """Test for sanity."""
    args = [
        "prog",
        "tests/test_data/tokens/valid_tokens/",
        "tests/test_data/questions/valid_questions/",
    ]
    assert core.main(args) == 0
