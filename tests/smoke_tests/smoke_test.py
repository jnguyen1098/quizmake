from quizmake import quizmake as cuntone
from quizmake import corpus as cunttwo


def test_smoke():
    assert cuntone.return_string() == "string"


def test_smoke2():
    assert cuntone.return_string() == "string"


def test_smoke3():
    number: str = 10
    assert number == 10


def test_file():
    corpus_test = cunttwo.Corpus()
    assert corpus_test is not None


def test_corn():
    assert cunttwo.corn() == "corn"
