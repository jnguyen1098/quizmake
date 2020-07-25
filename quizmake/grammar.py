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

newline = Literal("\n")

comment_line = Literal("//") + restOfLine + newline

content_line = Regex("[^[].*") + newline.suppress()

"""
Multiple choice question
"""

mc_question_header = CaselessLiteral("[multiple_choice]") + newline.suppress()
mc_question_section = mc_question_header + OneOrMore(content_line)

mc_answer_header = CaselessLiteral("[answer]") + newline.suppress()
mc_answer_section = mc_answer_header + OneOrMore(content_line)

mc_feedback_header = CaselessLiteral("[feedback]") + newline.suppress()
mc_feedback_section = mc_feedback_header + OneOrMore(content_line)

multiple_choice_q = (
    ZeroOrMore(comment_line).suppress() + Group(mc_question_section) + Group(mc_answer_section) + Group(mc_feedback_section)
)

"""
Short answer question
"""
sa_question_header = CaselessLiteral("[short_answer]") + newline.suppress()
sa_question_section = sa_question_header + OneOrMore(content_line)

sa_answer_header = CaselessLiteral("[answer]") + newline.suppress()
sa_answer_section = sa_answer_header + OneOrMore(content_line)

short_answer_q = (
    ZeroOrMore(comment_line).suppress() + Group(sa_question_section) + Group(sa_answer_section)
)

"""
True-False question
"""
true_false_q = Literal("Not implemented")

"""
Matching question
"""
m_question_header = CaselessLiteral("[matching]") + newline.suppress()
m_question_section = m_question_header + OneOrMore(content_line)

m_left_answer = CaselessLiteral("[left_match]") + newline.suppress()
m_left_section = m_left_answer + OneOrMore(content_line)

m_right_answer = CaselessLiteral("[right_match]") + newline.suppress()
m_right_section = m_right_answer + OneOrMore(content_line)

matching_q = (
    ZeroOrMore(comment_line).suppress()
    + Group(m_question_section)
    + Group(m_left_section)
    + Group(m_right_section)
)

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
