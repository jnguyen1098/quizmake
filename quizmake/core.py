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
        return 1

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
        logging.error(f"{t_folder} either has no tokens or doesn't exist...skipping")
        """
        logging.error("Exiting...")
        return 1
        """

    logging.info(f'Checking path "{q_folder}" for questions')
    if not parser.assert_dir_has_files(q_folder):
        logging.error(f"{q_folder} either has no questions or doesn't exist")
        logging.error("Exiting...")
        return 1

    """
    This is going to be a relatively slow (but important) step where each and
    every token and question file will be validated and parsed into objects.

    For tokens, it's going to be relatively quick, as tokens are delimited
    merely line-by-line.

    For questions, on the other hand... :grimace:
    """

    # TODO: integrate validation and creation into one step
    for token in os.listdir(t_folder):
        logging.debug(f"Testing token {token}")
        if token.startswith("."):
            logging.debug(f"{token} is a hidden file. Skipping")
            continue
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
        if question.startswith("."):
            logging.debug(f"{question} is a hidden file. Skipping.")
            continue
        parser.assert_question_file(q_folder + "/" + question)
        if not parser.assert_question_file(q_folder + "/" + question):
            # TODO: disambiguate between invalid questions and skipped folders
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

    # TODO: proper disambiguation between question types
    def print_question(filename, question):
        if question.type == parser.QuestionType.MULTIPLE_CHOICE:
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

        elif question.type == parser.QuestionType.SHORT_ANSWER:
            question_text = question.sections["question"][0]
            answers = question.sections["answers"]

            print("="*50)
            print(f"{filename}: ", end = "")
            print(question_text)

            print("")
            for i in range(len(answers)):
                print(f"Answer: {answers[i]} ", end = "")
                print()

        elif question.type == parser.QuestionType.MATCHING:
            question_text = question.sections["question"][0]
            left_match = question.sections["left_match"]
            right_match = question.sections["right_match"]

            print("="*50)
            print(f"{filename}: ", end = "")
            print(question_text + "\n")

            if len(left_match) is not len(right_match):
                raise Exception("Number of matching lefts must match right;"
                " also, all question files must end with a blank line")

            for i in range(len(left_match)):
                print(f"{left_match[i]} -> {right_match[i]}")



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
        if question.type == parser.QuestionType.MULTIPLE_CHOICE:
            sections = [
                "question",
                "answers",
                "feedback",
            ]
        elif question.type == parser.QuestionType.SHORT_ANSWER:
            sections = [
                "question",
                "answers",
            ]
        elif question.type == parser.QuestionType.MATCHING:
            sections = [
                "question",
                "left_match",
                "right_match",
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

    def output_gift_mc(question_number, question, filename):
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

    # TODO: after the exhaustive test harness is done,
    #       support multi line answers
    # TODO: do weights
    # TODO: do feedbacks
    def output_gift_sa(question_number, question, filename):
        output = open(filename, "a")
        text = question.sections["question"]
        answers = question.sections["answers"]
        output.write(f'::Q{question_number}::[html]')
        text_cleaned = quick_clean(text[0])
        for i in range(len(answers)):
            # TODO investigate the short answer formatting
            answers[i] = answers[i].replace("#", "\\#").replace("=", "\\=")
        output.write(text_cleaned + "\n")
        output.write('{ ')
        for i in range(len(answers[:-1])):
            output.write('=%100%')
            output.write(answers[i])
            output.write("\n")
        output.write("=")
        output.write(answers[-1])
        output.write('}\n\n')

    # TODO: feedback count checking (make sure it matches)
    #       along with checking equality for left_ and right_match
    def output_gift_m(question_number, question, filename):
        output = open(filename, "a")
        text = question.sections["question"]
        left_match = question.sections["left_match"]
        right_match = question.sections["right_match"]
        output.write(f'::Q{question_number}::[html]')
        text_cleaned = quick_clean(text[0])
        for i in range(len(left_match)):
            # TODO: investigate the matching answers formatting
            left_match[i] = left_match[i].replace("#", "\\#").replace("=", "\\=")
            right_match[i] = right_match[i].replace("#", "\\#").replace("=", "\\=")
        output.write(text_cleaned + "\n")
        output.write('{ ')
        for i in range(len(left_match[:-1])):
            output.write("=")
            output.write(left_match[i])
            output.write(" -> ")
            output.write(right_match[i])
            output.write("\n")
        output.write("=")
        output.write(left_match[-1])
        output.write(" -> ")
        output.write(right_match[-1])
        output.write('}\n\n')

    if args.export_gift:
        logging.info(f"Exporting GIFT to {args.export_gift}!")
        for i in range(len(questions_array)):
            if questions_array[i].type == parser.QuestionType.MULTIPLE_CHOICE:
                output_gift_mc(i + 1, questions_array[i], args.export_gift)
            elif questions_array[i].type == parser.QuestionType.SHORT_ANSWER:
                output_gift_sa(i + 1, questions_array[i], args.export_gift)
            elif questions_array[i].type == parser.QuestionType.MATCHING:
                output_gift_m(i + 1, questions_array[i], args.export_gift)
            else:
                raise Exception("Different question type than expected")
        logging.info("Done!")
    else:
        counter = 0
        for question in questions_array:
            print_question(filenames_array[counter], question)
            counter += 1

    return 0


















