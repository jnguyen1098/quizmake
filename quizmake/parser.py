# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Common helper functions.

This will represent the bread and butter of the application.
"""

import argparse
import os
import sys
from typing import List, NoReturn


class CaughtArgumentParser(argparse.ArgumentParser):
    """Overridden argparse.ArgumentParser class.

    The original ArgumentParser, when encountering an error, would
    completely exit the program. For my testing purposes (and due
    to the fact that I am still very new to PyTest), I ended up
    intercepting the parse_args() call to raise an exception instead
    of outright quitting the program with sys.exit()
    """

    def error(self, message: str) -> NoReturn:
        """Override argparse.ArgumentParser error to not exit."""
        self.print_usage(sys.stderr)
        args = {"prog": self.prog, "message": message}
        sys.stderr.write("%(prog)s: error: %(message)s\n" % args)
        raise ValueError()


def verify_args(argv: List[str]) -> argparse.Namespace:
    """
    Verify the caller's arguments w.r.t. quizmake.

    :param argv: The sys.argv list of command-line args
    :type argv: List[str]
    :return: Dictionary of command-line arguments
    :rtype: Dict[Str, Str]
    """
    arg_p = CaughtArgumentParser()

    arg_p.add_argument("tokens", help="specify tokens folder")
    arg_p.add_argument("questions", help="specify questions folder")
    arg_p.add_argument(
        "-v", "--verbose", help="verbose debug output", action="store_true"
    )

    return arg_p.parse_args(argv)


def assert_nonempty_dir(folder: str) -> bool:
    """
    Assert that a directory is not empty.

    :param folder: the folder
    :type folder: str
    :return: Truth statement
    :rtype: bool
    """
    if not os.path.isdir(folder) or not os.listdir(folder):
        return False
    return True


def assert_dir_has_files(folder: str) -> bool:
    """
    Assert that a directory has files.

    This differs from the assert_nonempty_dir function
    because a folder with no files but only subfolders
    will return true when passed through that function.

    :param folder: The folder
    :type folder: str
    :return: Truth statement
    :rtype: bool
    """
    if not assert_nonempty_dir(folder):
        return False

    count = 0
    for _ in os.listdir(folder):
        if os.path.isfile(folder + "/" + _):
            count += 1

    return count > 0


def assert_question_file(question: str) -> bool:
    """Check if a question file has correct structure."""
    return bool(question)


def assert_token_file(token: str) -> bool:
    """Check if a token file has correct structure."""
    return bool(token)
