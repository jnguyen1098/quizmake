# !/usr/bin/env python3

"""
Execute unit tests for token parsing.

Making sure that it parses correctly
"""

from quizmake import parser


def test_token_assert() -> None:
    """Assert the validation of token file."""
    assert not parser.assert_token_file("tests/test_data/empty/")
    assert not parser.assert_token_file(
        "tests/test_data/tokens/invalid_tokens/empty_token"
    )
