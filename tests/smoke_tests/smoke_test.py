from quizmake import corpus


def test_corn():
    """
        This function is meant for greatness
    """
    lmao = corpus.Corpus()
    assert lmao is not None
    assert corpus.corn() == "corn"
