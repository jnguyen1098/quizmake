from quizmake import quizmake


def test_e2e_1():
    assert quizmake.return_string() == "string"


def test_e2e_2():
    assert quizmake.return_string() == "string"


def test_e2e_3():
    number: str = 10
    assert number == 10
