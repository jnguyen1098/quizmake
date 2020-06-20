# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Module that runs when you natively execute the program.

As if one did this:
>>> python3 -m quizmake
"""

import logging
import os
from typing import List

from quizmake import parser


def main(argv: List[str]) -> int:
    """
    Take in the user's question queries and process them.

    :param argv: The sys.argv list of command-line args
    :type argv: List[str]
    :return: The exit code of the program, usually.
    :rtype: int
    """
    try:
        args = parser.verify_args(argv[1:])
    except ValueError:
        return os.EX_USAGE

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

    t_folder = args.tokens
    q_folder = args.questions

    logging.info(f'Checking path "{t_folder}" for tokens')
    if not parser.assert_dir_has_files(t_folder):
        logging.error(f"{t_folder} either has no tokens or doesn't exist")
        logging.error("Exiting...")
        return os.EX_USAGE

    logging.info(f'Checking path "{q_folder}" for questions')
    if not parser.assert_dir_has_files(q_folder):
        logging.error(f"{q_folder} either has no questions or doesn't exist")
        logging.error("Exiting...")
        return os.EX_USAGE

    # Verify every question/token file

    for question in os.listdir(q_folder):
        if not parser.assert_question_file(question):
            logging.error(f"{question} is not a valid question. Skipping...")
        else:
            logging.info(f"{question} is valid...")

    for token in os.listdir(t_folder):
        if not parser.assert_token_file(token):
            logging.error(f"{token} is not a valid token. Skipping...")
        else:
            logging.info(f"{token} is valid...")

    return os.EX_OK
