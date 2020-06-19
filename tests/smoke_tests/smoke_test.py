# !/usr/bin/env python3

"""
Execute smoke test cases.

Testing to see if the system works
"""

import quizmake


def test_corn() -> None:
    """Execute placeholder test."""
    lmao = quizmake.Corpus()
    assert lmao is not None
    assert quizmake.corn() == "corn"
