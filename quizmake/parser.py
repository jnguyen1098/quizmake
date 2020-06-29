# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Common helper functions.

This will represent the bread and butter of the application.
"""

import argparse
import copy
import logging
import os
import random
import sys
from enum import Enum
from typing import List, NoReturn

from pyparsing import ParseException

from quizmake import grammar


class QuestionType(Enum):
    """Enumeration of the question types."""

    OTHER = 0
    MULTIPLE_CHOICE = 1
    SHORT_ANSWER = 2
    TRUE_FALSE = 3
    MATCHING = 4
    NUMERICAL = 5
    ESSAY = 6
    DESCRIPTION = 7
    CLOZE = 8


# Question Object
class Question:
    """Used to store question file data."""

    def __init__(self, filename: str) -> None:
        """Create a question using the filename."""
        self.sections = {}
        self.filename = filename
        self.parsed = grammar.parse_file(filename)

        for section in self.parsed:

            if section[0].casefold() == "[multiple_choice]".casefold():
                self.type = QuestionType.MULTIPLE_CHOICE
                question_lines: List[str] = []
                for line in section[1:]:
                    if not line.startswith("//"):
                        question_lines.append(line)
                self.sections["question"] = ["\n".join(question_lines)]

            elif section[0].casefold() == "[answer]".casefold():
                answer_lines: List[str] = []
                for line in section[1:]:
                    if not line.startswith("//"):
                        answer_lines.append(line)
                self.sections["answers"] = answer_lines

            elif section[0].casefold() == "[feedback]".casefold():
                feedback_lines: List[str] = []
                for line in section[1:]:
                    if not line.startswith("//"):
                        feedback_lines.append(line)
                self.sections["feedback"] = feedback_lines
            # TODO: re-add else statement
                

    def speak(self) -> None:
        """Thwart the linter lmao."""
        print(self.sections)

    def speaker(self) -> None:
        """Thwart the linter again."""
        print(self.filename)


# Token database
class TokenSet:
    """Used to store token data."""

    def __init__(self, filename: str) -> None:
        """Create a token list using the filename."""

    def __init__(self, filename):
        with open(filename, "r") as fd:
            self.data = fd.read().splitlines()
            self.data = list(filter(lambda a : a, self.data))
            self.uniques = random.sample(copy.deepcopy(self.data), len(self.data))

    def get_random(self):
        return random.choice(self.data)

    def pop_random(self):
        if self.uniques:
            elem = self.uniques.pop()
            return elem
        return None

    def reset_uniques(self):
        self.uniques = copy.deepcopy(self.data)
        random.shuffle(self.uniques)


# Corpus
class Corpus:
    """Used to store a bunch of tokens and their indexes."""

    # TODO: this is bad
    def __init__(self, tokens_folder):
        self.data = {}
        for filename in os.listdir(tokens_folder):
            self.data[filename] = { 0 : TokenSet(tokens_folder + "/" + filename) }

    def exists(self, filename):
        return filename in self.data

    def request(self, filename, number):
        if not self.exists(filename):
            return None # should raise exception
        if number == 0:
            return self.data[filename][0].get_random()
        if number not in self.data[filename]:
            elem = self.data[filename][0].pop_random()
            if not elem:
                raise Exception(f"No unique strings left in {filename}")
            self.data[filename][number] = elem
        return self.data[filename][number]

    def items(self):
        return self.data.items()


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
        "--export-gift",
        help="specify GIFT export and output filename",
        metavar="FILENAME",
    )
    arg_p.add_argument(
        "-v", "--verbose", help="verbose debug output", action="store_true"
    )

    return arg_p.parse_args(argv)


def assert_nonempty_dir(folder: str) -> bool:
    """
    Assert that a directory is not empty.

    This means subfolders count!

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


def assert_token_file(filename: str) -> bool:
    """
    Check if a token file has correct structure.

    :param filename: File path to the token file
    :type filename: str:
    :return: Truth statement answering the question
    :rtype: bool
    """
    try:
        with open(filename, "r") as token_fp:
            i = 0
            for i, dummy in enumerate(token_fp, 1):
                pass
        return i > 0
    except (OSError, IOError) as exception:
        logging.debug(f"Token file exception: {exception}")
        return False


def assert_question_file(filename: str) -> bool:
    """
    Check if a question file has correct structure.

    :param filename: File path to the question file
    :type filename: str
    :return: Truth statement answering the question
    :rtype: bool
    """
    try:
        # Question(filename)
        list(grammar.parse_file(filename))
        return True
    except ParseException as exception:
        logging.debug(f"Question file exception: {exception}")
        return False
