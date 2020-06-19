# !/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Corpus module (for storing variable data)
"""

__license__ = "MIT"
__revision__ = "not_defined"
__docformat__ = "reStructuredText"


class Corpus:
    """This is just the Corpus class to hold datasets

    There is a function :func:`speak` that just speaks the
    field `amazing`.

    - **parameters**, **types**, **return** and **return types**::

        :param nothing: description I guess
        :param nothing2: description again I guess
        :type nothing: int
        :type nothing2: str
        :return: everything
        :rtype: int

    - and to provide sections such as **Example**::

        :Example:


    """

    def __init__(self) -> None:
        self.amazing = "lmao"

    def speak(self) -> None:
        """
        This will just make the Corpus speak its assigned word
        """
        print(self.amazing)

    def yell(self) -> None:
        """
        This will also just make the corpus say random stuff
        """
        print(self.amazing + " LMaO")


def corn() -> str:
    """
    Returns the string 'corn' lmao

    Parameters
    ----------
    nothing : None
        This is just a placeholder

    Returns
    -------
    nothing
        None lmao
    """
    return "corn"
