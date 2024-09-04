from test_api.checks import run_test, skip_test, format_err_msg


def is_suspicious(crew_mates):
    if "imposter" in crew_mates:
        return True
    else:
        return False


@run_test
def test_is_not_suspicious():
    assert is_suspicious([]) is False, \
        format_err_msg(False, is_suspicious([]))

    assert is_suspicious(["innocent northcoder"]) is False, \
        format_err_msg(False, is_suspicious(["innocent northcoder"]))

    test_group = ["renegade northcoder",
                  "imposing northcoder", "hard working northcoder"]
    assert is_suspicious(test_group) is False, \
        format_err_msg(False, is_suspicious(test_group))


@run_test
def test_is_suspicious():
    assert is_suspicious(["imposter"]) is True, \
        format_err_msg(True, is_suspicious(["imposter"]))

    test_group = ["northcoder happily doing their tasks",
                  "suspicious northcoder", "imposter"]
    assert is_suspicious(test_group) is True, \
        format_err_msg(True, is_suspicious(test_group))


if __name__ == '__main__':
    test_is_not_suspicious()
    test_is_suspicious()
