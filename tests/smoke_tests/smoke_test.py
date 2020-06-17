from quizmake import quizmake


def test_smoke():
    assert quizmake.return_string() == "string"


def test_smoke2():
    assert quizmake.return_string() == "string"


def test_smoke3():
    number: str = 10
    assert number == 10
