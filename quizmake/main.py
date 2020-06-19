# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Module that runs when you natively execute the program.

As if one did this:
>>> python3 -m quizmake
"""

import argparse
import logging
import os
from pathlib import Path
from typing import List


def main(argv: List[str]) -> int:
    """
    Take in the user's question queries and process them.

    :param argv: The sys.argv list of command-line args
    :type argv: List[str]
    :return: The exit code of the program, usually.
    :rtype: int
    """
    # Parse arguments
    parser = argparse.ArgumentParser()

    """
    Validate argument syntax

        tokens
            the location of the tokens folder

        questions
            the location of the questions folder
    """

    parser.add_argument("tokens", help="specify tokens folder")
    parser.add_argument("questions", help="specify questions folder")
    parser.add_argument(
        "-v", "--verbose", help="verbose debug output", action="store_true"
    )

    args = parser.parse_args()

    # Set up logging
    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="[%(levelname)s] %(message)s",
    )

    logging.info("Logging initiated")

    """
    Not only do both `tokens` and `questions` must exist as directories
    have to exist as directories: they must also have a nonzero amount
    of valid files (question/answer, tokens, etc.)

    In the original script that I made, it would only check for existence
    of the directories but never the validity of the files themselves. This
    meant that the program would not realize this until much later in the
    export of the resultant files. Here I am to save some time.
    """

    questions_folder = Path(args.questions)
    tokens_folder = Path(args.tokens)

    logging.info(f'Checking path "{questions_folder}" for questions')
    logging.info(f'Checking path "{tokens_folder}" for tokens')

    print(argv)

    return os.EX_OK
