# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Main function for executing the package
This is the main program logic for when you run::
>>> python3 -m quizmake
"""

from typing import List


def main(argv: List[str]) -> int:
    """
    Main function call

    :param argv: The sys.argv list of command-line args
    :type argv: List[str]
    :return: The exit code of the program, usually 0 if the termination
        is not abnormal. Treat 0 as success
    :rtype: int
    """
    if argv is not None:
        print("Hello! You called the main command for quizmake.")
        print("Right now there isn't much going on, but stay tuned!")
    return 0
