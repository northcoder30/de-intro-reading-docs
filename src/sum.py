def calculate_price_percentage(percentage_changes):
    pass


def test_calculate_total():
    assert calculate_price_percentage([-10, -15]) == 75
    assert calculate_price_percentage([20]) == 120
    assert calculate_price_percentage([]) == 100
    assert calculate_price_percentage([-50, 75]) == 125
