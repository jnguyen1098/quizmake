# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Module that runs when you natively execute the program.

As if one did this:
>>> python3 -m quizmake
"""

import logging
import os
import re
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
            raise Exception(f"{token} is not a valid token.")
            # logging.error(f"{token} is not a valid token. Skipping...")
        else:
            logging.info(f"{token} is valid...")

    logging.info(f"Tokens folder {t_folder} is valid. Parsing files now.")
    try:
        corpus = parser.Corpus(t_folder)
    except Exception as e:
        logging.critical(f"Could not parse tokens folder {t_folder}.")
        logging.critical(f"Exception: {e}")
        exit(1)

    questions_array = []
    filenames_array = []
    for question in os.listdir(q_folder):
        logging.debug(f"Testing question {question}")
        parser.assert_question_file(q_folder + "/" + question)
        if not parser.assert_question_file(q_folder + "/" + question):
            raise Exception(f"{question} is not a valid questiion.")
            # logging.error(f"{question} is not a valid question. Skipping...")
        else:
            logging.info(f"{question} is valid...")
            temp = parser.Question(q_folder + "/" + question)
            questions_array.append(temp)
            filenames_array.append(question)

    class bcolors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'

    def print_question(filename, question):
        question_text = question.sections["question"][0]
        answers = question.sections["answers"]
        feedback = question.sections["feedback"]

        print("="*50)
        print(f"{filename}: ", end = "")
        print(question_text + "\n")

        option_number = 1
        print("")
        for i in range(len(answers)):
            print(f"{option_number}. {answers[i]} ", end = "")
            print(bcolors.OKGREEN + "(correct)" + bcolors.ENDC if i == 0 else "", end = "")
            print(f"\n(Feedback: {feedback[i] if feedback[i].rstrip() else 'None'})")
            option_number += 1
            print()

    identifier = re.compile(r'{([A-Za-z-_]+)([0-9]+)?}')
    custom_call = re.compile(r'{CUSTOM\.([\w\_]+)}')

    def process_line(corpus, line):
        matches = identifier.findall(line)
        for match in matches:
            filename = match[0]
            number = match[1] if match[1] else ''
            original_text = '{' + filename + number + '}'
            if corpus.exists(filename):
                request = corpus.request(filename, int(number if number else 0))
                line = line.replace(original_text, request, 1)
        return line
        

    for question in questions_array:
        corpus = parser.Corpus(t_folder) # TODO: proper corpus reset
        sections = [
            "question",
            "answers",
            "feedback",
        ]
        for section in sections:
            for i in range(len(question.sections[section])):
                question.sections[section][i] = process_line(corpus, question.sections[section][i])

    def quick_clean(dirty_string):
        return dirty_string\
            .replace("\\n", "\\\\n")\
            .replace("~", "\\~")\
            .replace("=", "\\=")\
            .replace("#", "\\#")\
            .replace("{", "\\{")\
            .replace("}", "\\}")\
            .replace(":", "\\:")\
            .replace("<", "&lt;")\
            .replace(">", "&gt;")\
            .replace("    ", "&nbsp;&nbsp;&nbsp;&nbsp;")\
            .replace("\n", "<br>")

    def output_gift(question_number, question, filename):
        output = open(filename, "a")
        text = question.sections["question"]
        answers = question.sections["answers"]
        feedbacks = question.sections["feedback"]
        output.write(f'::Q{question_number}::[html]')
        text_cleaned = quick_clean(text[0])
        for i in range(len(answers)):
            answers[i] = quick_clean(answers[i])
            feedbacks[i] = quick_clean(feedbacks[i])
        output.write(text_cleaned + "\n")
        output.write('{ =')
        for i in range(len(answers[:-1])):
            output.write(answers[i])
            output.write(' # ')
            output.write(feedbacks[i])
            output.write(' ~')
        output.write(answers[- 1])
        output.write(' # ' + feedbacks[-1])
        output.write('}\n\n')

    if args.export_gift:
        logging.info(f"Exporting GIFT to {args.export_gift}!")
        for i in range(len(questions_array)):
            output_gift(i + 1, questions_array[i], args.export_gift)
        logging.info("Done!")
    else:
        counter = 0
        for question in questions_array:
            print_question(filenames_array[counter], question)
            counter += 1

    return os.EX_OK


















