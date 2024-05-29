from test_api.checks import run_test, format_err_msg


def add_decimals(fractions_to_add):
    pass


@run_test
def test_add_decimals():
    assert add_decimals(["0.1", "0.2"]) == "0.3", \
        format_err_msg("0.3", add_decimals(["0.1", "0.2"]))

    assert add_decimals(["0.1", "0.1", "0.1", "0.1"]) == "0.4", \
        format_err_msg("0.4", add_decimals(["0.1", "0.1", "0.1", "0.1"]))


if __name__ == '__main__':
    test_add_decimals()
