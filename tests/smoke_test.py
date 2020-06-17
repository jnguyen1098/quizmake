from quizmake import quizmake


def test_return_string():
    assert quizmake.return_string() == "string"


def test_return_string_again():
    assert quizmake.return_string() == "string"


def test_numbers_exist():
    number: str = 10
    assert number == 10
