# !/usr/bin/env python3

"""
Execute unit tests for the Question object.

Making sure that it parses correctly
"""

from quizmake import parser

CREATION_CASES = "tests/test_data/questions/unit_test_questions"

cases = [
    # fmt: off
    {
        "filename": CREATION_CASES + "/" + "case1.txt",
        "question_type": parser.QuestionType.MULTIPLE_CHOICE,
        "sections": {
            "question": "This is a question line.",
            "answers": "This is an answer line.",
            "feedback": "This is a feedback line.\nSo is this.",
        },
    },
    {
        "filename": CREATION_CASES + "/" + "case2.txt",
        "question_type": parser.QuestionType.MULTIPLE_CHOICE,
        "sections": {
            "question": "  Hello there.\n    This is a question on "
                        "multiple lines.\n      hehe....\n\n",
            "answers": "This is an answer line.\nThat exists on"
                       " multiple lines.\nBecause sometimes we"
                       " need...\nMultiple answers, no?",
            "feedback": "This is a feedback line.\nSo is this.\nasdf"
                        "\nasdf\nasdf\nasdf\nasdf\nasdf\nasdf",
        },
    },
    # fmt: on
]


def test_question_creation() -> None:
    """Assert the creation and return values of a Question."""
    for test_case in cases:
        question = parser.Question(str(test_case["filename"]))
        assert test_case["filename"] == question.filename

        sections = test_case["sections"]
        for key, value in sections.items():  # type: ignore
            assert question.sections[key] == value
