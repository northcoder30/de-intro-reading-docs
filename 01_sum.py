from test_api.checks import run_test, format_err_msg


def calculate_price_percentage(percentage_changes):
    count = 0
    for i in percentage_changes:
        count += i
    return 100 + count


@run_test
def test_calculate_total():
    assert calculate_price_percentage([-10, -15]) == 75, \
        format_err_msg(75, calculate_price_percentage([-10, -15]))

    assert calculate_price_percentage([20]) == 120, \
        format_err_msg(120, calculate_price_percentage([20]))

    assert calculate_price_percentage([]) == 100, \
        format_err_msg(100, calculate_price_percentage([]))

    assert calculate_price_percentage([-50, 75]) == 125, \
        format_err_msg(125, calculate_price_percentage([-50, 75]))


if __name__ == '__main__':
    test_calculate_total()
