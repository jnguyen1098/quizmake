from quizmake import quizmake


def test_integration_1():
    assert quizmake.return_string() == "string"


def test_integration_2():
    assert quizmake.return_string() == "string"


def test_integration_3():
    number: str = 10
    assert number == 10
