"""
Smoke test cases

Testing to see if the system works
"""

import quizmake


def donttest_corn() -> None:
    """
        This function is meant for greatness
    """
    lmao = quizmake.Corpus()
    assert lmao is not None
    assert quizmake.corn() == "corn"
