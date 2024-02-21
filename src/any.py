def is_suspicious(crew_mates):
    pass


def test_is_suspicious():
    assert is_suspicious(["imposter"]) is True
    assert (
        is_suspicious(["innocent northcoder", "hard working northcoder"])
        is False
    )
    assert (
        is_suspicious(["northcoder happily doing their tasks", "imposter"])
        is True
    )
    assert is_suspicious(["suspicious northcoder", "imposter"]) is True
    assert (
        is_suspicious(["renegade northcoder", "imposing northcoder"]) is False
    )
