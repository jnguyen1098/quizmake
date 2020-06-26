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

    """
    This is going to be a relatively slow (but important) step where each and
    every token and question file will be validated and parsed into objects.

    For tokens, it's going to be relatively quick, as tokens are delimited
    merely line-by-line.

    For questions, on the other hand... :grimace:

    TODO: in this part of the project, I haven't thought of the top-down
          result of parsing tokens and questions. I just want to parse.

          In the original project, I had a 'DataSet' object that basically
          represented each file in the tokens folder. Then, I had a 'Corpus'
          object that held a dictionary of 'DataSet' objects and a top-level
          interface was made from that. I might do the same, but less messy.

          The original implementation used a very weird index system.
    """

    # PLANNED: integrate validation and creation into one step
    for token in os.listdir(t_folder):
        logging.debug(f"Testing token {token}")
        if not parser.assert_token_file(t_folder + "/" + token):
            logging.error(f"{token} is not a valid token. Skipping...")
        else:
            logging.info(f"{token} is valid...")

    questions_array = []
    for question in os.listdir(q_folder):
        logging.debug(f"Testing question {question}")
        parser.assert_question_file(q_folder + "/" + question)
        if not parser.assert_question_file(q_folder + "/" + question):
            logging.error(f"{question} is not a valid question. Skipping...")
        else:
            logging.info(f"{question} is valid...")
            temp = parser.Question(q_folder + "/" + question)
            questions_array.append(temp)

    return os.EX_OK
