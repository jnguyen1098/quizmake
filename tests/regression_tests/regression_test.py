from quizmake import quizmake


def test_regression_1():
    assert quizmake.return_string() == "string"


def test_regression_2():
    assert quizmake.return_string() == "string"


def test_regression_3():
    number: str = 10
    assert number == 10
