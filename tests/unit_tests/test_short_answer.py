# !/usr/bin/env python3
# pylint: skip-file

"""
Execute unit tests for the Question object.

Making sure that it parses correctly
"""

from quizmake import parser

CREATION_CASES = "tests/test_data/questions/unit_test_questions"
VALID_QUESTIONS = "tests/test_data/questions/valid_questions"

# TODO: perhaps fix the discrepancy between the internal "answers" key
#       and the external [answer] section?
# TODO: add commenting to the resultant GIFT file
# TODO: add more cases
# TODO: look at '->' escaping as well as other escapes in GIFT
cases = [
    # fmt: off
    {
        "filename": CREATION_CASES + "/" + "case3.txt",
        "question_type": parser.QuestionType.SHORT_ANSWER,
        "sections": {
            "question": [
                "  Hello there.\n    This is a question on "
                "multiple lines.\n      hehe....\n\n"
            ],
            "answers": [
                "This is an answer line.",
                "That exists on multiple lines.",
                "Because sometimes we need...",
                "Multiple answers, no?",
            ],
        },
    },
    {
        "filename": VALID_QUESTIONS + "/" + "q0014.txt",
        "question_type": parser.QuestionType.SHORT_ANSWER,
        "sections": {
            "question": [
                "What library would you import to use the printf() function?"
            ],
            "answers": [
                "stdio.h",
                "#include <stdio.h>",
                "<stdio.h>",
                "stdio",
            ],
        },
    },
    # fmt: on
]

"""
    {
        "filename": VALID_QUESTIONS + "/" + "q0001.txt",
        "question_type": parser.QuestionType.MULTIPLE_CHOICE,
        "sections": {
            "question": "",
            "answers": [],
            "feedback": [],
        },
    },
"""

# TODO: move the bare questions in valid_questions/ to a dedicated mc folder
# add replacement cases
# TODO: come to terms with the keys of the test case and generalize. 
#       perhaps maybe a single test driver and a bunch of test def files
def test_sa_question_creation() -> None:
    """Assert the creation and return values of a Question."""
    for test_case in cases:
        question = parser.Question(str(test_case["filename"]))

        assert test_case["filename"] == question.filename
        assert test_case["question_type"] == question.type
        # Add case for checking number of feedback == number of answer

        sections = test_case["sections"]
        for key, value in sections.items():  # type: ignore
            assert question.sections[key] == value
