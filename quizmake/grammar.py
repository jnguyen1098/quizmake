# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Grammar module for quizmake's question format(s).

This was mostly an exercise in using pyparsing.
"""

from pyparsing import (
    CaselessLiteral,
    Group,
    Literal,
    OneOrMore,
    ParserElement,
    Optional,
    ParseResults,
    Regex,
    restOfLine,
    ZeroOrMore,
)


def parse_file(filename: str) -> ParseResults:
    """Parse a file using the grammar."""
    return bnf.parseFile(filename)


# This makes sure nothing is whitespace
ParserElement.setDefaultWhitespaceChars("")

"""
Multiple choice question
"""

newline = Literal("\n")

comment_line = Literal("//") + restOfLine + newline

content_line = Regex("[^[].*") + newline.suppress()

question_header = CaselessLiteral("[multiple_choice]") + newline.suppress()
question_section = question_header + OneOrMore(content_line)

answer_header = CaselessLiteral("[answer]") + newline.suppress()
answer_section = answer_header + OneOrMore(content_line)

feedback_header = CaselessLiteral("[feedback]") + newline.suppress()
feedback_section = feedback_header + OneOrMore(content_line)

multiple_choice_q = (
    ZeroOrMore(comment_line).suppress() + Group(question_section) + Group(answer_section) + Group(feedback_section)
)

"""
Short answer question
"""
short_answer_q = Literal("Not implemented")

"""
True-False question
"""
true_false_q = Literal("Not implemented")

"""
Matching question
"""
matching_q = Literal("Not implemented")

"""
Numerical question
"""
numerical_q = Literal("Not implemented")

"""
Essay question (free-form)
"""
essay_q = Literal("Not implemented")

"""
Description (not a question)
"""
description_q = Literal("Not implemented")

"""
Cloze question
"""
cloze_q = Literal("Not implemented")

question = (
    multiple_choice_q
    | short_answer_q
    | true_false_q
    | matching_q
    | numerical_q
    | essay_q
    | description_q
    | cloze_q
)
bnf = question
