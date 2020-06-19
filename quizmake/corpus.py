# !/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Corpus module used for storing tokens' data.

I might just deprecate this.
"""

__license__ = "MIT"
__revision__ = "not_defined"
__docformat__ = "reStructuredText"


class Corpus:
    """This is just the Corpus class to hold datasets.

    There is a function :func:`speak` that just speaks the
    field `amazing`.

    :param nothing: description I guess
    :param nothing2: description again I guess
    :type nothing: int
    :type nothing2: str
    :return: everything
    :rtype: int
    """

    def __init__(self) -> None:
        """Initiate the Corpus class."""
        self.amazing = "lmao"

    def speak(self) -> None:
        """Speak the assigned word."""
        print(self.amazing)

    def yell(self) -> None:
        """Say random stuff."""
        print(self.amazing + " LMaO")


def corn() -> str:
    """Return the string corn."""
    return "corn"
