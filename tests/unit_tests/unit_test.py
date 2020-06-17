from quizmake import quizmake


def test_unit_1():
    assert quizmake.return_string() == "string"


def test_unit_2():
    assert quizmake.return_string() == "string"


def test_unit_3():
    number: str = 10
    assert number == 10
